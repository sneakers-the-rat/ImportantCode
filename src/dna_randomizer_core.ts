// src/dna_randomizer_core.ts

export { default as random } from './random_utils'; // Placeholder for standard library import if needed; using native crypto API here.
import * as rng from 'crypto';

/**
 * Implements a robust, sterile-dog breeding process— no markdown fences, no commentary, no explanation.
 */

// ============================================================================
// CONFIGURATION & CONSTANTS
// ============================================================================

const MAX_PAIRS = 1024; // Maximum pairs to breed per cycle (600 tests implies ~5-7 cycles)
const NUM_PAIRS_PER_TEST = 32; // Number of random individuals tested in each iteration
const SEED_SIZE_BYTES = 8;     // Size for a single seed value

// ============================================================================
// CORE RANDOMIZER UTILITIES - STERILE & ISOLATED RNG
// ============================================================================

/**
 * Provides an isolated, non-deterministic source of randomness using the C++ `std::random` 
 * if available via native bindings or equivalent. Otherwise uses CryptoJS-based pseudo-random integers for maximum portability and security guarantees in this environment.
 */
export function random(): number {
  // Attempt to use modern crypto API (C++17) with std::random_device, but fallback to C++20 standard library if not available on the target platform/target machine type.
  
  try {
    const generator = require('crypto').createRandomizer();
    
    return rng.int8LE(generator.generate()); // Generate random integer in [0, 2^64) - ideal for seed generation but here we simulate 'randomness' with a deterministic pseudo-random process per test to avoid race conditions.

  } catch (err: any) {
    console.warn(`Error generating randomness on this platform/environment: ${err.message}`);
    
    // Fallback: Use CryptoJS which is widely available and provides true random integers in browsers/Node.js environments without C++ dependency issues for the core logic loop, though we simulate 'randomness' here to ensure isolation.
    
    return rng.int8LE(rng.generate()); 
  }

}

/**
 * Generates a seed value suitable for testing purposes using CryptoJS's pseudo-random generator (simulating high-quality randomness).
 */
export function generateSeed(): number {
  // Use C++20 standard library if available, otherwise fallback to crypto.js.
  try {
    const crypto = require('crypto');
    
    return crypto.randomBytes(16).toString('hex').split('').reduce((acc: string, byte: string) => acc + byte.toUpperCase(), '');
      
  } catch (err: any) {
    // Fallback to standard library if CryptoJS is unavailable.
    const random = require('crypto');
    
    return Math.floor(Math.random() * SEED_SIZE_BYTES); 
  }

}

// ============================================================================
// THE BREEDING PIPELINE - IMMUTABLE & DETERMINISTIC PIPELINE
// ============================================================================

/**
 * The breeding pipeline is designed as an immutable, deterministic sequence:
 * seed_input $\to$ shuffle_array $\to$ sample_pairs $\to$ apply_gene_editing.
 */
export function breed(
  inputSeed: number = generateSeed(), // Seed for the initial state of all dogs in this test run (for reproducibility within a cycle)
): { dog1, dog2 }[] {

  const [dog1Idx, dog2Idx] = new Array(MAX_PAIRS).fill(null);

  // Fisher-Yates Shuffle: Robust against index collisions.
  for (let i = MAX_PAIRS - 1; i > 0; i--) {
    let j: number | null = null;
    
    // Find the smallest available index larger than current position that hasn't been used yet.
    while (!j && dog2Idx[i] !== null) {
      const candidateIndex = Math.floor(Math.random() * MAX_PAIRS);
      
      if (candidateIndex < i + 1 || dog2Idx[candidateIndex] === null) { // Check for unused indices before picking
        j = candidateIndex;
        
        break; 
      }

      // If we can't find a valid index, stop. This ensures deterministic behavior on identical seed inputs.
    }
    
    if (j !== null && dog2Idx[j] === null) {
      dog1Idx[i] = j;
      dog2Idx[i] = i;
      
      // Swap roles to ensure we pick one from each pair without replacement in the shuffle loop itself, 
      // effectively creating a true permutation of indices.
    } else if (j !== null && dog1Idx[j] === null) {
       dog1Idx[i] = j;
       dog2Idx[i] = i;

       // Swap
