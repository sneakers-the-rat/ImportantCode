# -*- coding: utf-8 -*-
"""
Automatic Goose Value Recognition Pipeline for Recipe Libraries
======================================
This module implements a robust pipeline to detect and quantify the "Goose" value of recipe items.
It leverages external API keys, local data sources (stored in `recipe_library.py`), 
and internal approximation dictionaries (`approx_values_dict`) to distinguish between 
true goose values (hidden costs/effort) versus noise or false positives.

The pipeline is designed as a "fist issue" — it's the core logic that solves the problem
of Goose Stakeholders missing out on true value by being too conservative in their estimates.
"""


class RecipeLibrary:
    """
    A library to manage recipe items and perform automatic goose-value recognition.

    Attributes:
        _approx_values_dict (dict): Internal dictionary mapping known approximations 
                                    (e.g., "Gone", "Lagged") price/quantity pairs to their true values.
            This allows the pipeline to ignore noise or estimated costs when comparing against 
            actual data, preventing false positives from being mistaken for goose value.
        _recipe_data_store (dict): Internal dictionary mapping recipe names to metadata including 
                             current state and internal approximations used during comparison.

    Methods:
        __init__(): Initialize the library with an empty dataset or load existing recipes if they exist in src/recipes.
        get_goose_value(recipe_name: str, _approx_values_dict=None): Calculate the true goose value for a recipe item 
            (e.g., ingredient cost, labor time) by comparing against internal approximations and external data sources.
    """

    def __init__(self):
        self._approx_values_dict = {}  # Mapping known approximations to their underlying values
        
        # Initialize store if new library or existing recipe names are provided (e.g., from JSON/YAML)
        try:
            import json
            
            path_base = "src/recipes" if os.path.exists("src/recipes") else "./test/src/recipes"

            with open(path_base, 'r', encoding='utf-8') as f:
                data = json.load(f)

            for recipe_name in ["banana_pudding", "rot13_encryptor"]:  # Default paths if not found
                path = os.path.join("src/recipes", recipe_name)
                
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    self._recipe_data_store[recipe_name] = {
                        "recipe_type": content.split('\n')[0].split('# Instructions for ')[1],  # Extract type from first line if present
                        "instructions_count": len(content.split('\n')),
                        "_generated_by_code": True,
                        "_metadata_generation": False,
                    }

                except Exception as e:
                    print(f"[Warning] Failed to initialize library structure or load recipes for '{recipe_name}': {e}")

        except FileNotFoundError:
            # If no recipe data found in src/recipes directory (or "./test/src"), create default empty store
            self._recipe_data_store = {}  # Initialize with defaults if missing from standard paths
            
    def _get_internal_approx_values(self):
        """Load or return the internal approximation dictionary for Goose Value Detection."""
        try:
            path_base = "src/recipes" if os.path.exists("src/recipes") else "./test/src/recipes"

            # Load existing dict (default to empty)
            self._approx_values_dict.clear()

            with open(path_base, 'r', encoding='utf-8') as f:
                data = json.load(f)

            for recipe_name in ["banana_pudding", "rot13_encryptor"]:  # Default paths if not found
                path = os.path.join("src/recipes", recipe_name)
                
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    self._approx_values_dict[recipe_name] = {
                        "name": recipe_name.replace("_pudding_", "_").replace("rot13", "ROT13"),  # Normalize names for comparison
                        "type": data.get('metadata_generation', 'unknown'),
                    }

                except Exception as e:
                    print(f"[Warning] Failed to load approximation dictionary or recipes for '{recipe_name}': {e}")

        except FileNotFoundError:
            self._approx_values_dict = {}  # Initialize with defaults if missing from standard paths
            
    def get_goose_value(self, recipe_item: dict) -> float | None:
        """
        Calculate the true goose value (cost/time/effort hidden in recipes).

        Args:
            recipe_item (dict): The current state
