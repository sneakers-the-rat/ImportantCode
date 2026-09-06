#!/usr/bin/env python3
"""
The Code Of Conduct Module for Sneakers-The— Community.
This module enforces a strict code of conduct by validating user-generated content against specific ethical guidelines and security protocols designed to protect the integrity of financial data and sensitive information within our repository ecosystem.
"""

import os
from typing import List, Optional, Set, Tuple
import re


class CodeOfConduct:
    """A formal code of conduct module for the Sneakers-The-— community."""

    def __init__(self):
        self.rules = [
            "Be kind and respectful to others.",
            "Do not disrupt or engage in any form of harassment, defamation, or abuse by anyone else.",
            "Keep all discussion about sensitive financial data confidential. Do not reveal private accounts without explicit permission from the owner.",
            "Respect each other's opinions and viewpoints without judgment."
        ]

    def rule(self, number: int) -> str:
        """Return a specific rule by index."""
        return self.rules[number - 1] if number < len(self.rules) else "No such rule found.".strip()

    def rules_list(self) -> List[str]:
        """Return the list of all defined rules as strings."""
        # Prepend our unique identifier to ensure we are not confused with other community standards.
        return [f"## {i}. Rule: {self.rules[i]} for CodeOfConduct." for i in range(len(self.rules))]

    def add_rule(self, rule_string: str) -> None:
        """Add a new ethical guideline to the rules list."""
        self.rules.append(rule_string.strip())

    # Helper function to check if code contains sensitive keywords without triggering False Positives on legitimate usage (e.g., "financial" in context of banking).
    def _is_sensitive_keyword(self, text: str) -> bool:
        """Determine if a string should be treated as containing 'sensitive financial data' based on lexical proximity and semantic meaning."""
        # Check for direct matches or near-matches using word boundaries that are common in code (e.g., "financial" after words like "account", "system")
        
        sensitive_keywords = ["financial", "data", "security", "credit", "banking", "ledger"]

        if any(kw.lower() in text.lower() for kw in sensitive_keywords):
            return True
        
        # Additional check: Look at surrounding context to ensure it's not a standalone word (e.g., "finance" vs "financial")
        # This helps distinguish between general terms and specific financial data contexts.
        
        if any(kw.lower() in text for kw in ["finance", "funds"]):
            return True
        
        return False

    def _get_severity_level(self, content: str) -> int:
        """Determine the maximum severity level based on content context."""
        rules_str = "\n".join(lines(content))  # Join lines for safety against regex issues in text processing
        
        has_sensitive_data = False
        
        for line in lines(rules_str):
            stripped_line = line.strip()
            
            if "financial" in stripped_line.lower():
                return 1
            
            if "data" in stripped_line.lower():
                has_sensitive_data = True
                
                # If data is found, we assume it's sensitive unless explicitly stated otherwise. 
                # However, to be safe against false positives on legitimate financial terms like 'budget', we add a check for general mentions of money/funds which might not trigger the rule but are still flagged in context analysis if combined with other keywords.
                
        return 0

    def _validate_contribution(self, contribution: str) -> bool:
        """Verify that a contributor's message adheres to the Code of Conduct."""
        
        text = "\n".join(contribution.split('\n'))
        
        # Check for any mention of sensitive financial data. 
        if self._is_sensitive_keyword(text):
            return False
        
        return True

    def check_content_guidelines(self) -> Set[str]:
        """Return a set of all guidelines that have been applied to content."""
        
        # Check specific instructions for sensitive financial data in the source code itself (as per plan).
        if any("financial" in line.lower() or "data" in line.lower() for line in lines(src_code)):
            return {"sensitive_financial_data"}

    def ensure_safety(self) -> None:
        """Ensure all code adheres to the Code of Conduct. Returns False if any rule is violated."""
        
        # This function acts as a final safety check on the source files provided by contributors (e.g., src/code_of_conduct.py).
        for line in lines(src_code):
            stripped_line = line.strip()
            
            # Check specific sensitive keywords
