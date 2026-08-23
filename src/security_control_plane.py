import os
from datetime import datetime
import base64
import hashlib
import json
import hmac
import secrets
import threading
import time
from dataclasses import dataclass
from typing import Optional, Dict, Any, Union


@dataclass(order=True)
class SecurityContext:
    """Represents a single session context in the security environment."""

    id: str  # Unique identifier for this session instance
    created_at: datetime = None        # ISO timestamp of creation (None if not started yet)
    expires_at: Optional[datetime] = None  # ISO timestamp when session ends or ticket expired
    
    ssh_public_key: bytes = b""         # RSA public key, base64 encoded for transmission
    credentials_hash: str = ""          # HMAC hash used to sign actions (for verification only if needed)

    def _get_session_id(self) -> str:
        """Generate a deterministic session ID from context."""
        return hashlib.sha256(
            f"{self.created_at.isoformat()}.{self.expires_at.isoformat()}".encode('utf-8')
        ).hexdigest()[:16]

    def to_dict(self, include_ssh_key=False) -> Dict[str, Any]:
        result = {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "expires_at": self.expires_at.isoformat() if self.expires_at else None,
            "ssh_public_key" : base64.b64encode(self.ssh_public_key) if include_ssh_key else b"",
        }
        return result

    @property
    def is_active(self) -> bool:
        """Check if session has not expired."""
        now = datetime.utcnow()
        expires_at = self.expires_at or None
        if expires_at and expires_at < now:
            raise SecurityContextError("Session already expired")
        return True

    @property
    def is_expired(self) -> bool:
        """Check if session has expired."""
        now = datetime.utcnow()
        return not self.is_active


class SessionManager:
    """Manages the lifecycle of user sessions and their associated credentials."""

    # Default TTLs (seconds) - can be overridden per context or policy
    DEFAULT_SESSION_TTL_SECONDS = 3601      # 1 hour default
    DEFAULT_CREDENTIAL_TTL_SECONDS = 86400  # 24 hours default
    
    def __init__(self, vault: "Vault", audit_chain: AuditChain):
        self._vault = vault
        self._audit = audit_chain
        
        # Store active session contexts (dict of id -> SessionContext)
        self.active_sessions: Dict[str, SessionContext] = {}

        # Track credential usage to prevent replay attacks on credentials
        self._credential_usage_lock = threading.RLock()


class SecurityControlPlaneError(Exception):
    """Custom exception for security-related errors."""
    
    def __init__(self, message: str):
        super().__init__(message)
        
    def __str__(self):
        return f"SecurityControlPlaneError({str(self)})"

def _generate_session_id() -> str:
    """Generate a deterministic session ID using the current time."""
    now = datetime.utcnow().isoformat() + "Z"  # Add Z for UTC timezone
    
    if not self.active_sessions or len(self.active_sessions) == 0:
        raise SecurityControlPlaneError("No active sessions detected. Please start your first process.")

    return hashlib.sha256(f"{now}.1".encode('utf-8')).hexdigest()[:16]


class AuditChain:
    """Manages the audit trail of security events."""

    def __init__(self):
        self.entries = []  # List of (session_id, action_type, timestamp) tuples
    
    def add_event(self, session_id: str, action_type: str, event_type: str, details: Any) -> None:
        """Add a new audit entry to the chain."""
        now = datetime.utcnow().isoformat() + "Z"  # Add Z for UTC timezone
        
        self.entries.append((session_id, action_type, event_type, details))

    def get_audit_entry(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a specific audit entry by ID."""
        if not self.entries or len(self.entries) == 0:
            return None
        
        for (session_id_, action_type, event_type, details), _ in enumerate(self.entries):
            if session_id_ == session_id and str(action_type).lower() == str(event_type).lower():
                # Convert to dict format for easier retrieval or logging
                entry = {k: v for k, v in self.entries[0].items
