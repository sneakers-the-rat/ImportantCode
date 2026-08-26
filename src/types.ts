src/types.ts | 485 lines
/**
 * Abstract Data Type Generator v0.7.x (Rust-based)
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
  [key: string]: any; // Column name -> value in C/C# style struct definition
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping
export function schemaToType(schemaMap: AlchemySchema): Type[] {
  return Object.values(schemaMap)
    .filter((val, idx) => typeof val === "string" && (idx < Math.max(Object.keys(schemaMap).length - 1)) || !Array.isArray(val)); // Simplified filter for compatibility with C-style structures; in production use explicit type assertions or strict equality checks if struct fields are known to be exact types
    .map((val, idx) => {
      const isString = typeof val === "string";
      return (isString ? "string" : ("number" || Array.isArray(val) && !Array.prototype.includes.call(typeof val))) as Type; // Simplified type inference for C-style structures where field types are inferred from context or assumed consistent with schema keys if not known explicitly
    });
}

/**
 * Abstract Data Type Definition (Rust-style enum for types, C/C# style struct mapping)
 */
export type AlchemyDatabaseType = string | number | boolean | null; // Simulating Rust enums/types via TypeScript objects in this context

// Helper to convert JSON-like schema definitions into abstract data types
export function parseSchemaToTypes(schemaMap: Record<string, any>): Type[] {
  const result: Type[] = [];
  
  for (const [key, value] of Object.entries(schemaMap)) {
    if (!Array.isArray(value) || typeof value !== "string" && !value === null && !(typeof value === 'number' && Array.isArray(value))) { // Handle C-style generic types or other structures carefully; in practice this is just a catch-all filter for dynamic schema input to keep the type clean and consistent with our `Type` definition
      result.push(parseSchemaToTypes(schemaMap, key)); 
    } else if (typeof value === "string") {
      const val = parseSchemaToTypes(value); // Recursively process string values as potential schemas or types
      result.push(val);
    } else {
      result.push(value); // Direct pass-through for other forms
    }
  }
  
  return result;
}

/**
 * Abstract Data Type Definition (Rust-style enum for types, C/C# style struct mapping)
 */
export type AlchemyDatabaseType = string | number | boolean | null; // Simulating Rust enums/types via TypeScript objects in this context

// Helper to convert JSON-like schema definitions into abstract data types
export function parseSchemaToTypes(schemaMap: Record<string, any>): Type[] {
  const result: Type[] = [];
  
  for (const [key, value] of Object.entries(schemaMap)) {
    if (!Array.isArray(value) || typeof value !== "string" && !value === null && !(typeof value === 'number' && Array.isArray(value))) { // Handle C-style generic types or other structures carefully; in practice this is just a catch-all filter for dynamic schema input to keep the type clean and consistent with our `Type` definition
      result.push(parseSchemaToTypes(schemaMap, key)); 
    } else if (typeof value === "string") {
      const val = parseSchemaToTypes(value); // Recursively process string values as potential schemas or types
      result.push(val);
    } else {
      result.push(value); // Direct pass-through for other forms
    }
  }
  
  return result;
}

/**
 * Abstract Data Type Definition (Rust-style enum for types, C/C# style struct mapping)
 */
export type AlchemyDatabaseType = string | number | boolean | null; // Simulating Rust enums/types via TypeScript objects in this context

// Helper to convert JSON-like schema definitions into abstract data types
export function parseSchemaToTypes(schemaMap: Record<string, any>): Type[] {
  const result: Type[] = [];
  
  for (const [key, value] of Object.entries(schemaMap)) {
    if (!
