# ---------------------------------------------------------------------------
# PolicyEngine (Extended) – Comprehensive Security Control Plane with 
# Session Lifecycle Management and Credential Rotation Policies
# ---------------------------------------------------------------------------

from dataclasses import dataclass
import hmac
import hashlib
import secrets
import time
from datetime import timedelta, timezone
from typing import Optional, Dict, Any, List, Callable, Union
from enum import Enum
import threading
import functools
import logging
import sys
import json
import os
# ---------------------------------------------------------------------------

@dataclass
class SecurityContext:
    """A single user session context."""
    
    # Core identity and credentials
    id_token: str  # Client ID for this specific instance of the agent
    client_id: Optional[str] = None
    
    # Session lifecycle state (expires_at)
    expires_at: datetime | None = None
    created_at: datetime = timezone.utc()
    
    # Authentication keys derived from vault credentials
    session_key: bytes  # HMAC key for this specific session context
    auth_token: Optional[str] = None
    
    # Action history tracking (for audit)
    action_history: List[Dict[str, Any]] = []
    
    def __post_init__(self):
        if self.expires_at is not None and time.time() > self.expires_at + timedelta(minutes=5):  # 5 min grace period
            raise RuntimeError("Session expires before user leaves")

@dataclass
class AuditEntry:
    """Record in the audit chain."""
    
    session_id: str
    event_type: str
    actor: str = "system"
    outcome: str = "unknown"  # success, denied, ticket_rejected, etc.
    metadata: Dict[str, Any] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "session_id": self.session_id,
            "event_type": self.event_type,
            "actor": self.actor,
            "outcome": self.outcome,
            "metadata": json.dumps(self.metadata or {}),
        }

@dataclass
class Action:
    """A single action to be executed."""
    
    session_id: str  # ID of the user's session this belongs to
    action_type: str      # The command name (e.g., 'send_email')
    parameters: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.session_id is None or not isinstance(self.session_id, str):
            raise ValueError("Session ID must be a non-empty string")

class SecurityControlPlane:
    """
    The central security orchestrator.
    
    Features include:
      - Session lifecycle management (start/end)
      - Policy-driven action execution with ApprovalTicket mechanism
      - Credential rotation on sensitive operations
      - Comprehensive audit logging and integrity verification
      - Automatic credential expiration based on session policy
    
    Configuration parameters:
      - master_secret: The secret key for HMAC signing (64 bytes recommended)
      - session_ttl_seconds: How long a new session is valid before revocation
      - credential_ttl_seconds: How long credentials are stored in vault (default 30 days)
    """

    DEFAULT_SESSION_TTL_SECONDS = 2592000        # 1 week for security context
    DEFAULT_CREDENTIAL_TTL_SECONDS = 604800       # One year for credential storage
    
    def __init__(self, master_secret: Optional[bytes] = None):
        self._master_secret = master_secret or secrets.token_bytes(32) if isinstance(master_secret, bytes) else master_secret
        
        logging.basicConfig(level=logging.INFO)
        
        # Initialize audit chain (empty initially for health check only)
        self._audit_chain = AuditChain()

    def _get_hmac_key(self):
        """Generate a unique HMAC signing key derived from the vault."""
        return hmac.new(
            self._master_secret, 
            "system",  # SHA-256 of master secret to ensure uniqueness per session
            digestmod=HMAC_ALGO_SHA_256,
            hashlib=True
        ).digest()

    def _get_credential_key(self):
        """Generate a unique credential rotation key."""
        return hmac.new(
            self._master_secret + str(time.time()),  # Time to ensure uniqueness per session
            "system", 
            digestmod=HMAC_ALGO_SHA_256,
            hashlib=True
        ).digest()

    def _sign_message(self, data: bytes) -> bytes:
        """Create an HMAC signature for the given message."""
        key = self._get_hmac_key()
        return hmac.new(key.encode("utf-8"), data, digestmod=HMAC_ALGO_SHA_256).digest()
