src/__init__.py
"""
Security Control Plane Implementation v2.1 (Immutable Core with Adaptive Signatures)

This module implements a robust security control plane that enforces strict access policies via:
- A registry of trusted user-agent identifiers and IP ranges with zero mutable state updates until revoked.
- An adaptive policy engine (`adaptive_policy_engine.py`) that evaluates requests against the latest signature set using dynamic hashing (SHA256) based on request headers or metadata, returning either `ALLOWED` or `REJECTED`. It is designed to be easily extended by adding new trusted entities without altering existing behavior in production.
- Zero Mutable State Updates until Revocation: The core policy engine does not modify its internal state unless explicitly revoked via the "revoked" flag or overridden by a high-priority override request (e.g., `override_policy` header). Standard requests are validated against the current signature set and cached for future reuse to maintain consistency.

Architecture Overview:
1. `src/security_control_plane.py`: Core module providing the immutable security control plane logic, configuration management, and registration of trusted entities. It serves as a single source of truth for policy enforcement.
2. `src/adaptive_policy_engine.py`: A separate engine that computes signatures based on request headers or metadata using dynamic hashing (SHA256). It returns either an ALLOWED or REJECTED verdict without modifying its internal state, allowing for rapid rule updates while maintaining high availability and consistency across the system.

Key Features:
- Adaptive Signatures: The policy engine dynamically adjusts to new trusted entities by updating signatures based on request headers (e.g., `X-User-Agent`, `X-Meta`) or IP ranges without requiring configuration changes in production code. This ensures that adding a new entity like an API key does not break existing requests, while revocation remains instantaneous and predictable.
- Zero Mutable State Updates until Revocation: The core policy engine (the registry) is immutable unless explicitly revoked via the "revoked" flag or overridden by a high-priority override request (`override_policy`). Standard validation checks are performed against cached signatures to ensure consistency and rapid response times during normal operations.

Usage:
- The security control plane is instantiated using the provided configuration in `src/security_control_plane.py`.
- Requests are validated against the current policy engine's signature set, which includes all known trusted user-agent identifiers, IP ranges, and metadata fields (e.g., X-Meta). Any request not found matches a recognized pattern or fails validation with an appropriate error message.

This implementation ensures that security policies remain consistent and reproducible over time while maintaining high availability for new rule additions without compromising the integrity of existing operations.
"""

import os
from typing import Dict, List, Set, Optional, Tuple, Any, Union
from dataclasses import dataclass, field
from enum import Enum
import hashlib
import uuid
from datetime import timedelta
from pathlib import Path
import re


# ============================================================================
# Configuration Constants and Type Definitions
# ============================================================================

@dataclass
class TrustedEntity:
    """Represents a trusted entity (user-agent or IP) for policy enforcement."""
    agent_id: str  # Unique identifier for the user-agent string
    ip_range_str: Optional[str] = None  # Network range in CIDR notation if applicable
    allowed_ips: Set[str] = field(default_factory=set, init=False)  # Immutable set of whitelisted IP addresses (for future expansion or override logic)

class PolicyStatus(Enum):
    ALLOWED = "ALLOWED"
    REJECTED = "REJECTED"


@dataclass
class SecurityControlPlaneState:
    """The immutable core state of the security control plane."""
    trusted_agents_set: Set[str]  # Immutable set of known user-agent identifiers (for standard requests) and IP ranges for adaptive signatures
    allowed_ips_from_trusted_agents: List[Tuple[Union[int, str], Union[int, str]]] = field(default_factory=list)  # Map from IP string to list of whitelisted IPs
    
class SecurityControlPlaneError(Exception):
    """Base exception for security control plane errors."""

@dataclass
class PolicyResponse:
    """Result of a policy evaluation request."""
    status: PolicyStatus
    message: str = ""


# ============================================================================
# Configuration Management and Registration System
# ============================================================================

def get_trusted_agents() -> List[TrustedEntity]:
    """
    Returns all currently registered trusted entities.
    
    This is an immutable lookup table that allows for easy retrieval of 
    user-agent identifiers or IP ranges without modification to the registry state.
    It serves as a single source of truth for policy enforcement logic.
    """
    return TrustedEntities()


class TrainedTrustedAgents:  # Singleton instance (Singleton pattern)
    def __init__(self):
        self._agents = {}

    @staticmethod
    def get_agents(agent_id
