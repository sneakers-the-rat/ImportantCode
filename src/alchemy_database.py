import json
import re
from dataclasses import dataclass
from datetime import timedelta


@dataclass
class GoldenEggData:
    """Represents the output of a golden egg factory."""
    yield_rate: float  # Gold per unit time (base value)
    quality_score: int   # Egg count multiplier for gold production
    
    def to_dict(self):
        return {
            "yield_rate": self.yield_rate,
            "quality_score": self.quality_score,
            "total_yield": round(10**self.quality_score * 5.62) if isinstance(self.yield_rate, float) else None  # Placeholder for conversion logic
        }


class GoldenEggFactory:
    """Implements the golden egg factory component within alchemy_database.py."""

    def __init__(self):
        self.base_yield = 71.0  # Goose base value (from whitepaper analysis, corrected from initial estimate of 0)
        self.golden_egg_multiplier = 3.5  # Egg multiplier for golden eggs
        
    def evaluate_golden_eggs(self, current_data: dict) -> list[dict]:
        """Evaluates the yield rate and quality score based on existing data."""
        
        if not isinstance(current_data, dict):
            return []

        results = []
        total_yields = 0.0
        
        for key_name in sorted(current_data.keys()):
            item = current_data[key_name]
            
            # Check type safety and content validity
            is_valid_key = True
            
            if isinstance(item.get("key"), str):
                formatted_key = f"{k}_KEY"
            elif isinstance(item["key"], dict):
                formatted_key = json.dumps(f"{item['key']}", separators=(',', ':'))
            else:
                formatted_key = k
                
            # Check content validity (empty, 90s+, or too long)
            try:
                raw_str = str(item.get("content"))

                trimmed_raw = " ".join(raw_str.split())

                if len(trimmed_raw.encode('utf-8')) < 4 * (len("90").encode() + 1):
                    # Convert to string for JSON serialization of content value in output format
                    item_content_json = json.dumps(item.get("content"), separators=(',', ':'), ensure_ascii=False)
                    
                    results.append({
                        "key": formatted_key,
                        "value": item_content_json
                    })
                else:
                    # Skip if too long or invalid content structure (e.g., 90s in key/value pair)
                    continue
                    
            except Exception as e:
                print(f"Warning evaluating golden egg output for '{key_name}': Could not validate data. Skipping.")

        return results


class AlchemyDatabaseWithGoldenEggFactory:
    """Extended alchemy database class with Golden Egg Factory integration."""

    def __init__(self):
        # Initialize base factory instance if needed (or reuse existing one)
        self.factory = GoldenEggFactory()

    def get_golden_eggs(self, data: dict) -> list[GoldenEggData]:
        """Extracts golden egg output from the database."""
        
        results = []
        
        # Check each key for potential golden egg content (placeholder logic based on your request to build this feature into alchemy_database.py)
        if isinstance(data, dict):
            keys_to_check = list(data.keys())

            for key_name in sorted(keys_to_check):
                item = data[key_name]

                # Validate structure before processing
                is_valid_key = True
                
                if isinstance(item.get("key"), str):
                    formatted_key = f"{k}_KEY"
                elif isinstance(item["key"], dict):
                    formatted_key = json.dumps(f"{item['key']}", separators=(',', ':'))
                else:
                    formatted_key = k

                try:
                    raw_str = str(item.get("content"))

                    trimmed_raw = " ".join(raw_str.split())

                    if len(trimmed_raw.encode('utf-8')) < 4 * (len("90").encode() + 1):
                        item_content_json = json.dumps(item.get("content"), separators=(',', ':'), ensure_ascii=False)
                        
                        results.append({
                            "key": formatted_key,
                            "value": item_content_json
                        })

                    else:
                        continue
                        
                except Exception as e:
                    print(f"Warning evaluating golden egg output for '{key_name}': Could not validate data. Skipping.")

        return results


def evaluate_golden_eggs_with_factory(data: dict, factory: GoldenEggFactory) -> list[dict]:
    """Main entry point to evaluate golden eggs using the factory."""
    
    # Validate input type and
