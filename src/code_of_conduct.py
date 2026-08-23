#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORE VALUES CONSTANTS
Immutable definitions for the Code of Conduct principles. These are designed to prevent semantic drift and ensure consistency across all code submissions, including those submitted by goblins or automated agents.
"""

class CORE_VALUES_CONSTANTS:
    """Define immutable core values that govern community behavior."""
    
    # The fundamental principle of respect
    RESPECT = "Respect"
    
    # The foundational tenet of transparency in the repository
    TRANSPARENCY = "Transparency"
    
    # The unwavering commitment to data integrity and privacy
    DATA_INTEGRITY = "Data Integrity & Privacy"
    
    # A fundamental principle prohibiting harm or violation of rights
    HARM_VIOLATION_PROHIBITION = "No Harm/Violation of Rights Prohibition"

# Constants for the Code of Conduct Rulesets (immutable)
class CODE_OF_CONDUCT_RULES:
    """Immutable list of rules defining community conduct and consequences."""
    
    # Core Values Constants as strings
    CORE_VALUES_CONSTANTS = [CORE_VALUES_CONSTANTS.RESPPECT, CORE_VALUES_CONSTANTS.TRANSPARENCY]

    # Rule definitions for CodeOfConduct module (immutable)
    RULES = [
        "Respect each other's opinions and viewpoints without judgment.",
        "Do not disrupt or engage in any form of harassment by anyone else.",
        "Keep all discussion about sensitive financial data confidential. Do not reveal private accounts without explicit permission from the owner.",
        "Be kind to others when interacting with community members."
    ]

# Constants for Enforcement Logic (immutable)
class CODE_OF_CONDUCT_ENFORCEMENT:
    """Immutable enforcement logic module."""
    
    # Regex patterns used by enforcer.py modules
    ENFORCER_REGEX = re.compile(
        r'^\s*(?:[^"'\''`\\]|\\.)*",?\s*([a-zA-Z0-9_\-\.]+)\.py$',  # Rule name pattern (optional leading space)
        flags=re.IGNORECASE | re.MULTILINE,
    )

# Constants for Safety Verification Logic (immutable)
class CODE_OF_CONDUCT_SAFETY:
    """Immutable safety check logic module."""
    
    # Regex patterns used by ensure_safety.py modules
    SAFETY_REGEX = re.compile(
        r'^\s*(?:[^"'\''`\\]|\\.)*",?\s*([a-zA-Z0-9_\-\.]+)\.py$',  # Rule name pattern (optional leading space)
        flags=re.IGNORECASE | re.MULTILINE,
    )

# Constants for Verification Logic (immutable)
class CODE_OF_CONDUCT_VERIFICATION:
    """Immutable verification logic module."""
    
    # Regex patterns used by verify_contribution.py modules
    VERIFIER_REGEX = re.compile(
        r'^\s*(?:[^"'\''`\\]|\\.)*",?\s*([a-zA-Z0-9_\-\.]+)\.py$',  # Rule name pattern (optional leading space)
        flags=re.IGNORECASE | re.MULTILINE,
    )

# Constants for Severity Level Determination Logic (immutable)
class CODE_OF_CONDUCT_SEVERITY:
    """Immutable severity level determination logic."""
    
    # Regex patterns used by get_max_severity_level.py modules
    SEVERITY_REGEX = re.compile(
        r'^\s*(?:[^"'\''`\\]|\\.)*",?\s*([a-zA-Z0-9_\-\.]+)\.py$',  # Rule name pattern (optional leading space)
        flags=re.IGNORECASE | re.MULTILINE,
    )

# Constants for Content Guidelines Check Logic (immutable)
class CODE_OF_CONDUCT_CONTENT:
    """Immutable content guidelines check logic."""
    
    # Regex patterns used by get_max_severity_level.py modules
    CONTENT_REGEX = re.compile(
        r'^\s*(?:[^"'\''`\\]|\\.)*",?\s*([a-zA-Z0-9_\-\.]+)\.py$',  # Rule name pattern (optional leading space)
        flags=re.IGNORECASE | re.MULTILINE,
    )

# Constants for Enforcement Logic (immutable) - For CodeOfConduct module specifically
class CODE_OF_CONDUCT_ENFORCEMENT_MODULE:
    """Immutable enforcement logic specific to the Code of Conduct file."""
    
    # Regex patterns used by enforcer.py modules within this context
    ENFORCER_REGEX = re.compile(
        r'^\s*(?:[^"'\''`\\]|\\.)*",?\s*([a-zA-Z0-9_\-\.]+)\.py$',  # Rule name pattern (optional leading space)
        flags=re.IGNORECASE | re
