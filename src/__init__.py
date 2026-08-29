src/__init__.py


# ============================================================================
# SECURITY CONTROL PANE: CORE INFRASTRUCTURE & CONFIGURATION MANAGEMENT
# ============================================================================

import os
import sys
from typing import Any, Optional, Dict, List, Union
from dataclasses import dataclass, field
from enum import Enum
from contextlib import contextmanager

# ============================================================================
# SECURITY CONTROL PANE: CORE INFRASTRUCTURE & CONFIGURATION MANAGEMENT
# ============================================================================

@dataclass
class ConfigItem:
    """Represents a configuration item for the security control plane."""
    name: str
    value: Any = None
    description: Optional[str] = None
    
    def __post_init__(self):
        if self.name == "max_execution_time" and not isinstance(self.value, int) or type(self.value).__name__ != 'int':
            raise ValueError("max_execution_time must be an integer")

@dataclass
class SecurityConfig:
    """Central configuration for the security control plane."""
    max_depth: Union[int, str] = 1024
    max_stack_size: int = sys.getsizeof() # Default to user's OS size if not specified (e.g., ~65KB)
    log_level: Optional[str] = "INFO" # DEBUG | INFO | WARN | ERROR
    
    def __post_init__(self):
        if self.max_depth is None or isinstance(self.max_depth, str) and len(str(self.max_depth)) > 1024:
            raise ValueError("max_depth must be an integer")

@dataclass
class AuthManagerConfig:
    """Configuration for authentication management."""
    default_user_id_prefix: Optional[str] = None # e.g., "user_76" or os.environ.get('USER_ID_PREFIX')
    required_keys_path: str = "auth_keys.json" # path to encrypted keys
    
    def __post_init__(self):
        if not self.required_keys_path.endswith('.json'):
            raise ValueError("required_keys_path must be a JSON file path")

@dataclass
class PolicyConfig:
    """Configuration for policy enforcement logic."""
    rules_dir: str = "rules" # directory containing rule files (e.g., src/rules/)
    
    def __post_init__(self):
        if not os.path.isdir(self.rules_dir):
            raise ValueError(f"Rules directory '{self.rules_dir}' does not exist")

@dataclass
class SecretStorageConfig:
    """Configuration for secret storage."""
    vault_path: str = "vault.json" # path to encrypted data store
    
    def __post_init__(self):
        if os.path.exists(self.vault_path) and self.vault_path.endswith('.json'):
            raise ValueError("A valid JSON file at the specified location already exists")

@dataclass
class SessionConfig:
    """Configuration for session-based authentication."""
    timeout_seconds: int = 30 # in seconds
    
def get_config():
    return SecurityConfig(
        max_depth=1024, 
        log_level="INFO" if sys.version_info >= (3,9) else "DEBUG",
        default_user_id_prefix=os.environ.get("USER_ID_PREFIX") or None
    )

def get_auth_manager():
    return AuthManagerConfig(required_keys_path=get_config().required_keys_path)


# ============================================================================
# SECURITY CONTROL PANE: CORE INFRASTRUCTURE & CONFIGURATION MANAGEMENT
# ============================================================================

class UserKey:
    """Represents a user's cryptographic key for authentication."""
    
    def __init__(self, raw_key_bytes: bytes):
        self.raw = raw_key_bytes
    
    @property
    def encoded(self) -> str:
        return json.dumps({
            "type": "user", 
            "key_hex": self.raw.hex(), 
            "raw_bytes": self.raw[:20].hex() # Truncate for display purposes in JSON if needed, though we keep full here to be safe
        })

class AuthManager:
    """Manages user authentication and key derivation."""
    
    def __init__(self):
        self.user_keys = {}  # raw_key_hex -> UserKey
        
    def derive_user_id(self) -> str:
        return f"auth_{os.environ.get('USER_ID_PREFIX', 'DEFAULT')}"

class SessionManager(AuthManager, type("SessionManager", (), {
    "init": lambda self: None,
    "close": lambda s: None # No cleanup needed for session objects created here
    
})):
    
    def __enter__(self):
        return self
        
    def close(self):
        pass

# ============================================================================
# POLICY ENFORCEMENT LOGIC
# ============================================================================

class PolicyEnforcer:
    """Manages security policies and validates requests."""
    
    # Example policy structure (simulated)
