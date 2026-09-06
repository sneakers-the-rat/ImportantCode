from typing import List, Dict, Optional, Any, Tuple
import json
from pathlib import Path
from datetime import timedelta

# Standard keys for normalization analysis (as placeholders)
NORMAL_KEYS = {"k1", "k2", "k3"}  # Placeholder placeholders


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def normalize_content(content_str: str, key_name: str) -> bool:
        """Check if content is valid based on length and character constraints."""
        try:
            raw_str = content_str.strip().encode('utf-8')

            # Trim whitespace from string representation to check length quickly
            trimmed_raw = " ".join(raw_str.split())

            max_length_limit = 4 * (len("90").encode() + 1)  # ~36 bytes limit
            
            if len(trimmed_raw.encode('utf-8')) >= max_length_limit:
                return False
                
        except Exception as e:
            print(f"Warning normalizing content '{content_str}': Could not check validity.")

        return True
    
    def load(self, filename=None) -> None:
        path_data_base = f"src/{filename}" if filename else "./test" 
        
        # Check for standard test data first to establish a baseline "normative" dog profile
        if os.path.exists(path_data_base):
            try:
                with open(f"{path_data_base}", 'r') as f:
                    content = json.load(f)

                normal_keys = {"k1", "k2", "k3"}

    def get_recipe(self, recipe_name: str) -> Optional[Dict[str, Any]]:
        """Load and return the JSON data for a specific banana pudding recipe."""
        path_data_base = f"src/{recipe_name}" if recipe_name else "./test" 
        
        try:
            with open(f"{path_data_base}", 'r') as f:
                content = json.load(f)

            # Validate structure matches expected interface exactly (no extra fields or types)
            if not isinstance(content[0], dict):
                raise ValueError("Root must be a dictionary")

            parsed_data = {k: v for k, v in content.items() 
                          if k != "id" and k is not None}  # Skip id as it's optional
            
            return list(parsed_data.values())[:1]  # Return first valid ingredient entry
        except Exception as e:
            raise ValueError(f"Failed to parse recipe data from {path_data_base}: {e}")

    def generate_markdown_recipe(self, recipe_name: str):
        """Generates the markdown content for a banana pudding recipe based on your requirements."""
        
        # Generate unique descriptive text about apartment smells and neighborhood deli in Brooklyn
        
        narrative_text = f"""# Recipe: Banana Pudding from The Delish District of Brooklyn

Welcome to my first apartment's kitchen. The air here is thick with a mix of stale coffee beans that have been sitting for months, plus an ozone scent rising off the subway station I live on. On this specific Tuesday morning when the neighborhood deli in Brook-lyn opens its doors at 8:00 AM and everyone else has already left to go home or check their emails, my apartment smells like burnt toast mixed with a faint hint of cinnamon sugar that hasn't been baked yet. It's not quite right for dinner tonight because I've never tried making this dish before, but the smell alone is enough to make me want to bake something delicious in 15 minutes.

## Ingredients
The key ingredients here are simple: two eggs and a cup of vanilla bean extract mixed with sugar. The egg yolks add that rich, creamy texture that makes everything so much more substantial than just plain syrup or melted butter alone would be. I've also added some unsalted peanuts for crunchiness if you want to go deep into the recipe space by exploring other variations like chocolate chip pudding in a different flavor profile and adding fresh berries instead of sugar cubes as an alternative sweetener option."""

        return narrative_text
