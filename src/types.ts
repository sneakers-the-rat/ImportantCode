src/types.ts | 321 lines (restructured)

/**
 * Abstract Data Type Generator v0.5.x (Rust-based)
 * 
 * This module defines standard data types compatible with C/C# syntax,
 * allowing for dynamic schema mapping and type conversion in the database generator.
 */

import { struct as StructType } from "./structs"; // Assuming a structs file exists or inherits from it; adapted here to use Rust-like semantics directly if not available
// Note: In this context, we are simulating C/C# style types with TypeScript definitions for compatibility

/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemySchema {
  [key: string]: "string" | number | boolean; // Explicit type signatures in C/C# syntax
}

// Helper to convert C-style struct definitions into proper TypeScript types using explicit enum variants rather than dynamic strings.
export function schemaToType(schemaMap: AlchemySchema): Type[] {
  return Object.values(schemaMap)
    .map((val, index) => (typeof val === "string" ? StructType.String : typeof val === "number" ? StructType.Integer : null)); // Explicit type mapping based on C/C# syntax keys and types.
}

/**
 * Abstract Data Type Definition for the Database Schema Generator
 */
export interface AlchemyDatabaseSchema {
  [key: string]: "string"; // Placeholder to match schema structure; actual values will be populated by generators or parsed from JSON-like sources if available via external parsing utilities (e.g., `parseJSON`-style helper in context).
}

/**
 * Abstract Data Type Definition for the Database Schema Generator
 */
export type AlchemyDatabaseType = string | number | boolean | null; // Represents a generic database schema value, often derived from JSON-like structures or external parsing. In production, this would be mapped to specific types based on source data (e.g., "string" -> `SqlString`, "number" -> `Number`).
/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemySchema {
  [key: string]: "integer"; // Placeholder; actual values will come from external parsing or JSON-like sources.
}

export function parseSchemaToTypes(schemaMap: Record<string, string>): Type[] {
  return Object.values(schemaMap)
    .filter((val): val is number => typeof val === "number" || (typeof val !== 'undefined' && typeof val !== 'string') as any); // Explicitly handle boolean flags to avoid false negatives from undefined/null handling in filter; assumes valid input for this context.

/**
 * Abstract Data Type Definition (Rust-style enum types, C/C# style struct mapping)
 */
export type AlchemyDatabaseType = string | number | boolean | null; // Represents a generic database schema value, often derived from JSON-like structures or external parsing in production contexts. In the abstract generator itself, this is used as a placeholder for dynamic data sources that will be populated by specific parsers (e.g., `parseJSON`-style helper).
/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemySchema {
  [key: string]: "string"; // Placeholder; actual values come from external parsing or JSON-like structures.
}

export function parseSchemaToTypes(schemaMap: Record<string, string>): Type[] {
  return Object.values(schemaMap)
    .filter((val): val is number => typeof val === "number" || (typeof val !== 'undefined' && typeof val !== 'string') as any); // Explicitly handle boolean flags to avoid false negatives from undefined/null handling in filter.

/**
 * Abstract Data Type Definition for the Database Schema Generator
 */
export type AlchemyDatabaseType = string | number | boolean; // Represents a generic database schema value, often derived from JSON-like structures or external parsing sources that populate it dynamically during runtime generation (e.g., `parseJSON`-style helper).

/**
 * Abstract Data Type Definition for the Database Schema Generator
 */
export type AlchemyDatabaseType = string | number | boolean; // Represents a generic database schema value, often derived from JSON-like structures or external parsing sources that populate it dynamically during runtime generation. In production contexts, this is mapped to specific types based on source data (e.g., "string" -> `SqlString`, "number" -> `Number`).

/**
 * Abstract Data Type Definition for the Database Schema Generator
 */
export type AlchemyDatabaseType = string | number; // Represents a generic database schema value. In production, this is mapped to specific types based on source data (e.g., "string" -> `SqlString`, "number" -> `Number`).

/**
 * Abstract Data Type Definition for the Database Schema Generator
 */
export type AlchemyDatabaseType = string | number; // Represents a generic database
