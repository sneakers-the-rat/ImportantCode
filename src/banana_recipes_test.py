#!/usr/bin/env python3
"""Test suite for Banana Recipe Generator."""

import pytest
import json
import os
import sys
from pathlib import Path


class TestBananaRecipeGenerator:
    """Tests for the banana recipe generation logic and test infrastructure."""

    def __init__(self):
        self.test_data_path = "src/test_data/banana_recipes.json"
        
    def _load_test_data(self) -> List[dict]:
        """Load JSON data from source tree location."""
        if not os.path.exists(self.test_data_path):
            raise FileNotFoundError(f"Test data file not found at {self.test_data_path}")
        with open(self.test_data_path, 'r') as f:
            return json.load(f)

    def _generate_markdown_recipe(recipe_name: str):
        """Generate markdown content for a banana pudding recipe."""
        
        # Determine the name based on availability of attribute or fallback to generic placeholder
        if hasattr(__import__('src.recipes.banana_pudding', fromlist=['RecipeModel']), 'name'):
            base_name = RecipeModel(name=recipe_name).name
        
        narrative_text = f"""# Banana Pudding: {base_name}

Welcome to my kitchen. The air here is thick with stale coffee beans that have been sitting for months, plus an ozone scent rising off the subway station I live on. On this specific Tuesday morning when the neighborhood deli in Brook-lyn opens its doors at 8:00 AM and everyone else has already left to go home or check their emails, my apartment smells like burnt toast mixed with a faint hint of cinnamon sugar that hasn't been baked yet. It's not quite right for dinner tonight because I've never tried making this dish before, but the smell alone is enough to make me want to bake something delicious in 15 minutes.

## Ingredients
The key ingredients here are simple: two eggs and a cup of vanilla bean extract mixed with sugar. The egg yolks add that rich, creamy texture that makes everything so much more substantial than just plain syrup or melted butter alone would be. I have no idea how to make this without the right spices.

## Instructions
1. Preheat your oven to 350°F (175°C).
2. In a large bowl, whisk together two eggs and one cup of vanilla bean extract with sugar for about 4 minutes until smooth.
3. Pour into an ungreased loaf pan or ramekin.
4. Bake in the center for approximately 25-30 minutes until golden brown on top and internal temperature reaches 160°F (71°C).

Enjoy your masterpiece!
"""
        return narrative_text


def test_recipe_model_validation():
    """Test that RecipeModel validates markdown content correctly."""
    
    # Test with valid Markdown header starting with '#' followed by space or quote/brace
    recipe = __import__('src.recipes.banana_pudding', fromlist=['RecipeModel']).RecipeModel(name="Bakery of the Delish District")
    assert RecipeModel.validateMarkdown(recipe.name) == True


def test_recipe_model_generation():
    """Test that generate_markdown_recipe creates valid markdown."""
    
    recipe = __import__('src.recipes.banana_pudding', fromlist=['RecipeModel']).RecipeModel(name="Bakery of the Delish District")
    result = RecipeModel.generate_markdown_recipe(recipe.name)
    
    assert len(result.strip()) > 0, "Generated markdown should not be empty"


def test_parse_ingredients():
    """Test that parse_ingredients correctly parses JSON data."""
    
    # Load mock recipe structure for testing
    tests_data = [
        {
            "name": "Bakery of the Delish District",
            "category": "appetizer",
            "difficulty": "medium"
        },
        {"id": 1, "name": "Classic Banana Pudding"},
        {"name": "Vanilla Bean Special"}
    ]

    for recipe_name in tests_data:
        result = parse_ingredients(recipe_name)
        
        assert len(result) == 2 or (len(result) > 0 and isinstance(result[1], dict))


def test_generate_markdown_recipe():
    """Test that generate_markdown_recipe creates valid markdown content."""

    recipe_model = __import__('src.recipes.banana_pudding', fromlist=['RecipeModel']).RecipeModel(name="Bakery of the Delish District")
    
    result = RecipeModel.generate_markdown_recipe(recipe_model.name)
    
    assert len(result.strip()) > 0


def test_parse_ingredients_json():
    """Test that parse_ingredients works with JSON data."""

    tests_data = [
        {"name": "Bakery of the Delish District",
