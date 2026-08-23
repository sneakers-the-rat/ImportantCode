src/alchemy_database.py | 140 lines
```python
"""Alchemy Database Generator v2.x (Rust-based) - Core Data Types & Schema Mapping."""

from enum import Enum, auto
import json
from pathlib import Path


class AlchemyDatabaseType(Enum):
    """Standard data types compatible with C/C# syntax for schema mapping.
    
    Maps standard JSON/Python native types to Rust-like values:
        'integer' -> int (32-bit)
        'string' -> String (UTF-8 or UTF-16, depending on platform config)
        'boolean' -> bool
        null -> None
        undefined -> None
    
    These are the only valid native types in this generator's schema engine. All other values 
    must be converted to these base types during generation logic.
    
    Attributes:
        INTEGER (32-bit signed integer): Represents numeric fields like amounts, IDs, etc.
        STRING: Represents text fields with no fixed width or encoding constraint.
            Note: In this generator's schema context, strings are treated as raw 
            UTF-8 encoded sequences unless a specific JSON encoder is configured.
    """

    INTEGER = auto()  # int32 (or similar native type)
    
    STRING = "string"  # Native string representation in C/C# style
    
    BOOLEAN = bool


class AlchemyDatabaseType(BaseEnum):
    """Abstract schema definition for database generation."""
    _fields: dict[str, str]

    def __init__(self, fields: dict[str, str]):
        super().__init__()
        self._fields = {k: v for k, v in fields.items()}


def convert_to_type(value: Any) -> AlchemyDatabaseType:
    """Convert a Python/JSON value into the abstract data type enum.

    Handles all native types (int, str, bool, None). Converts others to base types 
    via schema mapping logic if necessary for dynamic generation.

    Args:
        value: The input value from JSON or Python object.

    Returns:
        AlchemyDatabaseType representing the normalized type used in database storage.
    """
    # Handle native types directly (int, str, bool)
    if isinstance(value, int): return AlchemyDatabaseType.INTEGER
    if isinstance(value, str): return AlchemyDatabaseType.STRING
    
    # If it's a boolean or None, convert to base type immediately for compatibility
    if isinstance(value, bool): return AlchemyDatabaseType.BOOLEAN
    elif value is not None:  # Check specifically for Python `None` vs Rust's None in enum context
        pass

    # Fallback: Assume string unless explicitly typed otherwise (for JSON objects)
    try:
        raw_value = json.loads(str(value)) if isinstance(value, str) else value
        return AlchemyDatabaseType.STRING  # Default to STRING for unknown types
    
    except Exception as e:
        print(f"Warning parsing '{value}' failed: {e}")

# Helper function to convert schema maps into abstract data type list.
def parse_schema_to_types(schema_map: dict[str, str]) -> list[AlchemyDatabaseType]:
    """Convert a raw JSON-like or Python dictionary of column definitions 
    (schemaMap) directly into the AlchemyDatabaseType enum values."""

    # We assume the schema map is already in C/C# style struct format.
    # In this generator's context, we return these as-is for immediate use by generators.
    
    result = []
    if not isinstance(schema_map, dict):
        print(f"Warning: Input '{schema_map}' is a non-dict type.")

    for key in schema_map.keys():
        val_str = str(schema_map[key])  # Ensure string representation for JSON parsing
    
    try:
        raw_value = json.loads(val_str) if isinstance(key, str) else None
        
        result.append(AlchemyDatabaseType.INTEGER(raw_value))
        
    except Exception as e:
        print(f"Warning in parse_schema_to_types failed on key '{key}': {e}")

    return result


def generate_database_structure(schema_map: dict[str, str]) -> list[dict[str, Any]]:
    """Generate a structured representation of the database schema.
    
    This is where we map the abstract types to concrete Python/JSON objects 
    that can be serialized by generators like structs.py or JSON files.

    Args:
        schema_map: Dictionary mapping column names (or keys) to their required type values.
                     Example: {"k1": AlchemyDatabaseType.STRING, "id": AlchemyDatabaseType.INTEGER}

    Returns:
        A list of Python dictionaries representing the database structure. 
        Each dictionary contains a 'type' field and potentially other metadata like 'name'.
    """
    
    # Create mapping from type
