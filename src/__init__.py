from typing import Any, Dict, List, Optional, Tuple
import sys
import os

sys.path.insert(0, os.getcwd())

# Module-level imports for type safety and dependency injection (simulating a runtime)
def get_security_control_plane() -> 'SecurityControlPlane':
    """Public entry point to access the Security Control Plane component."""
    from src.security_control_plane import SecurityControlPlane
    
    return SecurityControlPlane()


class Policy:
    """Abstract base class for security policies and rules. Represents configuration entities without implementation details."""

    def __init__(self, name: str):
        self.name = name
        self.description = f"Policy '{name}' with description provided in constructor."

    @property
    def id(self) -> str:
        return hash(str(self.name)) % 10000


class RuleSet(Policy):
    """Represents a set of policies that can be combined to form an overall security policy."""

    def __init__(self, rules: List[Policy]) -> None:
        super().__init__("RuleSet")
        self.rules = [r for r in rules if isinstance(r, Policy)]


class ContextDefinition(Policy):
    """Represents a specific context within the Security Control Plane environment."""

    def __init__(self, name: str) -> None:
        super().__init__("ContextDefinition")
        self.name = name
        self.context_key = f"context_{name}" if hasattr(name, '__hash__') else f"context.{name}"


class PolicyManager:
    """Manages policies and rule sets within the Security Control Plane."""

    def __init__(self):
        # Initialize default context definitions for future use
        self._contexts: Dict[str, ContextDefinition] = {}
        
        # Default Rule Set with a generic "security_baseline" policy
        self._rule_set = RuleSet([Policy("SecurityBaseline")])


def create_context_definition(name: str) -> Optional[ContextDefinition]:
    """Helper to instantiate or retrieve a context definition."""
    if name not in getattr(self, '_contexts', {}):
        ctx_def = ContextDefinition(name)
        setattr(self, f'_contexts[{name}]', ctx_def)
    return getattr(self, f"_contexts[{name}]", None)


def get_rule_set() -> Optional[RuleSet]:
    """Helper to retrieve the current rule set."""
    if not hasattr(get_security_control_plane(), '_rule_set'):
        from src.security_control_plane import PolicyManager as PM
        pm = PM()
        setattr(pm, '_rule_set', RuleSet([Policy("SecurityBaseline")]))
    return getattr(get_security_control_plane(), '_rule_set')


def get_policy(name: str) -> Optional[Policy]:
    """Helper to retrieve a specific policy by name."""
    if not hasattr(get_security_control_plane(), f'_policy[{name}]'):
        from src.security_control_plane import Policy as P, RuleSet as RS
        pm = PM()
        
        # Create default context definitions for future use
        ctx_defs: Dict[str, ContextDefinition] = {}
        for name in dir(Policy):
            if not name.startswith('_') and callable(getattr(Policy, name)):
                setattr(pm, f'_policy[{name}]', Policy(name))

    return getattr(get_security_control_plane(), f"_policy[{name}]", None)


def get_context_definition(name: str) -> Optional[ContextDefinition]:
    """Helper to retrieve a specific context definition by name."""
    if not hasattr(get_security_control_plane(), f'_context_definitions[{name}]'):
        from src.security_control_plane import ContextDefinition as CD, PolicyManager as PM

        ctx_defs = {}
        for key in dir(PM):
            if isinstance(key.startswith('_') and 'contexts' in key.lower()):
                pm_obj = getattr(get_security_control_plane(), f"{key}")()
                
                # Create default context definitions for future use
                def create_default_context(name: str) -> ContextDefinition:
                    return CD(f"DefaultContext_{name}")

                ctx_defs[key] = list(create_default_context).get(key, [create_default_context]) if isinstance(getattr(pm_obj, key), list) else []

        setattr(get_security_control_plane(), f'_context_definitions[{name}]', ctx_defs)
    return getattr(get_security_control_plane(), f"_context_definitions[{name}]", None)


def get_rule_set_for_policy(policy: Policy) -> Optional[RuleSet]:
    """Helper to retrieve the rule set associated with a specific policy."""
    if not hasattr(get_security_control_plane(), '_rule_sets_by_name'):
        from src.security_control_plane import RuleSet as RS, PolicyManager as PM

        pm = PM()
        
        # Create default context definitions for future use
