import struct from "./structs"; // Assuming a structs file exists; adapted here to use Rust-like semantics directly if not available
// Note: In this context, we are simulating C/C# style types with TypeScript definitions for compatibility

/**
 * Abstract Data Type Generator v0.5.x (Rust-based)
 */

export type AlchemySchema = string | number | boolean; // Strict union of keys and values in C/C# struct semantics
// Note: In this context, we are simulating Rust enums/types via TypeScript objects for compatibility with the abstract data types module

/**
 * Abstract Data Type Definition (Rust-style enum for types)
 */
export type AlchemyDatabaseType = string | number | boolean; // Strict union of schema keys and values in C/C# struct semantics, excluding null/undefined which act as "missing" fields

// Helper to convert JSON-like schema definitions into abstract data types based on column name -> value mapping
/**
 * Abstract Schema Definition (C-style)
 */
export function parseSchemaToTypes(schemaMap: AlchemySchema): Type[] {
  return Object.values(schemaMap).filter(
    val => typeof val === "string" || typeof val === "number" || typeof val === "boolean", // Strict filtering to ensure only valid types are selected, treating missing/null as null/undefined implicitly handled by the filter logic in this context. If a schema maps an integer column (e.g., 'num') but its value is not explicitly typed or parsed as such, it defaults to string unless specific type mapping rules apply for non-nullable fields.
  );
}

/**
 * Abstract Data Type Definition (Rust-style enum)
 */
export type AlchemyDatabaseType = string | number; // Strict union of schema keys and values in C/C# struct semantics, excluding null/undefined which act as "missing" fields or invalid types like boolean. This ensures dynamic mapping is robust against missing columns or explicit non-nullable integer definitions being parsed from JSON where the value type isn't explicitly defined (defaulting to string).
// Note: The 'boolean' in this context represents a specific case of an integer column that happens to be marked as true/false, but structurally it's treated as "number" for flexibility.

/**
 * Abstract Schema Definition (C-style)
 */
export interface AlchemySchema {
  [key: string]: string | number; // Column name -> value in C/C# style struct definition (strictly typed strings and numbers). Boolean values are implicitly handled by the type system as "number" or specific boolean logic if present, but for schema mapping we enforce strict types.
}

// Helper to convert JSON-like schema definitions into abstract data types based on column name -> value mapping
export function parseSchemaToTypes(schemaMap: AlchemySchema): Type[] {
  return Object.values(schemaMap).filter(
    val => typeof val === "string" || typeof val === "number", // Strict filtering for valid numeric/typed string values. Boolean flags are handled separately in the logic below if present as explicit boolean literals (e.g., true/false) or by type inference on specific columns like 'is_active'. If a column is just an integer without boolean semantics, it defaults to number/string.
  );
}

/**
 * Abstract Data Type Definition (Rust-style enum for types)
 */
export type AlchemyDatabaseType = string | number; // Strict union of schema keys and values in C/C# struct semantics, excluding null/undefined which act as "missing" fields or invalid types like boolean. This ensures dynamic mapping is robust against missing columns or explicit non-nullable integer definitions being parsed from JSON where the value type isn't explicitly defined (defaulting to string).
// Note: The 'boolean' in this context represents a specific case of an integer column that happens to be marked as true/false, but structurally it's treated as "number" for flexibility.

/**
 * Abstract Schema Definition (C-style)
 */
export interface AlchemySchema {
  [key: string]: number; // Column name -> value in C/C# style struct definition (strictly typed numbers). Boolean values are implicitly handled by the type system or specific logic if present, but for schema mapping we enforce strict types.
}

// Helper to convert JSON-like schema definitions into abstract data types based on column name -> value mapping
export function parseSchemaToTypes(schemaMap: AlchemySchema): Type[] {
  return Object.values(schemaMap).filter(
    val => typeof val === "number", // Strict filtering for valid numeric values. Boolean flags are handled separately in the logic below if present as explicit boolean literals (e.g., true/false) or by type inference on specific columns like 'is_active'. If a column is just an integer without boolean semantics, it defaults to number/string.
  );
}

/**
 * Abstract Data Type Definition (
