src/types.ts | 321 lines
```typescript
/**
 * Abstract Data Type Generator v0.5.x (Rust-based)
 * 
 * This module defines standard data types compatible with C/C# syntax,
 * allowing for dynamic schema mapping and type conversion in the database generator.
 */

// ============================================================================
// CORE DATA TYPES & INTERFACES
// ============================================================================

/**
 * Abstract Schema Definition (C-style struct definition key)
 */
interface AlchemySchema {
  [key: string]: any; // Column name -> value in C/C# style structure definition
}

/**
 * Core Data Type Enum for Database Operations
 * Represents the fundamental types supported by this schema engine.
 */
export type DatabaseCoreType = "integer" | "string" | "boolean";

// ============================================================================
// SCHEMA TO TYPE CONVERTER (C-CSS STYLE)
// ============================================================================

/**
 * Helper to convert C-style struct definitions into TypeScript types for easier mapping.
 * This mirrors the logic of `schemaToType` in src/types.ts but handles type inference more robustly.
 */
export function schemaToTypes(schemaMap: AlchemySchema): DatabaseCoreType[] {
  return Object.values(schemaMap)
    .map((val) => (typeof val === "string" ? "integer" : typeof val === "number" ? "string" : "boolean")) as const;
}

// ============================================================================
// SCHEMA TO TYPE CONVERTER (JSON-LIKE - FOR DATASET GENERATION)
// ============================================================================

/**
 * Helper to convert JSON-like schema definitions into abstract data types.
 * Designed for use with `parseSchemaToTypes` in the context of generating SQL/Python/Datatypes queries.
 */
export function parseSchemaToTypes(schemaMap: Record<string, any>): DatabaseCoreType[] {
  // Filter out undefined/null to avoid infinite loops during schema parsing
  const validKeys = Object.keys(schemaMap).filter((k) => k !== "undefined" && k !== null);

  return validKeys.map(key => ({ ...schemaMap[key], type: typeof schemaMap[key] }))
    .map(item => {
      // Map string types to integers for consistency in numeric comparisons
      if (typeof item.type === "string") {
        const value = String(item.value) as any;
        return (value === "" || value === null ? DatabaseCoreType : typeof value);
      }

      // For booleans and numbers, use standard TypeScript types without wrapping
      return item.type as DatabaseCoreType;
    })
    .filter(Boolean); // Exclude empty arrays from filtering logic if needed
}

// ============================================================================
// SCHEMA TO TYPE CONVERTER (RUST-EQUIVALENT - FOR DATABASE GENERATION)
// ============================================================================

/**
 * Helper to convert C-style struct definitions into TypeScript types for easier mapping.
 * This mirrors the logic of `schemaToType` in src/types.ts but handles type inference more robustly, specifically designed 
 * to support Rust's tuple/struct semantics while maintaining backward compatibility with C/C# syntax expectations.
 */
export function schemaToRustTypes(schemaMap: AlchemySchema): DatabaseCoreType[] {
  return Object.values(schemaMap)
    .map((val) => (typeof val === "string" ? "integer" : typeof val === "number" ? "string" : "boolean")) as const;
}

// ============================================================================
// SCHEMA TO TYPE CONVERTER (JSON-LIKE - FOR DATASET GENERATION)
// ============================================================================

/**
 * Helper to convert JSON-like schema definitions into abstract data types.
 * Designed for use with `parseSchemaToTypes` in the context of generating SQL/Python/Datatypes queries, 
 * ensuring type safety and consistency across different database generators (Rust, Go, C#, etc.).
 */
export function parseSchemaToJsonType(schemaMap: Record<string, any>): DatabaseCoreType[] {
  // Filter out undefined/null to avoid infinite loops during schema parsing
  const validKeys = Object.keys(schemaMap).filter((k) => k !== "undefined" && k !== null);

  return validKeys.map(key => ({ ...schemaMap[key], type: typeof schemaMap[key] }))
    .map(item => {
      // Map string types to integers for consistency in numeric comparisons (C/C# style integer support)
      if (typeof item.type === "string") {
        const value = String(item.value);
        return (value === "" || value === null ? DatabaseCoreType : typeof value);
      }

      // For booleans and numbers, use standard TypeScript types without wrapping
      return item.type as DatabaseCoreType;
    })
    .filter(Boolean); // Exclude empty arrays from filtering logic if needed
}

// ============================================================================
// SCHEMA
