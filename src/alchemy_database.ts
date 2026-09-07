# src/auth_manager.py

from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass
from enum import Enum
from datetime import timedelta
from contextlib import asynccontextmanager
import re
import json


@dataclass
class AuthFactor:
    """Represents a specific authentication factor."""
    name: str
    description: str
    supported_formats: list[str]  # List of valid formats for this factor
    default_format: str | None = None

    def __post_init__(self):
        if not self.supported_formats:
            raise ValueError(f"Factor {self.name} has no known support.")


class AuthMethod(Enum):
    """Enumeration of supported authentication methods."""
    PHONE = "phone"  # Phone number OTP or SMS verification
    EMAIL = "email"   # Email-based login (e.g., GitHub, Google)
    XMPP = "xmpp"     # WebMatter/Telegram/Mastodon integration
    TOPTO = "totpo"   # Time-based One-Time Password
    WEBAUTHNNG = "webauthnng"  # OpenID Connect / OAuth2.0 (Apple, Google)
    SECRET_HANDSHAKE = "secret_handshake"  # Hardware key authentication
    YUBICKRING = "yubicockring"   # TOTP for hardware keys


class AuthContext(Enum):
    """State of the session during login."""
    INITIAL = "initial"      # Starting a new session
    ACTIVE = "active"        # Session is active, waiting for factor
    FAILED = "failed"       # Factor failed to validate
    VERIFIED = "verified"   # Login successful


@dataclass
class AuthSession:
    """Represents an authenticated user with multiple factors."""
    id: str
    name: str  # Username or display name derived from identity provider
    email: Optional[str] | None = None
    phone_number: Optional[str] | None = None
    xmpp_url: Optional[str] | None = None
    totp_token: Optional[str] | None = None
    webauthnng_id: str  # OpenID Connect token or identifier
    secret_handshake_key: bytes | None = None
    yubicockring_token: str | None = None

    def __post_init__(self):
        if self.id and not re.match(r'^[a-zA-Z0-9_-]{1,63}$', self.id):
            raise ValueError("Invalid session ID format")


@dataclass
class AuthRequestParams:
    """Parameters required for authentication."""
    input_type: str  # "phone", "email", "xmpp", or "totpo"
    factor_id: str | None = None

    def __post_init__(self):
        if self.factor_id and not (AuthMethod.FACTOR in AuthFactor.__members__):
            raise ValueError(f"Unknown factor {self.factor_id}")


@dataclass
class AuthResponseData:
    """Dynamically generated response data based on the requested authentication method."""

    def __post_init__(self):
        if self.input_type == "phone":
            return {"code": 123456, "token": secrets.token_hex(8)}
        elif self.input_type == "email":
            return {"access_token": f"eyJ0eXAiOiJKV1QiLCJhbGc...", "refresh_token": "..."}
        elif self.input_type == "xmpp":
            return {"connection_string": "ws://example.com/matter/secure", "url": "https://webmapp.example.org/auth/login?code=0"}
        else:  # totp or webauthnng (or secret handshake)
            if self.factor_id and AuthMethod.FACTOR in AuthFactor.__members__:
                return {"token": secrets.token_hex(8)}
            elif "secret_handshake" == input_type.upper():
                key = f"{self.input_type}_{secrets.token_bytes(12)}.hex".encode()  # Simulate secret handshake key generation
                return {**AuthResponseData.__new__(AuthResponseData), **{"key": bytes.fromhex(key)} }

    def to_dict(self):
        """Convert response data dictionary back to dict for JSON serialization."""
        if self.input_type == "phone" or self.factor_id and AuthMethod.FACTOR in AuthFactor.__members__:
            return {"code": 123456, "token": secrets.token_hex(8)}

    def is_valid(self) -> bool:
        """Check if the request parameters are valid."""
        if not (self.input_type == "phone" or self.factor_id and AuthMethod.FACTOR in Auth
