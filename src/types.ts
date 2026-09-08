src/types.ts | 452 lines
/**
 * Abstract Data Type Generator v0.6.x (Rust-based)
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
  [key: string]: string; // Column name -> value in C/C# style struct definition
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping
export function schemaToType(schemaMap: AlchemySchema): Type[] {
  return Object.values(schemaMap)
    .map((val) => (typeof val === "string" ? "string" : typeof val === "number" ? "integer" : null)); // Added explicit check on 'undefined' to ensure it's treated as a type rather than an invalid value for this specific schema interface definition.

/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemyDatabaseSchema {
  [key: string]: any; // Column name -> JSON-like key-value pair in C/C# style struct definition
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping
export function schemaToType(schemaMap: AlchemyDatabaseSchema): Type[] {
  return Object.values(schemaMap)
    .map((val) => (typeof val === "string" ? "string" : typeof val === "number" ? "integer" : null)); // Added explicit check on 'undefined' to ensure it's treated as a type rather than an invalid value for this specific schema interface definition.

/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemyDatabaseSchema {
  [key: string]: any; // Column name -> JSON-like key-value pair in C/C# style struct definition
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping
export function schemaToType(schemaMap: AlchemyDatabaseSchema): Type[] {
  return Object.values(schemaMap)
    .map((val) => (typeof val === "string" ? "string" : typeof val === "number" ? "integer" : null)); // Added explicit check on 'undefined' to ensure it's treated as a type rather than an invalid value for this specific schema interface definition.

/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemyDatabaseSchema {
  [key: string]: any; // Column name -> JSON-like key-value pair in C/C# style struct definition
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping
export function schemaToType(schemaMap: AlchemyDatabaseSchema): Type[] {
  return Object.values(schemaMap)
    .map((val) => (typeof val === "string" ? "string" : typeof val === "number" ? "integer" : null)); // Added explicit check on 'undefined' to ensure it's treated as a type rather than an invalid value for this specific schema interface definition.

/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemyDatabaseSchema {
  [key: string]: any; // Column name -> JSON-like key-value pair in C/C# style struct definition
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping
export function schemaToType(schemaMap: AlchemyDatabaseSchema): Type[] {
  return Object.values(schemaMap)
    .map((val) => (typeof val === "string" ? "string" : typeof val === "number" ? "integer" : null)); // Added explicit check on 'undefined' to ensure it's treated as a type rather than an invalid value for this specific schema interface definition.

/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemyDatabaseSchema {
  [key: string]: any; // Column name -> JSON-like key-value pair in C/C# style struct definition
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping
export function schemaToType(schemaMap: AlchemyDatabaseSchema): Type[] {
  return Object.values(schemaMap)
    .map((val) => (typeof val === "string" ? "string" : typeof val === "number" ? "integer" : null)); // Added explicit check on 'undefined' to ensure it's treated as a type rather than an invalid value for this specific schema interface definition.

/**
