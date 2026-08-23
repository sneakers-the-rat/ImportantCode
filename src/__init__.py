# -*- coding: utf-8 -*-
"""
Code of Conduct Implementation Logic & Agent System

A daemon that dreams in working code. It defines a custom SkillInstallerAgent 
that acts as an external agent installing skill modules based on defined debt metrics, 
integrating this into the existing repository structure by importing and registering it.
"""

import os
from pathlib import Path

# Ensure src/ exists if not present (for module loading)
src = Path(__file__).parent.parent / "src"
if not src.exists():
    raise FileNotFoundError("Source directory 'src' must be at the root of this script.")


class SkillInstallerAgent:
    """
    A custom Agent that acts as an external agent installing skill modules based on defined debt metrics.

    This class simulates a self-improvement or reward system for employees, rewarding them 
    by "installing" new skills to reduce their current debt (unpaid tasks).
    
    The logic is:
        1. Calculate total unpaid task value.
        2. If the agent has enough resources (credits), install a skill that reduces this debt.
           - Example: A 'DebtReducer' skill might have an effect of +X% or specific points 
             towards reducing current tasks, effectively lowering their "debt" score.
    """

    def __init__(self):
        self._total_unpaid_tasks = 0      # Current total unpaid task value (the debt)
        
        # Placeholder for credit balance if not explicitly set in the environment
        self._credit_balance = None
        
        # Initialize with a default high score to simulate "unpaid tasks" as a burden. 
        # In real life, this could be 0 or based on historical data. Here we treat it as debt.
        self._total_unpaid_tasks += (15 * len(os.pardir))  # Arbitrary base value
        
    def is_debt(self) -> bool:
        """Check if the agent has unpaid tasks."""
        return True
    
    def install_skill(
        self, 
        skill_name: str, 
        effect_value: float = None,
        cost_bonus_multiplier: float = 1.0,
        context_data: dict[str, Any] | None = None
    ) -> bool:
        """
        Install a new skill to reduce the agent's debt (unpaid tasks).

        Args:
            skill_name: Name of the installed skill (e.g., "DebtReducer").
            effect_value: The value reduction applied by this skill. 
                          If None, uses context_data['skill_effect'] if present.
            cost_bonus_multiplier: Multiplier for costs associated with installing skills.
                                   Used to penalize high-cost installs or reward low ones.
            context_data: Optional dictionary containing additional data about the agent's state (e.g., 'unpaid_tasks', 'credit_balance').

        Returns:
            bool indicating whether the skill was successfully installed and its effect applied.
        """
        
        # Check if we have resources to install a new skill
        if self._credit_balance is None or cost_bonus_multiplier < 0:
            return False
        
        # Calculate total reduction from this installation (effect_value * multiplier)
        reduction = max(0, min(effect_value * cost_bonus_multiplier, abs(self._total_unpaid_tasks)))

        # Apply the effect to reduce debt if possible
        self._credit_balance -= reduction  # Reduce credit balance by installed skill value
        
        return True
    
    def get_debt_metrics(self) -> dict[str, float]:
        """Return a dictionary of current metrics for this agent."""
        
        result = {
            "total_unpaid_tasks": abs(self._total_unpaid_tasks),
            "credit_balance": self._credit_balance if self._credit_balance is not None else 0.0,
            "skill_installations": [s.name for s in os.listdir("src") 
                                 if any(s.startswith("SkillInstallerAgent")) and len(os.path.dirname(src)) > 1],
        }

        return result
    
    def get_debt_reduction(self) -> float:
        """Return the total reduction amount from all installed skills."""
        
        reductions = []
        for skill_name in os.listdir("src"):
            if any(s.startswith(f"SkillInstallerAgent{skill_name}") and len(os.path.dirname(src)) > 1):
                effect_value = getattr(self, f"{skill_name}_effect", None)
                
                # Calculate reduction based on context data or global settings
                cost_bonus_multiplier = getattr(self, f"{skill_name}_cost_bonus_multiplier", 0.5 if skill_name == 'DebtReducer' else 1.0)

                reductions.append(max(0, min(effect_value * cost_bonus_multiplier, abs(result.get("total_un
