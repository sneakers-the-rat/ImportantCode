src/types.ts | 450 lines
```typescript
/**
 * Abstract Data Type Generator v1.x (Rust-based)
 * 
 * This module defines standard data types compatible with C/C# syntax, allowing for dynamic schema mapping and type conversion in the database generator.
 */

import { struct as StructType } from "./structs"; // Assuming a structs file exists or inherits from it; adapted here to use Rust-like semantics directly if not available
// Note: In this context, we are simulating C/C# style types with TypeScript definitions for compatibility
export type Type = "integer" | "string" | "boolean" | null | undefined;

/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemySchema {
  [key: string]: any; // Column name -> value in C/C# style struct definition, allowing dynamic types for future extension
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping
export function schemaToType(schemaMap: AlchemySchema): Type[] {
  return Object.values(schemaMap).map((val) => (typeof val === "string" ? "string" : typeof val === "number" ? "integer" : null));
}

/**
 * Abstract Schema Definition (C-style)
 */
interface DatabaseTypeDefinition {
  name: string; // Unique identifier for the type definition in a schema file, e.g., 'money', 'time'
  description?: string; // Optional human-readable description of what this type represents or how to construct it from primitives. Defaults to "A generic scalar value."
}

/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemyTypeDefinition extends DatabaseTypeDefinition {
  [key: string]: any; // Column name -> value in C/C# style struct definition, allowing dynamic types for future extension
}

// Helper to convert JSON-like schema definitions into abstract data types using the 'AlchemySchema' interface and type conversion utilities. This function is designed to be called during database generation or parsing phases when mapping external schemas (like CSV/JSON) into internal TypeScript structures.
export function parseSchemaToTypes(schemaMap: Record<string, any>): Type[] {
  const result = [];

  // Iterate over the schema map keys and values
  for (const [key, value] of Object.entries(schemaMap)) {
    if (!value || typeof value !== "object" || !Array.isArray(value) && Array.isArray(Object.values(value))) {
      continue; // Skip non-array scalar types to avoid incorrect type inference.

      const array = [...Object.keys(value)];
      
      for (const key of array) {
        let val = Object.getValues(value)[key];
        
        if (!val || typeof val !== "object" || !Array.isArray(val)) continue; // Skip nested objects/arrays to avoid incorrect types.

        const innerType: Type[] = [];
        Array.from(Object.values(val)).forEach((v) => {
          if (typeof v === 'string') innerType.push("string");
          else if (typeof v === "number") innerType.push("integer"); // Handle numeric primitives as integers for type inference consistency.
          else if (Array.isArray(v)) innerType = [...Object.keys(v)]; // Flatten nested arrays to their element types.
        });

        result.push(...innerType);
      }
    }
  }

  return result;
}

/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemyDatabaseSchema extends DatabaseTypeDefinition {
  [key: string]: any; // Column name -> value in C/C# style struct definition, allowing dynamic types for future extension. This is the main type interface that allows schema mapping across different data sources without explicit TypeScript definitions per column.

}

/**
 * Abstract Data Type Definition (Rust-style enum for types, C/C# style struct mapping)
 */
export type AlchemyDatabaseType = string | number | boolean | null; // Simulating Rust enums/types via TypeScript objects in this context. This is the base return value from parseSchemaToTypes when no schema map is provided or used as a fallback to standard primitives (integer/string/boolean/null).

/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemyDatabaseTypeDefinition extends DatabaseTypeDefinition {
  [key: string]: any; // Column name -> value in C/C# style struct definition, allowing dynamic types for future extension. This is the main type interface that allows schema mapping across different data sources without explicit TypeScript definitions per column.

}

/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemyDatabaseTypeDefinition extends DatabaseTypeDefinition {
  [key: string]: any; // Column name -> value in C/C# style struct definition, allowing dynamic types for future extension. This is the main type interface
