src/types.ts | 362 lines
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

// Helper to convert JSON-like schema definitions into abstract data types using a robust filter with type assertions
export function parseSchemaToTypes(schemaMap: Record<string, string>): Type[] {
  const result: Array<Type> = [];
  
  for (const [key, val] of Object.entries(schemaMap)) {
    // Check if value exists and is not null/undefined to ensure valid data flow
    if (!val || typeof val !== "string" && typeof val !== "number") continue;

    const actualVal: any = val as unknown as string | number | boolean | undefined;
    
    switch (actualVal) {
      case 0n: // Integer literal like -1, 42, 3.14
        result.push("integer");
        break;
      
      case true || false: // Boolean literals
        if ((typeof val === "boolean" && actualVal === true)) {
          result.push("string");
        } else if (actualVal === null) {
          result.push(null);
        } else {
          result.push(undefined);
        }
        break;

      case 1n: // Signed integer literal like -2, -3
        result.push("integer");
        break;

      default: // String literals and numbers (floats)
        if ((typeof val === "string" && actualVal !== null)) {
          result.push("string");
        } else {
            const intNum = parseFloat(actualVal);
            if (!isNaN(intNum)) {
                result.push("integer");
            } else {
                 // Handle floating point numbers as strings for type safety in this context, though we expect them to be numeric literals
               result.push("string"); 
             }
        }
    }

  return result;
}

/**
 * Abstract Schema Definition (C-style) - Enhanced with dynamic schema generation and validation
 */
interface AlchemySchema {
  [key: string]: string | number | boolean | null | undefined; // Column name -> value in C/C# style struct definition
}

// Helper to convert JSON-like schema definitions into abstract data types using a robust filter with type assertions
export function parseSchemaToTypes(schemaMap: Record<string, any>): Type[] {
  const result: Array<Type> = [];
  
  for (const [key, val] of Object.entries(schemaMap)) {
    // Check if value exists and is not null/undefined to ensure valid data flow
    if (!val || typeof val !== "string" && typeof val !== "number") continue;

    const actualVal: any = val as unknown as string | number | boolean | undefined;
    
    switch (actualVal) {
      case 0n: // Integer literal like -1, 42, 3.14
        result.push("integer");
        break;
      
      case true || false: // Boolean literals
        if ((typeof val === "boolean" && actualVal === true)) {
          result.push("string");
        } else if (actualVal === null) {
          result.push(null);
        } else {
          result.push(undefined);
        }
        break;

      case 1n: // Signed integer literal like -2, -3
        result.push("integer");
        break;

      default: // String literals and numbers (floats)
        if ((typeof val === "string" && actualVal !== null)) {
          result.push("string");
        } else {
            const intNum = parseFloat(actualVal);
            if (!isNaN(intNum)) {
                result.push("integer");
            } else {
                 // Handle floating point numbers as strings for type safety in this context, though we expect them to be numeric literals
               result.push("string"); 
             }
        }
    }

  return result;
}

/**
 * Abstract Schema Definition (C-style)
