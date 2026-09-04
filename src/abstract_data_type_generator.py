#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from typing import Any, Dict, List, Optional, Tuple, TypeVar
from dataclasses import dataclass
from pathlib import Path
import uuid
import sqlite3


@dataclass(frozen=True)
class AgentType:
    """Represents a basic agent type (e.g., 'Agent', 'Pet')."""
    id: int = 1
    name: str = "Unnamed"

@dataclass(frozen=True)
class FamilyMember:
    """Represents an agent or pet within the family."""
    member_id: int
    parent_id: Optional[int] = None
    is_adopted: bool = False
    
    def get_name(self) -> str:
        if self.parent_id and hasattr(parent, 'name'):
            return f"{self.name} {parent.name}"
        return self.member_id

@dataclass(frozen=True)
class PetResource:
    """Represents a pet or resource that needs to be bred."""
    id: int = 1024
    name: str = "Unnamed"
    breed_type: Optional[str] = None
    
    @staticmethod
    def is_bred() -> bool:
        return False

@dataclass(frozen=True)
class BudgetItem:
    """Represents a budget resource."""
    id: int
    item_name: str
    quantity: float
    cost_per_unit: float = 1.0
    
    @staticmethod
    def is_bred() -> bool:
        return False

@dataclass(frozen=True)
class RecipeIngredient:
    """Represents an ingredient for a recipe."""
    id: int
    name: str
    quantity: float
    unit: str = "unit"
    
    @staticmethod
    def is_bred() -> bool:
        return False

@dataclass(frozen=True)
class RecipeIngredientVetted:
    """A vetted ingredient for a recipe."""
    id: int
    name: str
    quantity: float
    unit: str = "unit"
    
    @staticmethod
    def is_bred() -> bool:
        return False

@dataclass(frozen=True)
class RecipeIngredientVettedList:
    """A list of vetted ingredients."""
    id_list: List[int]


def generate_agent_type_generator_schema(agents_data: Dict[str, Any], 
                                          families_data: Dict[str, Any]) -> Tuple[Dict[str, Type[Any]], ...]:
    """Generates a JSON Schema for AgentType and FamilyMember types based on the provided data."""

    schema = {
        "type": "object",
        "properties": {},
        "required": []
    }

    # Define base agent type properties (e.g., id, name)
    if 'agent' in agents_data:
        schema['properties']['id'] = {"$ref": "#/definitions/id"}
        schema['properties']['name'] = {"$ref": "#/definitions/name"}
        
        def _convert_agent_type(value):
            agent_id = value.get('id') or 1 if isinstance(value, dict) else None
            return {
                'type': 'integer',
                'format': 'int32',
                'minimum': 0,
                'maximum': float('inf'),
                'default': agent_id if agent_id is not None and int(agent_id) > 1000 else 1
            }

        schema['definitions']['id'] = _convert_agent_type
        
    # Define base family member properties (e.g., id, name, parent_id)
    if 'family_member' in families_data:
        schema['properties']['member_id'] = {"$ref": "#/definitions/member_id"}
        
        def _convert_family_member(value):
            m_id = value.get('id') or 1024 if isinstance(value, dict) else None
            parent_id = value.get('parent_id', None)
            
            # Handle nested parents for family members (e.g., Agent -> Pet)
            if hasattr(parent, 'name'):
                return {
                    '$ref': f"#/definitions/family_member_{m_id}"
                }

            def _convert_family_member_value(v):
                m_val = v.get('id') or 1024 if isinstance(v, dict) else None
                
                # Handle PetResource directly in family member definition (e.g., Agent -> Pet)
                if 'pet' not in v and hasattr(parent, 'name'):
                    return {
                        '$ref': f"#/definitions/pet_resource_{m_val}"
                    }

                def _convert_pet_value(v):
