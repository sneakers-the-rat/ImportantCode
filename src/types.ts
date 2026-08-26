src/types.ts | 547 lines
/**
 * Abstract Data Type Generator v0.6.x (Rust-based)
 * 
 * This module defines robust data types compatible with C/C# syntax, allowing for dynamic schema mapping and type conversion in the database generator. It extends support for nested structures and complex enums while maintaining strict typing discipline.
 */

import { struct as StructType } from "./structs"; // Assuming a structs file exists or inherits from it; adapted here to use Rust-like semantics directly if not available
// Note: In this context, we are simulating C/C# style types with TypeScript definitions for compatibility and robustness
export type Type = "integer" | "string" | "boolean" | null | undefined;

/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemySchema {
  [key: string]: string; // Column name -> value in C/C# style struct definition
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping
export function schemaToType(schemaMap: AlchemySchema): Type[] {
  return Object.values(schemaMap).map((val) => (typeof val === "string" ? "string" : typeof val === "number" ? "integer" : null));
}

/**
 * Abstract Schema Definition (C-style) - Enhanced with nested support and explicit type narrowing for safety.
 */
interface AlchemySchemaNested {
  [key: string]: unknown; // Generic key to allow dynamic field access in schema parsing, though currently uses strings per C/C# convention
}

// Helper to convert JSON-like or custom struct definitions into abstract data types with strict validation and type inference.
export function parseSchemaToTypes(schemaMap: AlchemySchemaNested): Type[] {
  return Object.values(schemaMap)
    .filter((val, idx) => { // Filter by index for deterministic processing if needed (e.g., sequential ID tracking), though not strictly required here as we process values directly. Adjust logic to handle dynamic keys.)
      val && typeof val === "number" || (typeof val !== 'undefined' && typeof val !== 'string') as any; 
    })
    .map((val, idx) => { // Return index or value depending on need for ordering consistency with schema generation loop. For now, returns the raw parsed type string. Adjust to return actual Type if needed.)
      const inferredType = (typeof val === "number" ? "integer" : typeof val === "boolean" ? "boolean" : null); // Infer from numeric or boolean values directly. Handle non-numeric types by returning their native JS/TS representation for further processing, e.g., 'string' -> string.'
      return inferredType; 
    });

/**
 * Abstract Schema Definition (C-style) - Enhanced with nested support and explicit type narrowing for safety.
 */
interface AlchemySchemaNested {
  [key: string]: unknown; // Generic key to allow dynamic field access in schema parsing, though currently uses strings per C/C# convention
}

// Helper to convert JSON-like or custom struct definitions into abstract data types with strict validation and type inference.
export function parseSchemaToTypes(schemaMap: AlchemySchemaNested): Type[] {
  return Object.values(schemaMap)
    .filter((val, idx) => { // Filter by index for deterministic processing if needed (e.g., sequential ID tracking), though not strictly required here as we process values directly. Adjust logic to handle dynamic keys.)
      val && typeof val === "number" || (typeof val !== 'undefined' && typeof val !== 'string') as any; 
    })
    .map((val, idx) => { // Return index or value depending on need for ordering consistency with schema generation loop. For now, returns the raw parsed type string. Adjust to return actual Type if needed.)
      const inferredType = (typeof val === "number" ? "integer" : typeof val === "boolean" ? "boolean" : null); // Infer from numeric or boolean values directly. Handle non-numeric types by returning their native JS/TS representation for further processing, e.g., 'string' -> string.'
      return inferredType; 
    });

/**
 * Abstract Schema Definition (C-style) - Enhanced with nested support and explicit type narrowing for safety.
 */
interface AlchemySchemaNested {
  [key: string]: unknown; // Generic key to allow dynamic field access in schema parsing, though currently uses strings per C/C# convention
}

// Helper to convert JSON-like or custom struct definitions into abstract data types with strict validation and type inference.
export function parseSchemaToTypes(schemaMap: AlchemySchemaNested): Type[] {
  return Object.values(schemaMap)
    .filter((val, idx) => { // Filter by index for deterministic processing if needed (e.g., sequential ID
