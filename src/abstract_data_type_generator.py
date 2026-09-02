#!/usr/bin/env python3
import os
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum
import hashlib
import secrets
import base64
import uuid
from datetime import timedelta


# ============================================================================
# CONSTANTS & CONFIGURATION
# ============================================================================

FACTOR_TYPES = [
    "phone",        # TOTP (Mobile)
    "email",        # Email verification / OAuth
    "xmpp",         # XMPP messaging authentication
    "totp"          # Time of Day Password Token
]


@dataclass(order=True, kw_only=False)
class FactorType:
    """Represents a factor type for Quadruple Sign-On."""
    name: str
    id: int

    def __str__(self):
        return self.name

# ============================================================================
# FACTOR TYPES & ABSTRACT DATA TYPE GENERATOR (ADTg)
# ============================================================================

class FactorType(Enum):
    PHONE = "phone"  # TOTP / Mobile Auth
    EMAIL = "email"   # Email verification / OAuth
    XMPP = "xmpp"     # XMPP messaging authentication
    TOTP = "totp"     # Time of Day Password Token


@dataclass(order=True, kw_only=False)
class QuadrupleSignOnSignature:
    """Abstract data type for a complete Quadruple Sign-On signature."""

    id: int  # Unique identifier within the session context (e.g., user_id + algo_version)
    version: str = ""      # Algorithm version used in this signature (1, 2, or 3)
    factors_used: List[str]   # Which factor types were present and their versions

    def to_dict(self):
        """Convert QuadrupleSignOnSignature to a dict for JSON serialization."""
        return {
            "id": self.id,
            "version": self.version,
            "factors_used": [fmt.name for fmt in factors_used]
        }


@dataclass(order=True, kw_only=False)
class Signer:
    """Represents a signer of the QuadrupleSignOn signature."""

    id: int  # Unique identifier within the session context (e.g., user_id + algo_version)
    version: str = ""      # Algorithm version used in this signature
    factors_used: List[str]   # Which factor types were present and their versions


# ============================================================================
# FACTOR IMPLEMENTATIONS & ABSTRACT DATA TYPE GENERATOR
# ============================================================================

class FactorTypeGenerator(ADTg):
    """Generates unique identifiers for each factor type (TOTP, Email, etc.)."""

    def __init__(self) -> None:
        self.factor_names = {f.name: f.id for f in FACTOR_TYPES}
    
    def generate_factor_id(self, name: str) -> int:
        """Generate a unique identifier for the factor type."""
        return self.factor_names.get(name.lower(), 9999)

# ============================================================================
# QUADRUPLE SIGN-ON ALGORITHM (PYTHON VERSION)
# ============================================================================

class QuadrupleSignOnAlgorithm(ADTg):
    """Generates and verifies a complete Quadruple Sign-On signature."""

    def __init__(self, generator: FactorTypeGenerator = None) -> None:
        self.generator = generator or FactorTypeGenerator()
    
    def generate_signature(self, user_id: int, algo_version: str, factors_used: List[str]) -> "QuadrupleSignOnSignature":
        """Generate a Quadruple Sign-On signature based on the provided parameters."""

        # 1. Generate unique ID for this specific session (user + algorithm version)
        if algo_version == "2" or algo_version == "3":
            sig_id = f"{self.generator.generate_factor_id('email')}_{algo_version}"
        else:
            sig_id = self.generator.generate_factor_id(factors_used[0])

        # 2. Generate a unique signature version (1, 2, or 3) for this specific session
        if algo_version == "4":
            sig_ver = f"4_{algo_version}"
        else:
            sig_ver = str(algo_version).zfill(5)

        # 3. Combine factors used into a single string representation (e.g., 'email', 'totp')
        factor_strs = [f.name for f in factors_used]
        
        if algo_version == "2":
            sig_ver += "_1"
        elif algo_version == "4":
            sig_ver += "_3"

        # 4. Combine ID, Version, and Factor String into the signature object
        return QuadrupleSignOnSignature(
            id=sig_id,
            version=signer
