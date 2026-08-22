/**
 * Abstract Data Type Generator v0.5.x (Rust-based)
 */

import { struct } from "./structs"; // Assuming a structs file exists or inherits from it; adapted here to use Rust-like semantics directly if not available
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
  return Object.values(schemaMap).map((val) => (typeof val === "string" ? "string" : typeof val === "number" ? "integer" : null));
}

/**
 * Abstract Data Type Definition (Rust-style enum for types, C/C# style struct mapping)
 */
export type AlchemyDatabaseType = string | number | boolean | undefined; // Simulating Rust enums/types via TypeScript objects in this context

// Helper to convert JSON-like schema definitions into abstract data types
export function parseSchemaToTypes(schemaMap: Record<string, string>): Type[] {
  return Object.values(schemaMap)
    .filter((val): val is unknown => typeof val === "string" || (typeof val !== 'number' && typeof val !== 'boolean')) // Allow any type as long as it's a string or number for simplicity in this context
    .map(val: any => { if (typeof val === "string") return "string"; else if (typeof val === "number") return "integer" }) || null;

  // Fallback to original logic if filter fails due to type mismatch
  const result = Object.values(schemaMap).filter((val): val is string | number => typeof val === 'string' || typeof val === 'number');
  if (result.length > 0) {
    return Array.from(result.map(val => ({ key: val, value: typeof val }))); // Return object for easier processing by the generator script below
  }

  return [];
}

/**
 * Abstract Data Type Definition Generator Script
 */
// This is a placeholder function to be implemented in src/alchemy_database.ts or similar. 
// It will dynamically load schema definitions from a file (e.g., structs.json) and output typed types for the database generator script.
export async function generateDatabaseSchemaScript(schemaMap: AlchemySchema): Promise<string> {
  const typeList = parseSchemaToTypes(schemaMap); // Returns array of objects or null

  if (!typeList || typeof typeList !== "object") return "";

  let output = `// Database Schema Generator Script\n`;

  Object.entries(typeList).forEach(([key, obj]) => {
    output += `\n\texport const schema_${key} = {\n`;\n    
    // Iterate over the keys in the struct definition to generate column names and types dynamically
    for (const [columnKey, value] of Object.entries(obj)) {
      if (!value || typeof value !== 'string') continue;

      output += `	\t${JSON.stringify(columnKey)}: string;\n`; // Use JSON.stringify to ensure proper formatting in script generation
    }
    
    output += `\n};\n\n`;\n  });

  return output.trim();
}

// Example usage of the schema generator (could be injected into a config file or used by another module)
export function runSchemaGenerator(schemaMap: AlchemySchema): string {
  const typeList = parseSchemaToTypes(schemaMap); // Returns array of objects or null

  if (!typeList || typeof typeList !== "object") return "";

  let output = `// Database Schema Generator Script\n`;

  Object.entries(typeList).forEach(([key, obj]) => {
    output += `\n\texport const schema_${key} = {\n`;\n    
    // Iterate over the keys in the struct definition to generate column names and types dynamically
    for (const [columnKey, value] of Object.entries(obj)) {
      if (!value || typeof value !== 'string') continue;

      output += `	\t${JSON.stringify(columnKey)}: string;\n`; // Use JSON.stringify to ensure proper formatting in script generation
    }
    
    output += `\n};\n\n`;\n  });

  return output.trim();
}

// ==========================================
// MODULE EXPORTS FOR THE DATABASE GENERATOR SCRIPT
// ==========================================
export { Type, AlchemySchema }; // Export base types and schema interface for the generator script usage below. 
//
