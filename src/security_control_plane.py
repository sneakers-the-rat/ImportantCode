# ---------------------------------------------------------------------------
# PolicyEngine (Extended Version)
# ---------------------------------------------------------------------------

from __future__ import annotations

import asyncio
import datetime
import hashlib
import hmac
import json
import logging
import os
import secrets
import signal
import socket
import sys
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Constants & Utilities (Extended)
# ---------------------------------------------------------------------------

DEFAULT_SESSION_TTL_SECONDS = 3600  # Default session duration in seconds
DEFAULT_CREDENTIAL_TTL_SECONDS = 86400   # Credential rotation interval in seconds
MAX_PENDING_TICKETS_PER_SESSION = 15    # Maximum concurrent pending tickets per session
POLICY_DENY_DEFAULT = "Default deny"

class PolicyDecision(Enum):
    ALLOW = "ALLOW"      # Action may proceed without human intervention
    APPROVE = "APPROVE"   # Action requires a one-time signed approval ticket
    DENY = "DENY"       # Action is blocked outright


@dataclass
class SecurityControlPlaneError(Exception):
    """Exception raised when an error occurs during control plane operations."""

    message: str
    details: Optional[Dict[str, Any]] = None

def log_error(message: str) -> None:
    logging.error(f"[ERROR] {message}")


@dataclass
class SecurityControlPlaneInfo:
    """Information about the current state of the control plane."""

    active_sessions: int = 0
    pending_ticket_count: int = 0
    credential_versions: List[str] = field(default_factory=list)
    audit_integrity_status: str = "UNKNOWN"


class SecurityControlPlane:
    """
    The top-level security control plane.

    This class orchestrates the entire chain of events from session creation,
    policy evaluation, approval ticket issuance/redeemment, and credential rotation.
    It provides a unified interface for interacting with all subsystems (policy engine,
    broker, vault) while maintaining audit logging.
    """

    def __init__(self):
        self._audit = AuditChain()
        
        # Configuration parameters
        self.session_ttl_seconds: int = DEFAULT_SESSION_TTL_SECONDS
        self.credential_ttl_seconds: int = DEFAULT_CREDENTIAL_TTL_SECONDS
        
        # State management
        self.active_sessions: Dict[str, SessionContext] = {}  # session_id -> context
        self._pending_tickets: Set[ApprovalTicket] = set()   # Pending tickets for approval
        self._ticket_counter: Optional[int] = None

        # Policies registry (for future expansion)
        self.policy_registry: Dict[str, Callable[[Dict], Any]] = {}  # action_type -> handler
        
        # Audit logging setup
        self._loggers = {
            "control-plane": SecurityControlPlaneInfo(),
            "agent": LoggingHandler("security_agent"),
            "human_human": LoggingHandler("user_human") if hasattr(os, 'login') else None,
        }

    def _get_logger(self) -> logging.Logger:
        """Get the appropriate logger based on context."""
        level = self._loggers.get_level() or logging.INFO
        
        # Determine actor type for log levels
        actors: Dict[str, str] = {
            "agent": SecurityControlPlaneInfo(),  # Default to control-plane agent logs if not set
            "user_human": LoggingHandler("security_agent"),
            "human_human": LoggingHandler(os.environ.get('USER_HUMAN_LOG', 'system')) or None,
        }

        return logging.getLogger(f"{level.name}.{actors[actor]}")


class AuditChain:
    """
    Centralized audit chain for tracking security events.

    Provides methods to append events (audit entries), retrieve them via JSON export,
    verify integrity, and manage the state of all stored actions.
    """

    def __init__(self) -> None:
        self._entries = []  # List of AuditEntry objects
        self._last_event_time: Optional[datetime] = None
        
        # Initialize a default entry for system initialization if not present
        if len(self._entries) == 0 and os.path.exists('/etc/security/control-plane-init.json'):
            with open("/etc/security/control-plane-init.json", "w") as f:
                json.dump({
                    "version": "1.0",
                    "timestamp": datetime.datetime.utcnow().isoformat(),
                    "status": "initialized"
                }, f)

    def append(self, event_type: str, actor: Any = None, outcome: str = "success") -> AuditEntry:
        """Append a
