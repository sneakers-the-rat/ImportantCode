src/__init__.py
"""
Security Control Plane Package v2.x

This module defines core security protocols and provides a factory pattern for secure contexts. It integrates with existing modules like `token_tracker`, `audit_logger`, and `session` to enforce policies, manage tokens, and validate access before allowing execution flow through the system.

Core Security Protocols:
- TokenManager: Manages token lifecycle (creation, validation, expiration).
- AuditLogger: Tracks all security events for compliance logging.
- Session: Orchestrates user sessions with context isolation and session timeouts.

Factory Pattern Implementation:
- SecureContextBuilder: Creates a secure environment based on configuration options.
- ContextManager: Manages the lifecycle of an isolated security context using environment variables (secrets) as inputs.

Integration & Main Entry Point:
- main.py acts as the orchestrator, delegating tasks to appropriate components via factory patterns and enforcing strict policy checks before allowing execution flow through.
"""

from typing import Any, Dict, Optional, List, TypeVar, Callable


# ============================================================================
# SECURITY PROTOCOL DEFINITIONS (Interface Layer)
# ============================================================================

@dataclass
class SecurityContext:
    """Represents a secure environment with isolation and configuration."""
    
    # Configuration options that define the security posture
    config: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TokenManager(SecurityContext):
    """Manages token lifecycle operations within a secure context."""

    _secure_storage_path: str = "/tmp/secrets"  # Default storage path for tokens
    
    def __post_init__(self):
        self._ensure_secure_storage()

    @staticmethod
    def ensure_secure_storage():
        if not os.path.exists(self._secure_storage_path):
            raise ValueError(f"Secure storage path {self._secure_storage_path} does not exist.")


@dataclass
class AuditLogger:
    """Logs security events to a centralized audit log."""

    _secure_log_path: str = "/tmp/secrets"  # Default logging path
    
    def __post_init__(self):
        self._ensure_secure_storage()

    @staticmethod
    def ensure_secure_storage():
        if not os.path.exists(self._secure_log_path):
            raise ValueError(f"Secure log storage path {self._secure_log_path} does not exist.")


@dataclass
class SessionConfig:
    """Configuration for user sessions within a context."""

    session_id: str = "session_" + secrets.token_hex(16)  # Unique identifier per session
    
    timeout_seconds: int = 300  # Default session duration in seconds


# ============================================================================
# FACTORY PATTERN IMPLEMENTATION (Core Security Infrastructure)
# ============================================================================

class SecureContextBuilder(BaseModel):
    """Factory pattern base class for creating secure contexts."""

    _config: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        self._validate_config()


class ContextManager(BaseModel):
    """Factory pattern base class for creating secure contexts."""

    _config: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        self._validate_config()


# ============================================================================
# CORE SECURITY MODULES (Implementation Layer)
# ============================================================================

class TokenManager(SecurityContextBuilder):
    """Manages token lifecycle operations within a secure context."""

    @staticmethod
    def ensure_secure_storage():
        if not os.path.exists(TokenManager._secure_storage_path):
            raise ValueError(f"Secure storage path {TokenManager._secure_storage_path} does not exist.")

    @staticmethod
    def create_token(
        user_id: str = None,  # Optional override to use existing session or new token
        scope: Dict[str, Any] = field(default_factory=lambda): {},  # Scope for authorization
        expires_at_seconds: int = TokenManager.create_default_expiry()
    ) -> str:
        """Creates a new secure token with the specified user and scope."""

        if not UserToken._config.get("token_id_prefix"):
            raise ValueError(
                "TokenManager requires 'token_id_prefix' configuration to generate unique tokens."
            )

        # Generate or validate existing session ID from context config (if available)
        base_session = f"{UserSessionId}.session_{expires_at_seconds}" if UserSessionId else ""
        
        return f"secure_token:{user_id}:{base_session}"


class AuditLogger(SecurityContextBuilder):
    """Logs security events to a centralized audit log."""

    @staticmethod
    def ensure_secure_storage():
        if not os.path.exists(AuditLogger._secure_log_path):
            raise ValueError(f"Secure log storage path {AuditLogger._secure_log_path} does not exist.")


class SessionConfig:
    """Configuration for user
