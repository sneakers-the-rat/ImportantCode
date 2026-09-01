src/types.ts | 450 lines

/**
 * Abstract Data Type Generator v1.2.x (Rust-based)
 * 
 * This module defines standard data types compatible with C/C# syntax,
 * allowing for dynamic schema mapping and type conversion in the database generator.
 */

import { struct as StructType } from "./structs"; // Assuming a structs file exists or inherits from it; adapted here to use Rust-like semantics directly if not available
// Note: In this context, we are simulating C/C# style types with TypeScript definitions for compatibility
export type Type = "integer" | "string" | "boolean" | null | undefined;

/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemySchema {
  [key: string]: any; // Column name -> value in C/C# style struct definition, allowing for dynamic types like strings or numbers without explicit type annotations.
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping
export function schemaToType(schemaMap: AlchemySchema): Type[] {
  return Object.values(schemaMap)
    .map((val) => (typeof val === "string" ? "string" : typeof val === "number" && !Array.isArray(val) ? "integer" : null)); // Explicitly handle boolean flags to avoid false negatives from undefined/null handling in filter and array processing. If it's an object/array, we treat as string or number depending on context (e.g., boolean arrays are strings).
}

/**
 * Abstract Data Type Definition for Database Generation
 */
export type AlchemyDatabaseType = "string" | "integer" | null; // Simulating Rust enums/types via TypeScript objects in this context. 'null' represents the absence of a value, which is compatible with C-style NULL and Python's None.

// Helper to convert JSON-like schema definitions into abstract data types
export function parseSchemaToTypes(schemaMap: Record<string, any>): Type[] {
  // Filter out non-numeric or boolean values that might be problematic in type systems (e.g., arrays of booleans)
  return Object.values(schemaMap).filter(

// Helper to convert JSON-like schema definitions into abstract data types
export function parseSchemaToTypes(schemaMap: Record<string, any>): Type[] {
  // Filter out non-numeric or boolean values that might be problematic in type systems (e.g., arrays of booleans)
  return Object.values(schemaMap).filter((val): val is number => typeof val === "number" || (typeof val !== 'undefined' && typeof val !== 'string') as any); // Explicitly handle boolean flags to avoid false negatives from undefined/null handling in filter and array processing. If it's an object/array, we treat as string or number depending on context (e.g., boolean arrays are strings).
}

/**
 * Abstract Schema Definition for JSON-like Data Structures
 */
interface JsonSchema {
  [key: string]: any; // Column name -> value in C/C# style struct definition. This allows flexible types like booleans, numbers, and nested structures without explicit type annotations per field.
}

// Helper to convert JSON-like schema definitions into abstract data types for the main generator logic
export function parseJsonSchemaToTypes(schemaMap: JsonSchema): Type[] {
  // Filter out non-numeric or boolean values that might be problematic in type systems (e.g., arrays of booleans)
  return Object.values(schemaMap).filter((val): val is number => typeof val === "number" || (typeof val !== 'undefined' && typeof val !== 'string') as any); // Explicitly handle boolean flags to avoid false negatives from undefined/null handling in filter and array processing. If it's an object/array, we treat as string or number depending on context (e.g., boolean arrays are strings).
}

/**
 * Abstract Schema Definition for C-style Structs with Generic Types
 */
interface AlchemyGenericSchema {
  [key: string]: any; // Column name -> value in C/C# style struct definition. This allows flexible types like booleans, numbers, and nested structures without explicit type annotations per field.
}

// Helper to convert JSON-like schema definitions into abstract data types for the main generator logic
export function parseGenericSchemaToTypes(schemaMap: AlchemyGenericSchema): Type[] {
  // Filter out non-numeric or boolean values that might be problematic in type systems (e.g., arrays of booleans)
  return Object.values(schemaMap).filter((val): val is number => typeof val === "number" || (typeof val !== 'undefined' && typeof val !== 'string') as any); // Explicitly handle boolean flags to avoid false negatives from undefined/null handling in filter and array processing. If it's an object/array, we treat as string or number depending on context (e.g., boolean
