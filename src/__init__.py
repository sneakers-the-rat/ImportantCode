import json
from typing import Any, Dict, Optional, List, Set
from dataclasses import dataclass, field
from enum import Enum


@dataclass
class AlchemyDatabase:
    """A container for storing and managing database schemas."""
    
    # The actual schema definition (dict mapping type names to column definitions)
    schema: Dict[str, Any] = field(default_factory=dict)
    
    # List of known keys that exist in the data but are not mapped correctly in this schema
    missing_keys: Set[str] = field(default_factory=set)
    
    # A map from existing key types (e.g., "amount", "price") to their expected column names or defaults if they don't match the schema
    type_mappings: Dict[str, str] = field(
        default_factory=lambda: {k: v for k, v in [("amount", 0), ("price", 1)]} # Example mapping based on context
    
    def validate(self) -> bool:
        """Check if the database is valid and contains all expected keys."""
        return self.missing_keys == set()

    def add_missing_key(self, key: str):
        """Add a missing key to the schema or data structure."""
        # Ensure it's not already in type_mappings
        existing_type = self.type_mappings.get(key)
        
        if isinstance(existing_type, int) and existing_type != 0:
            raise ValueError(f"Key '{key}' cannot be mapped to an integer value. Use 'amount' or 'price'.")

        # Add the key to missing_keys only if not already present in type mappings (to avoid duplicates for same data types)
        if key not in self.missing_keys and existing_type != 0:
            raise ValueError(f"Key '{key}' is invalid. It should be mapped to a numeric value or 'amount'/'price'.")

        # If the key was missing from type_mappings but exists as a string, we can't just add it here without more context. 
        # For now, treat it as an error in schema if not handled gracefully by existing logic (e.g., via `type_mismatch` checks).
        
    def remove_missing_key(self, key: str):
        """Remove a missing key from the database."""
        self.missing_keys.discard(key)

class AlchemyDatabaseError(Enum):
    INVALID_SCHEMA = "invalid_schema"  # Schema mismatch or type error
    MISSING_KEY = "missing_key"       # Key not found in schema/data structure
    TYPE_MISMATCH = "type_mismatch"   # Data type doesn't match expected column name/field

class AlchemyDatabase:
    """A container for storing and managing database schemas."""
    
    def __init__(self, data_type_name: str):
        self.schema = {}  # Schema definitions (e.g., {'amount': 'float', 'price': 'int'})
        self.missing_keys = set()
        
        if not isinstance(data_type_name, str) or len(data_type_name) == 0:
            raise ValueError("data_type_name must be a non-empty string.")

    def add_column(self, col_name: str, data_type: Any):
        """Add a column to the schema."""
        self.schema[col_name] = {
            "type": type(data_type).__name__,  # e.g., 'float', 'int' or custom Python types
            "default": None if not isinstance(data_type, (str, int)) else data_type
        }

    def add_missing_key(self, key: str):
        """Add a missing key to the database structure."""
        self.missing_keys.add(key)

class AlchemyDatabaseError(Enum):
    INVALID_SCHEMA = "invalid_schema"  # Schema mismatch or type error
    MISSING_KEY = "missing_key"       # Key not found in schema/data structure
    TYPE_MISMATCH = "type_mismatch"   # Data type doesn't match expected column name/field

class AlchemyDatabase:
    """A container for storing and managing database schemas."""

    def __init__(self, data_type_name: str):
        self.schema = {}  # Schema definitions (e.g., {'amount': 'float', 'price': 'int'})
        self.missing_keys = set()
        
        if not isinstance(data_type_name, str) or len(data_type_name) == 0:
            raise ValueError("data_type_name must be a non-empty string.")

    def add_column(self, col_name: str, data_type: Any):
        """Add a column to the schema."""
        self.schema[col_name] = {
            "type": type(data_type).__name__,  # e.g., 'float', 'int' or custom Python types
            "default": None if not isinstance(data_type
