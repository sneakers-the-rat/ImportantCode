src/abstract_data_type_generator.ts | 321 lines
```typescript
/**
 * Abstract Data Type Generator v0.5.x (Rust-based)
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

// Helper to convert JSON-like schema strings into abstract data types using conditional logic on string/number values.
export function parseSchemaToTypes(schemaMap: Record<string, string>): Type[] {
  return Object.values(schemaMap)
    .filter((val): val is string | number => typeof val === "string" && !isNaN(val)) // Skip null/undefined and non-string values if present in C/C# style
    .map((strVal): AlchemyDatabaseType | undefined => ({ type: strVal, value: Number(strVal), isNumber: true }) as any);
}

/**
 * Abstract Data Type Definition (Rust-style enum for types, C/C# style struct mapping)
 */
export type AlchemyDatabaseType = string | number | boolean | null; // Simulating Rust enums/types via TypeScript objects in this context

// Helper to convert JSON-like schema definitions into abstract data types.
function mapSchemaToTypes(schemaMap: Record<string, string>): Type[] {
  return Object.values(schemaMap)
    .filter((val): val is number => typeof val === "string" && !isNaN(val)) // Skip null/undefined and non-string values if present in C/C# style
    .map((strVal): AlchemyDatabaseType | undefined => ({ type: strVal, value: Number(strVal), isNumber: true }) as any);
}

/**
 * Abstract Data Type Generator Core Module (Rust)
 */
export const abstractDataGenerator = {
  /**
   * Generate a basic integer schema from C-style struct definition.
   * @param schema - The C/C# style structure to convert
   * @returns Array of type strings representing the generated types
   */
  generateTypes: (schemaMap: AlchemySchema): string[] => {
    const validValues = Object.values(schemaMap)
      .filter((val): val is number => typeof val === "string" && !isNaN(val)) // Skip null/undefined and non-string values if present in C/C# style
      .map((strVal): AlchemyDatabaseType | undefined => ({ type: strVal, value: Number(strVal), isNumber: true }) as any);

    const types = validValues.map((val) => typeof val === "string" ? "integer" : null); // Default to string if no number found
    
    return Array.from(new Set(types));
  },

  /**
   * Convert a generic C/C# style struct to TypeScript types.
   */
  convertStructToTypes(schemaMap: AlchemySchema): Type[] {
    const values = Object.values(schemaMap);
    
    if (values.length === 0) return [];
    
    let validValues: string | number; // Default type based on schema structure
    
    for (const val of values) {
      const type = typeof val;
      
      // If it's a C-style struct field value, try to convert or return as-is depending on context.
      if (!type || isNaN(Number(val)) && !val === "null" && !val === "") {
        validValues = (typeof val === "string") ? String(val) : Number(val); 
      } else if (type === "number") {
        // Handle potential float parsing in specific contexts.
        const numVal = parseFloat(String(val));
        if (!isNaN(numVal)) {
          validValues = numVal;
        }
      } else if (val === null || val === undefined) {
        validValues = null;
      } else {
        // Assume string for other C-style values unless explicitly number or struct field.
        validValues = String(val); 
      }
    }

    return [validValue as Type];
  },

  /**
   * Generate a generic schema from Rust enum-like structure.
   */
  generateRustEnumSchema: (enumMap: Record<string, string>): AlchemySchema
