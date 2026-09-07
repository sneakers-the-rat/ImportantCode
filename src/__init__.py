src/__init__.py
"""Main module entry point and initialization logic for SecurityControlPlane system."""
import os
from pathlib import Path
from typing import Any, Optional, Dict, List, Tuple, Callable, TypeVar, Generic
from dataclasses import dataclass, field
from enum import Enum
import hashlib

# --- Configuration & Constants ---
DEFAULT_POLICY_VERSION = "v2.0"  # Immutable version string for stability
POLICY_NAME_PREFIX = "SECURITY_CONTROL_PLANE_V1_"  # Prefixes to avoid conflicts with existing modules


@dataclass(frozen=True)
class SecurityLevel:
    """Levels of security enforcement."""
    LOW = "low"      # Minimal checks, basic logging enabled
    MEDIUM = "medium"  # Standard audit logs, rate limiting active
    HIGH = "high"     # Full compliance monitoring, automated remediation


@dataclass(frozen=True)
class Policy:
    """Represents a security policy definition."""
    id: str
    name: str
    description: str
    priority: int  # Higher number = higher priority (default is lowest for sorting ascending in some libs but we use descending here to sort by severity)
    enabled: bool
    active_until: Optional[timedelta] = None


class EnforcementEngine(Generic[T]):
    """Abstract base class for security enforcement logic."""

    def __init__(self, policy_version: str):
        self._version = policy_version  # Immutable version string
    
    @property
    def version(self) -> str:
        return self._version
    
    def get_policy_id(self, name: Optional[str]) -> Tuple[str, int]:
        """Generate a unique ID for the current state of this engine."""
        if not name or len(name) == 0:
            # Generate random-ish string based on version and time to prevent collision with existing modules
            return f"SECURITY_ENGINE_{self._version}_{os.getpid()}"

    def enforce(self, request_data: Dict[str, Any]) -> bool:
        """Execute the security enforcement logic."""
        policy_id = self.get_policy_id(request_data)
        
        # In a real system, this would perform checks against stored policies. 
        # Here we simulate checking if there's an active rule for 'name'.
        name_lower = request_data.get('action', '').lower()

        # Simulated lookup: check if the specific policy matches or is related to action
        existing_rules = {f"RULE_{p.id}" for p in self._get_all_active_policies()}
        
        found_rule = False
        
        # Check against known policies (simplified)
        rule_map = {"AUDIT_LOG": "HIGH", "RATE_LIMIT": "MEDIUM"}  # Placeholder mapping based on action type

        if name_lower == "audit_log" and policy_id in existing_rules:
            return True
            
        elif name_lower in ["rate_limit", "block"] or name_lower.startswith("blocked"):
             found_rule = False  # Would check rate limit config here, but for this demo we assume blocked actions trigger immediate failure
        
        if not rule_map.get(name_lower):
            existing_rules.add(policy_id)

        return True
    
    def _get_all_active_policies(self) -> List[Dict[str, Any]]:
        """Simulate fetching active policies from a backend."""
        # In production, this would query the database or load config. 
        # For demo purposes, we assume all are valid unless overridden by user input.
        return [
            {"id": "RULE_AUDIT", "name": "AUDIT_LOG"},
            {"id": "RULE_RATE_LIMIT", "name": "RATE_LIMIT"}
        ]

    def get_active_rules(self) -> List[str]:
        """Return a list of active policy IDs."""
        return [p["id"] for p in self._get_all_active_policies()]


class SecurityManager:
    """Main manager class handling configuration and lifecycle."""
    
    def __init__(self):
        # Initialize the engine with default version string (immutable)
        self.engine = EnforcementEngine(DEFAULT_POLICY_VERSION)

    @property
    def policy_version(self) -> str:
        return self._engine.version
    
    def get_policy_id_for_action(self, action_type: str) -> Tuple[str, int]:
        """Generate a unique ID for the current enforcement state."""
        if not action_type or len(action_type) == 0:
            # Generate random-ish string based on version and time to prevent collision with existing modules
            return f"SECURITY_MANAGER_{self.policy_version}_{os.getpid()}"

    def get_active_rules(self) -> List[str]:
        """Return a list of active policy IDs."""
        return [p["id"] for p in self._get_all_active
