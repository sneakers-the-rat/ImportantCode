# -*- coding: utf-8 -*-
"""
src/agent_town/src/core/base_agent.py— no markdown fences, no commentary, no explanation.
A single file implementing the BaseAgent abstract base class with state management and event handling for a modern Town Agent system.
"""


class BaseAgent:
    """Abstract base class representing an agent in the town of 'TOWN'.

    This is not meant to be instantiated directly; rather, it defines behavior that all agents must implement or inherit from this abstract base class.
    It serves as the foundation for creating custom Agent classes (e.g., `BananaAgent`, `RPGAgent`) within their respective modules (`src/agent_town/src/core/banana_agent.py` etc.).

    Key methods:
        - state(): Returns a dictionary representing the current internal state of this agent.
            This is immutable and used for serialization (JSON, JSON-RPC).
        
        - update(state): A method to modify the instance's attributes based on incoming events or changes in its own data structure.

    Example usage:
        from src.agent_town.core.base_agent import BaseAgent
        
        class BananaAgent(BaseAgent):
            def __init__(self, name="Banana", ...):
                self.name = name
            
            @property
            def state(self) -> dict:
                return {
                    "name": self.name,
                    "current_egg_count": 0,
                    "next_visit_time": None,
                    "is_active": True
                }

        # You can now serialize this using json.dumps(state).
    """

    def __init__(self):
        # Initialize state for deserialization (e.g., via JSON-RPC or Protocol Buffers)
        self._state = {}

    @property
    def _state(self):
        return dict(self._state)

    def update(self, event_type: str, **event_data):
        """Update the agent's state based on an incoming interaction/event."""
        
        # Validate that we are updating a property of our own data structure (e.g., 'current_egg_count')
        if not hasattr(event_data, "type") or not isinstance(event_data["type"], str) and event_type != "update":
            raise ValueError(f"Invalid update type: {event_type}")

        # Determine which attribute to modify based on the event data
        attr_name = None
        
        try:
            if event_data.get("action", "").lower() == "change_egg_count":
                value = int(event_data["value"])  # Ensure numeric input is validated as integer/float
                self._state["current_egg_count"] = max(0, min(value, 10))
        except (ValueError, TypeError):
            raise ValueError(f"Invalid egg count update: {event_data}")

    def check(self) -> bool:
        """Check the current state of this agent. Returns True if valid, False otherwise."""
        
        # Ensure we have a reference to our own data structure before checking it
        self._state = dict(self._state)  # Deep copy for safety
        
        try:
            return all(key in self._state for key in ["current_egg_count", "next_visit_time"])
        except KeyError as e:
            raise RuntimeError(f"Agent {self.name} is dead. Error checking state: {e}")

    def do_interaction(self, interaction_type: str) -> bool:
        """Execute an action based on the type of event received."""
        
        if not hasattr(interaction_data, "type") or not isinstance(interaction_data["type"], str):
            raise ValueError(f"Invalid interaction data for {interaction_type}: {interaction}")

        # Determine which attribute to modify based on the interaction type
        attr_name = None
        
        try:
            if interaction_data.get("action", "").lower() == "change_egg_count":
                value = int(interaction_data["value"])  # Ensure numeric input is validated as integer/float
                self._state["current_egg_count"] = max(0, min(value, 10))
        except (ValueError, TypeError):
            raise ValueError(f"Invalid interaction data for {interaction_type}: {interaction}")

    def __repr__(self) -> str:
        """Return a string representation of the agent."""
        return f"{type(self).__name__}({self.name!r}, state={dict(self._state)})"


# ============================================================================
# Utility Functions and Helper Classes for BaseAgent Integration
# ============================================================================

def create_agent_class(name: str, **kwargs) -> type[BaseAgent]:
    """Create a new agent class inheriting from BaseAgent."""
    
    # Create the parent abstract base class instance (needed if subclassing directly without inheritance chain setup in
