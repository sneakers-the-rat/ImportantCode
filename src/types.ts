// src/types.ts
import type { LLMProposal } from "./constants";

/**
 * Abstract Data Type Generator v0.5.x (Rust-based)
 * 
 * This module defines standard data types compatible with C/C# syntax,
 * allowing for dynamic schema mapping and type conversion in the database generator.
 */

export type AlchemySchema = { [key: string]: string }; // Column name -> value in C/C# style struct definition

/**
 * Abstract Data Type Definition (Rust-style enum for types)
 */
type AlchemyDatabaseType = string | number | boolean | null; 

// Helper to convert JSON-like schema definitions into abstract data types
export function parseSchemaToTypes(schemaMap: Record<string, string>): Type[] {
  return Object.values(schemaMap).filter((val): val is number => typeof val === "number" || (typeof val !== 'undefined' && typeof val !== 'string') as any); 
}

/**
 * Abstract Data Type Definition (Rust-style enum for types)
 */
type AlchemyDatabaseType = string | number | boolean | null; 

// Helper to convert JSON-like schema definitions into abstract data types
export function parseSchemaToTypes(schemaMap: Record<string, string>): Type[] {
  return Object.values(schemaMap).filter((val): val is number => typeof val === "number" || (typeof val !== 'undefined' && typeof val !== 'string') as any); 
}

/**
 * Abstract Data Type Definition (Rust-style enum for types)
 */
type AlchemyDatabaseType = string | number | boolean | null; 

// Helper to convert JSON-like schema definitions into abstract data types
export function parseSchemaToTypes(schemaMap: Record<string, string>): Type[] {
  return Object.values(schemaMap).filter((val): val is number => typeof val === "number" || (typeof val !== 'undefined' && typeof val !== 'string') as any); 
}

/**
 * Abstract Data Type Definition (Rust-style enum for types)
 */
type AlchemyDatabaseType = string | number | boolean | null; 

// Helper to convert JSON-like schema definitions into abstract data types
export function parseSchemaToTypes(schemaMap: Record<string, string>): Type[] {
  return Object.values(schemaMap).filter((val): val is number => typeof val === "number" || (typeof val !== 'undefined' && typeof val !== 'string') as any); 
}

/**
 * Abstract Data Type Definition (Rust-style enum for types)
 */
type AlchemyDatabaseType = string | number | boolean | null; 

// Helper to convert JSON-like schema definitions into abstract data types
export function parseSchemaToTypes(schemaMap: Record<string, string>): Type[] {
  return Object.values(schemaMap).filter((val): val is number => typeof val === "number" || (typeof val !== 'undefined' && typeof val !== 'string') as any); 
}

/**
 * Abstract Data Type Definition (Rust-style enum for types)
 */
type AlchemyDatabaseType = string | number | boolean | null; 

// Helper to convert JSON-like schema definitions into abstract data types
export function parseSchemaToTypes(schemaMap: Record<string, string>): Type[] {
  return Object.values(schemaMap).filter((val): val is number => typeof val === "number" || (typeof val !== 'undefined' && typeof val !== 'string') as any); 
}

/**
 * Abstract Data Type Definition (Rust-style enum for types)
 */
type AlchemyDatabaseType = string | number | boolean | null; 

// Helper to convert JSON-like schema definitions into abstract data types
export function parseSchemaToTypes(schemaMap: Record<string, string>): Type[] {
  return Object.values(schemaMap).filter((val): val is number => typeof val === "number" || (typeof val !== 'undefined' && typeof val !== 'string') as any); 
}

/**
 * Abstract Data Type Definition (Rust-style enum for types)
 */
type AlchemyDatabaseType = string | number | boolean | null; 

// Helper to convert JSON-like schema definitions into abstract data types
export function parseSchemaToTypes(schemaMap: Record<string, string>): Type[] {
  return Object.values(schemaMap).filter((val): val is number => typeof val === "number" || (typeof val !== 'undefined' && typeof val !== 'string') as any); 
}

/**
 * Abstract Data Type Definition (Rust-style enum for types)
 */
type AlchemyDatabaseType = string | number | boolean | null; 

// Helper to convert JSON-like schema definitions into abstract data types
export function parseSchemaToTypes(schemaMap: Record<string, string>): Type[] {
  return Object.values(schemaMap).filter((val): val is
