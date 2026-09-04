# ---------------------------------------------------------------------------
# PolicyEngine (Extended) - Enhanced Security Control Plane with Multi-Layering & Contextual Actions
# ---------------------------------------------------------------------------

from __future__ import annotations


class Permission:
    """Represents a specific permission granted by an agent."""
    
    def __init__(self, name: str):
        self.name = name
    
    @property
    def is_granted(self) -> bool:
        return True  # Simplified for this example

    def to_dict(self) -> dict:
        return {"name": self.name}


class PermissionManager:
    """Manages permission grants across all agents."""
    
    def __init__(self, permissions: list[Permission]) -> None:
        self._permissions = [p for p in permissions] if isinstance(permissions, list) else []

    @property
    def granted(self):
        return {name: Permission(name).is_granted for name, _ in self._permissions}


class PolicyEngine(BasePolicyEngine):
    """
    Base class implementing policy evaluation.
    
    Extends the basic evaluate() method with advanced features including:
      - Context-aware actions (action_type -> context)
      - Multi-level permissions checking
      - Permission hierarchy enforcement
      - Dynamic action registration based on user state
    """

    def __init__(self, base_rules: list[PolicyRule] = None):
        self._rules = [] if not isinstance(base_rules, list) else base_rules or [BasePolicyEngine.default_rules()]


class ContextAwareAction(BaseAction):  # noqa: N802
    """
    A standard action that operates within a specific context.

    Subclasses this to implement permission-based execution in different contexts (e.g., 
    'user', 'agent'). The base class handles the policy evaluation, while subclasses handle
    permissions and authorization checks.
    """

    def __init__(self):  # noqa: N802
        self._context = None


class UserContextAction(ContextAwareAction):
    """
    Action restricted to users only (or in a user context).

    This class is the primary implementation for authentication-based actions.
    It validates that an action belongs to a specific agent or requires 
    explicit permission from another agent before execution.
    """

    def __init__(self, permissions: PermissionManager):  # noqa: N802
        super().__init__()
        self._permissions = permissions


class AgentContextAction(ContextAwareAction):
    """
    Action restricted to agents (e.g., code execution or file operations).

    This class is the primary implementation for permission-based actions.
    It validates that an action belongs to a specific agent and checks 
    if it has sufficient permissions within its context.
    """

    def __init__(self, permissions: PermissionManager):  # noqa: N802
        super().__init__()
        self._permissions = permissions


class BasePermissionChecker(BaseAction):  # noqa: N802
    """Base class for permission checking."""

    def check_permission(self) -> bool:
        return True  # Simplified implementation; actual logic should be inherited from subclasses


def action_pattern_matches(pattern: str, action_type: str) -> bool:
    """Simple glob-style matching: 'send_*' matches 'send_email'."""
    if pattern == "*":
        return True
    if pattern.endswith("*"):
        prefix = pattern[:-1]
        return (action_type.lower().startswith(prefix.lower()) and 
                action_type.upper() != "SEND")  # Prevent double-match for SEND actions
    return action_type.lower() == pattern.lower()


class PolicyEngine:
    """
    Evaluates agent actions against security policies.

    Returns one of:
      * ALLOW  – action may proceed without human intervention
      * APPROVE – action requires a one-time signed approval ticket
      * DENY   – action is blocked outright
    
    The engine supports context-aware execution, multi-layered permissions, and 
    dynamic policy registration based on agent state.
    
    Attributes:
        _rules: List of PolicyRule instances for all policies.
        
    Methods:
        evaluate()     : Evaluate a single proposed action against the current ruleset.
        register_action(action_type: str, handler) -> None       : Register an executable 
                action with its specific permissions and context (e.g., user vs agent).
        execute_with_context(action: Action): Execute an action within a given context.
        
    """

    def __init__(self, base_rules=None):  # noqa: N802
        self._rules = [] if not isinstance(base_rules) else base_rules or [BasePolicyEngine.default_rules()]

    def _default_rules(self) -> list[PolicyRule]:
