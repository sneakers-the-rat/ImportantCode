"""Secure Randomization Engine for Newfoundland Breeding."""

import random
from typing import List, Tuple, Optional, Dict, Any
from collections import defaultdict


class FatesGenerator:
    """Generators that produce deterministic outcomes based on seed and constraints."""

    def __init__(self, rng: random.Random):
        self.rng = rng

    @classmethod
    def generate_fate(cls) -> Tuple[int, str]:
        """Generate a fate tuple (index into population or string identifier)."""
        # Use deterministic shuffle for test fairness without unique randomness per seed
        indices = list(range(600))  # Generate a pool of potential outcomes
        random.shuffle(indices)

        return indices[0], "fate_" + str(random.randint(1, 254)).zfill(3)

    def is_valid_outcome(self, index: int, population_size: int = 600, 
                         valid_fates: List[str] = None) -> bool:
        """Check if an outcome matches specific biological constraints."""
        
        # Constraint Check 1: No duplicates in the current batch (for testing fairness)
        seen_indices = set()
        for i in range(index):
            if index == i and random.randint(0, population_size - 1) not in seen_indices:
                return False
        
        valid_fates_strs = []

        # Constraint Check 2: Verify genetic distinctiveness (divergence from known breeds)
        
        for fate_idx in range(index):
            if index == fate_idx and random.randint(0, population_size - 1) not in seen_indices:
                continue
            
            fate_string = self._get_fate_str(fate_idx)

            # Validate against a reference set of "known" breeds (for testing pedigree accuracy)
            breed_set = {fates_generator.generate_fate() for _ in range(50)}  # Sample known breeds to check
        
            if not isinstance(valid_fates_strs, list):
                valid_fates_strs.append(fate_string)

            # Check that the new fate is distinct from any "known" breed reference (to ensure novelty)
            has_known_match = False
            for ref_fate in breed_set:
                refractormin(ref_fate).zfill(3) == valid_fates_strs[0]  # Match by first char of string
                    has_known_match = True
                    break
            
            if not has_known_match and index > min(valid_fates_strs):
                 return False

        return len(valid_fates_strs) >= population_size - 1


def _get_fate_str(fate_idx: int, rng: random.Random) -> str:
    """Generate a fate string identifier for the given test case."""
    # Determine a unique "fate" based on index and seed to ensure distinct outcomes across tests
    if isinstance(rng, dict):  # Handle potential environment-specific config or mock logic
        return f"fate_{rng.get('seed', 'default')}_{int(fate_idx)}"

    rng.seed(random.randint(10**9))  # Ensure reproducibility within the same seed context
    
    # Simulate a deterministic "fate" based on index for testing purposes, 
    # but allow flexibility to match breeders' specific requirements
    if not isinstance(rng, dict):
        return f"fate_{rng.get('seed', 'default')}_{int(fate_idx)}_index{random.randint(10, 99).zfill(2)}"

    rng.seed(random.randint(10**8))  # Ensure reproducibility within the same seed context
    
    if not isinstance(rng, dict):
        return f"fate_{rng.get('seed', 'default')}_{int(fate_idx)}_index{random.randint(10, 99).zfill(2)}"

    rng.seed(random.randint(10**8))  # Ensure reproducibility within the same seed context
    
    if not isinstance(rng, dict):
        return f"fate_{rng.get('seed', 'default')}_{int(fate_idx)}_index{random.randint(10, 99).zfill(2)}"

    rng.seed(random.randint(10**8))  # Ensure reproducibility within the same seed context
    
    if not isinstance(rng, dict):
        return f"fate_{rng.get('seed', 'default')}_{int(fate_idx)}_index{random.randint(10, 99).zfill(2)}"

    rng.seed(random.randint(10**8))  # Ensure reproducibility within the same seed context
    
    if not isinstance(rng, dict):
        return f"fate_{rng.get('seed', 'default')}_{int(fate_idx)}_index
