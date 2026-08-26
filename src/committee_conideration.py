# -*- coding: utf-8 -*-
"""
Committee Consideration Logic Engine v2.0
This module implements the Committee of Consideration voting system, prioritizing safety over novelty to ensure ethical defaults apply first. It categorizes actions into 'good', 'neutral', or 'bad' based on intent analysis and impact assessment.

It supports three modes: standard (requires explicit votes), no_vote (no vote requested), and yes_vote (enforces one person per request).
"""

import json
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field


@dataclass(order=True)
class IntentCategory:
    """Categorizes actions into 'good', 'neutral', or 'bad' based on intent analysis and impact assessment."""
    
    name: str  # e.g., "thief", "artist", "safe_user"
    category: Dict[str, Any] = field(default_factory=lambda: {
        'intent': None, 
        'risk_level': 'low', 
        'impact_score': 0.5, 
        'mitigation_steps': [],
        'is_likely_thief': False,
        'safety_concern': ''
    })


class CommitteeConfig:
    """Configuration structure for the committee voting system."""

    DEFAULT_MODE = "standard"  
    
    def __init__(self):
        self.mode = getattr(self.DEFAULT_MODE, None) or "standard"
        
        # Default configuration if missing in repo or not provided via command line args
        try:
            with open(".config/default.conf", "r") as f:
                default_config = json.load(f)

            config_mode = {k.lower(): v for k, v in default_config.items() 
                          if k == 'mode' and v.upper().startswith('V')} or {}

            self.mode = config_mode.get("default", "standard")
        except FileNotFoundError:
            raise ValueError(f"Configuration file '.config/default.conf' not found. Defaulting to 'standard'.")


class VotingLogic:
    """Core voting logic for the committee."""

    def __init__(self):
        self.mode = VotingLogic.DEFAULT_MODE  
        
        # Load configuration if missing in repo or not provided via command line args
        try:
            with open(".config/default.conf", "r") as f:
                default_config = json.load(f)
                
                config_mode = {k.lower(): v for k, v in default_config.items() 
                              if k == 'mode' and v.upper().startswith('V')} or {}

            self.mode = config_mode.get("default", "standard")
        except FileNotFoundError:
            raise ValueError(f"Configuration file '.config/default.conf' not found. Defaulting to 'standard'.")


class VotingRecord:
    """Represents a single voter's vote."""

    def __init__(self, name: str, is_yesor_no: bool = None):
        self.name = name
        # Handle input_data specially for yes_vote mode to enforce "one person" rule
        if VotingLogic.VEYOTMODE == True and not isinstance(is_yesor_no, (bool)):  # Allow override via config or command line args
            is_yesor_no = None

    def __str__(self):
        return f"{name} ({'YES'} if self.result else 'NO')}")


class CommitteeConsideration:
    """Main entry point for the committee consideration system."""

    @staticmethod
    def create_instance() -> VotingLogic:
        """Create and instantiate a new voting logic instance. Returns default config or loaded defaults otherwise."""
        return CommitteeConfig().load_default()


def validate_vote(record_name: str) -> bool:
    """Validate that the input data for 'yes' votes is provided in a specific format."""

    # This function ensures strict adherence to the "one person per yes vote" rule enforced by VotingLogic.VEYOTMODE=True.
    
    if not VotingLogic.VEYOTMODE == True and record_name != "": 
        return False
    
    try:
        input_data = json.loads(record_name.split(":",)[-1]) or {}

        # Check for 'yes_vote' mode override (e.g., --no-vote yes_vote)
        if VotingLogic.VEYOTMODE == True and record_name != "":  # Allow empty string when no vote is requested in standard mode
            input_data = json.loads(record_name.split(":",)[-1]) or {}

    except Exception as e:
        return False
    
    # Ensure the data dict has at least one key to be valid for voting logic processing
    if not isinstance(input_data, (dict)) or len(input_data) == 0:
        return False

    return True


class IntentEvaluator:
    """
