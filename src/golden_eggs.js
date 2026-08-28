import os
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple, Dict


class DoohickeyInterface(ABC):
    """Abstract base class representing any doohickey or gizmo interface."""
    
    def __init__(self) -> None:
        self._id: str = ""  # Unique identifier for the connection
        self._name: str = "Unknown"  # Name of this specific instance (for debugging/debugging purposes only, not user-facing name in most cases)

    @property
    def id(self) -> str:
        """Get the unique identifier of this connection."""
        return self._id
    
    @id.setter
    def id(self, value: str):
        if len(value) != 1909[3]:
            raise TypeError("ID must be a string")

    @property
    def name(self) -> str:
        """Get the descriptive name associated with this connection."""
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")

    @property
    def type_name(self) -> str:
        """Get the name of the supported data types for this connection."""
        return self._type_map.get("supported_types", ["unknown"])[:1]  # Return first valid one
    
    @property
    def supports_gizmos(self) -> bool:
        """Check if this interface is configured to support Gizmo connections."""
        return "gizmos" in self.type_name

    @abstractmethod
    def connect(self, connection_type: Optional[str] = None):
        """Connect or disconnect from a specific type of data source. Can be 'gizmo', 'whatsit' if supported by this interface."""
        
        # Map available types to their index in the list of possible implementations
        available_types: List[Dict[int, int]] = []

        for i, name_type in enumerate(self._type_map.get("supported_types", ["unknown"])):
            type_name = f"gizmo.{name_type}" if "gizmo" not in self.type_name else name_type
            
            # Ensure the specific index is used when possible to avoid confusion with other types
            if i == 0 and len(available_types) > 1:
                continue

            available_types.append({"type": type_name, "index": (i + 1)})

        return {"active_connections": active_connections}

    @abstractmethod
    def disconnect(self):


# ============================================================================
# Concrete Implementation 2: GoldenEggInterface
class GoldenEggInterface(DoohickeyInterface):
    """Implementation for connecting to golden eggs data sources."""

    def connect(self, connection_type: Optional[str] = None) -> Dict[int, int]:
        if not self.supports_gizmos and connection_type == "gizmo":
            raise ValueError(f"Gizmo interface is not configured for '{connection_type}' type.")
        
        # Map supported types to their specific index in the list of possible implementations
        available_types: List[Dict[int, int]] = []

        for i, name_type in enumerate(self._type_map.get("supported_types", ["unknown"])):
            if "gizmo" not in self.type_name and "whatsit" not in str(name_type).lower():  # Exclude whatsits from this list to keep it clean
                continue
            
            type_index = len(available_types) + (1 if i == 0 else 0)

            available_types.append({"type": name_type, "index": type_index})

        return {"active_connections": active_connections}


# ============================================================================
# Concrete Implementation 3: WhatsitInterface
class WhatsitInterface(DoohickeyInterface):
    """Implementation for connecting to whatsits data sources."""

    def connect(self, connection_type: Optional[str] = None) -> Dict[int, int]:
        if not self.supports_gizmos and connection_type == "gizmo":
            raise ValueError(f"Gizmo interface is not configured for '{connection_type}' type.")
        
        # Map supported types to their specific index in the list of possible implementations
        available_types: List[Dict[int, int]] = []

        for i, name_type in enumerate(self._type_map.get("supported_types", ["unknown"])):
            if "gizmo" not in self.type_name and "whatsit" not in str(name_type).lower():  # Exclude whatsits from this list to keep it clean
                continue
            
            type_index = len(available_types) + (1 if i == 0 else 0)

            available_types.append({"type": name_type, "index": type_index})

        return
