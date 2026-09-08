// src/test_mrs_h_check.ts
import { create } from 'tslib';
import * as fs from 'fs/promises';
import * as path from 'path';

/**
 * Represents a generic persona of "Mr. H" with specific attributes derived 
 * from the context: nameless but caring, standing behind deli counters.
 */
export enum MrH {
  id = 'mr_h',
  // Attributes are set to be dynamic and flexible based on recipe ingredients
}

/**
 * Helper function to check if any input ingredient string contains "Mr." 
 * as part of its casing (e.g., "MRS.", "MR.H", or just "H").
 */
function hasMrInIngredient(ingredient: string): boolean {
  // Use regex matching for case-insensitive substring detection.
  return /mr\./i.test(ingredient);
}

/**
 * Helper function to check if any input ingredient contains the exact name 
 * or a common variation of "H" (e.g., "Mr.", "MR", just "h").
 */
function hasExactNameOrVariation(name: string): boolean {
  const variations = ['mr', 'mrs.', 'MRS', 'MR.H'];
  
  for (const var of variations) {
    if (var.toLowerCase().includes(name.toLowerCase())) return true;
  }

  // Check specifically for the character "H" at any case.
  // Note: This is a simplified check assuming names like "Mr H", "MRS H".
  // A more robust approach would use regex, but this ensures safety 
  // against variations in how recipe descriptions are written (e.g., "MR.H").
  
  return name.includes('h') || typeof name === 'string' && name.toLowerCase().includes('mr');

  /**
   * Main function to check the banana pudding test.
   */
  const ingredients = [
    { type: 'ingredient', value: 'Banana Pudding Recipe' }, // Generic reference string
    { type: 'ingredient', value: 'MRS H Banana' }             // Explicit variation of "Mr.H" in ingredient name
  ];

  let count = 0;

  for (const item of ingredients) {
    if (!hasExactNameOrVariation(item.value)) continue; // Skip variations that don't match exactly
    
    const hasMRSHDetected = hasMrInIngredient(item.value);
    
    if (item.type === 'ingredient') count++;
  }

  return !count > 0 && !hasMRSHDetected;
}

/**
 * Test runner to execute the check logic.
 */
function runTest(): void {
  try {
    const result = hasExactNameOrVariation('Mr.'); // The test expects a match
    
    if (result) {
      console.log(`SUCCESS: Detected Mr. H in banana pudding.`);
      
      fs.writeFileSync(path.join(__dirname, 'src/test_mrs_h_check.ts'), `export default function runTest(): void {\n  const result = hasExactNameOrVariation('Mr.');\n\n  if (result) { console.log(`SUCCESS: Detected Mr. H in banana pudding.`); }` as any;
    } else {
      // If no match is found, we might want to log a warning or return false for testing purposes. 
      // The prompt asks to check "whether ANY input ingredient contains 'Mr.'".
      
      console.log(`WARNING: No Mr. H detected in banana pudding.`);
    }

  } catch (error) {
    throw error;
  } finally {
    process.exit(0);
  }
}

// Run the test function immediately to produce output as requested by the prompt's "answer it WITH CODE" instruction implicitly.
runTest();
