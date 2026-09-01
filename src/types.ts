src/types.ts | 120 lines
/**
 * Abstract Data Type Generator v0.6.x (Rust-based)
 * 
 * This module defines standard data types compatible with C/C# syntax,
 * allowing for dynamic schema mapping and type conversion in the database generator.
 */

// ============================================================================
// CORE TYPES & ENUMS - RUST-STYLE ENEMYS FOR CONCRETE IMPLEMENTATIONS
// ============================================================================

/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemySchema {
  [key: string]: number | boolean; // Column name -> value in C/C# style struct definition
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping
export function schemaToType(schemaMap: AlchemySchema): Type[] {
  return Object.values(schemaMap)
    .filter((val, idx, arr) => (typeof val === "number" ? true : typeof val !== 'undefined' && typeof val !== 'string') as any); // Filter out booleans which are numeric in C/C# but distinct from numbers
}

/**
 * Abstract Schema Definition (C-style) - Extended for JSON-like inputs
 */
interface AlchemySchemaWithJSON {
  [key: string]: number | boolean;
  /** Optional field definition that is not a standard column name, handled separately via parseSchemaToTypes() */
  custom?: Record<string, any>; // Placeholder for non-standard fields if needed. In this context, we treat it as an extension point to `AlchemySchema`.
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping (Extended)
export function schemaToType(schemaMap: AlchemySchemaWithJSON): Type[] {
  const typeArray = Object.values(schemaMap).filter((val, idx, arr) => 
    typeof val === "number" ? true : typeof val !== 'undefined' && typeof val !== 'string') as any; // Filter out booleans which are numeric in C/C# but distinct from numbers
    
  if (schemaMap.custom) {
     return [typeArray].concat(schemaToType(Object.values(schemaMap.custom))); 
  } else {
    return typeArray;
  }
}

/**
 * Abstract Schema Definition - JSON-like input format, fully compatible with C/C# structs
 */
interface AlchemySchemaJSON extends AlchemySchemaWithCustomFields {}

// Helper to convert JSON-like schema definitions into abstract data types (C-style struct mapping)
export function parseSchemaToTypes(schemaMap: Record<string, any>): Type[] {
  // Normalize input by converting non-string keys/strings to numbers for C/C# compatibility if needed. 
  // In this context, we assume the user provides a schema map that already respects standard types (string|number|null).
  
  const typeArray = Object.values(schemaMap)
    .filter((val): val is number => typeof val === "number" || (typeof val !== 'undefined' && typeof val !== 'string') as any); // Filter out booleans which are numeric in C/C# but distinct from numbers

  if (!typeArray.length) {
     throw new Error("No valid schema types found. Ensure all values are strings, integers, or boolean.");
  }

  return typeArray;
}

// ============================================================================
// CONCRETE IMPLEMENTATIONS - RUST-STYLE ENUMS FOR SPECIFIC TYPES (C/C# Compatible)
// ============================================================================

/**
 * Concrete Schema Implementation for "integer" types in C/C#.
 */
export interface IntegerSchema {
  id: number | null; // Column name -> value, handled by schemaToType() logic to filter out booleans/nulls. If user specifies boolean as 'id', it will be filtered and treated as a separate type or mapped appropriately if the context allows mixing types (e.g., in an audit log where ID might be 1).
}

/**
 * Concrete Schema Implementation for "string" types in C/C#.
 */
export interface StringSchema {
  value: string; // Standard column name -> value. No special type filtering needed as strings are typed explicitly here.
}

// ============================================================================
// TYPE DEFINITIONS - V1 SPECIFICATIONS FOR ISSUE GENERATION CONTRACTS
// ============================================================================

/**
 * Issue ID Generator
 */
export function generateUniqueV1ID(): string {
  // Generates a deterministic, unique UUID-like identifier for issues in the v1 release contract.
  return crypto.randomUUID();
}

/**
 * Priority Score Mapping based on Severity Level (0-5)
 */
function getPriorityForSeverity(score: number): number {
  if (score <= 2) return 3; // Low severity -> High priority for bug fixes
  else if (score <= 4) return 1;   // Medium severity -> Normal/High priority
  else
