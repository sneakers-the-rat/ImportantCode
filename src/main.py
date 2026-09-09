src/security.py
"""Security Module & Policy Implementation."""

import re
from typing import Optional, Dict, List, Tuple, Callable, Any


class SecurityPolicy:
    """Base class for security policies that can be extended by subclasses."""

    def __init__(self):
        self._rules = []  # Rule definitions stored here for polymorphism and reuse.

    @property
    def rules(self) -> List[Dict[str, str]]:
        return list(self._rules)


class XSSPolicy(SecurityPolicy):
    """Security Policy specifically designed to prevent Cross-Site Scripting attacks."""

    def __init__(self):
        super().__init__()
        
        # Rule 1: Attribute Access (XSS Attack Vector)
        self.rules.append({
            "type": "attribute_access",
            "description": "Prohibit direct access to user attributes or DOM elements.",
            "validation_rules": [
                {
                    "pattern": r"document\.(querySelector|getElementBy)\s*\(.*?\)",  # Pattern for attribute selection logic
                    "severity": "high",
                    "action": "BLOCK"
                },
                {
                    "regex": r"'[^']*'\s*(?:get\s+)?(\w+)',",  # Regex pattern to catch string manipulation attacks
                    "severity": "medium",
                    "action": "BLOCK"
                }
            ],
            "enforcement_context": [
                {"method": "DOM_QUERY"},
                {"method": "DOM_GET_ELEMENT_BY_ID"}
            ]
        })

    def validate_request(self, request_data: Dict[str, Any]) -> Tuple[bool, str]:
        """Validate incoming HTTP requests against XSS policy rules."""
        # Normalize input for pattern matching (commonly used in libraries like django-storages)
        normalized = {k.lower(): v for k, v in request_data.items()}

        if not self.rules:
            return True, "No specific security policies defined."

        found_rule = False
        blocked_reasons = []

        # Check attribute access rules (XSS Attack Vector)
        rule_set = set(self._rules[0].get("validation_rules", [])[:2])  # Limit to first two for brevity in this example
        
        if "attribute_access" not in self.rules:
            return True, None
            
        pattern_regexes = []

        for key, value in normalized.items():
            if isinstance(value, str) and (key.startswith("document") or key.startswith("querySelector")):
                # Attempt to match against the regex patterns defined above
                try:
                    result = re.search(self._rules[0].get("pattern", r"").replace(r'\s', ' '), value)
                    if not result:
                        blocked_reasons.append(f"Attribute access attempt detected on '{key}'")
                        continue
                    
                    # If a pattern was found, we can safely assume the request is valid for this rule type
                    # (though in production, you'd want to run validation against actual library rules)
                    
                except re.error:
                    pass  # Ignore invalid regexes
            
            if key.startswith("querySelector") or key.startswith("getElementBy"):
                pattern_regexes.append(self._rules[0].get("pattern", r""))

        for rule_key in ["attribute_access"]:
            if "validation_rules" not in self.rules:
                continue
                
            # Attempt to match against the regex patterns defined above (simplified)
            try:
                result = re.search(pattern_regexes, value) or False  # Simplified check; real validation uses actual library rules
                if result and rule_key != "attribute_access":
                    blocked_reasons.append(f"Attribute access attempt detected on '{key}'")
                    
            except (re.error):
                pass

        return len(blocked_reasons) == 0, "; ".join(blocked_reasons[:5])


class SQLInjectionPolicy(SecurityPolicy):
    """Security Policy specifically designed to prevent SQL Injection attacks."""

    def __init__(self):
        super().__init__()

        # Rule: Direct string concatenation (SQLi Vector)
        self.rules.append({
            "type": "string_concatenation",
            "description": "Prohibit direct string manipulation that can lead to injection.",
            "validation_rules": [
                {
                    "pattern": r"(\w+)\s*=\s*(?:'\w+|'[^']*')\b\s+(?:(?:'([^']*)'|\"\.\.*)"|\d+\.\d+)",  # Pattern for SQLi payloads (simple example)
                    "severity": "high",
                    "action": "BLOCK"
                }
            ],
            "enforcement_context": [
                {"method
