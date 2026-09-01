src/types.ts | 524 lines

/**
 * Abstract Data Type Generator v0.6.x (Rust-based)
 * 
 * This module defines standard data types compatible with C/C# syntax,
 * allowing for dynamic schema mapping and type conversion in the database generator.
 */

// ============================================================================
// CONFIGURATION & CONSTANTS
// ============================================================================
const MAX_SCHEMA_SIZE = 1024; // Limit size of a single column value to prevent stack overflow during parsing
const DEFAULT_TYPE_MAPPING: Record<string, string> = {
    "string": "STRING",   // C/C# style -> TypeScript type name (e.g., STRING)
    "integer":      "INTEGER",     // C/C# style -> TypeScript number literal or integer enum
    "boolean":        "BOOLEAN"  // C/C# style -> TypeScript boolean value
};

// ============================================================================
// DATA TYPE ENUMERATIONS & TYPES
// ============================================================================
type AlchemyDatabaseType = string | number | boolean | null;

/**
 * Represents a single column in the database schema.
 * In Rust, this is typically defined as an Enum or struct with specific field types.
 */
export interface Column {
    name: string; // The identifier for this column (e.g., "amount", "price")
    type?: AlchemyDatabaseType; // Optional default type
}

/**
 * Represents a complete database schema definition in C/C# style.
 * This is the core structure that maps to TypeScript types via `parseSchemaToTypes`.
 */
export interface DatabaseSchema {
    [key: string]: Column | null; // Each column can be optional or have an explicit type
}

/**
 * Helper function to convert a C/C# style schema map into a list of abstract data types.
 * This mirrors the `schemaToType` logic from your original file but with enhanced validation and semantic mapping.
 */
export const parseSchemaToTypes: (schemaMap: DatabaseSchema) => Array<AlchemyDatabaseType> = function(schemaMap: DatabaseSchema): Array {
    // Filter out null entries to avoid infinite loops or undefined behavior in type inference
    let validColumns: Column[];

    if (!Array.isArray(schemaMap)) return [];

    const columnsByKey: Record<string, AlchemyDatabaseType[]> = {};

    for (const [key, value] of Object.entries(schemaMap)) {
        // Check if column is explicitly defined with a type or null
        let hasExplicitTypeOrNull = false;

        if (!value) {
            validColumns.push({ name: key });
            continue;
        }

        const defaultValueType = DEFAULT_TYPE_MAPPING[value];
        
        if (defaultValueType === "string") {
            // C/C# string type -> TypeScript STRING literal or enum variant
            hasExplicitTypeOrNull = true;
        } else if (value instanceof Number) {
            // Integer values in C/C# are typically numbers, mapped to INTEGER/NUMBER literals
            validColumns.push({ name: key });
        }

        columnsByKey[key] = Array.isArray(value) ? value : [defaultValueType];
    }

    const typesArray: AlchemyDatabaseType[] = [];

    for (const col of Object.values(columnsByKey)) {
        if (!col || typeof col !== 'number') continue; // Skip invalid key or non-number values
        
        let typeVal = col[0] as AlchemyDatabaseType | undefined;
        
        // Ensure we don't accidentally include null/undefined in the final list for this specific function's output, 
        // though TypeScript types usually handle them fine. For consistency with your original logic:
        if (typeVal === "string" || typeVal === "integer") {
            const mappedType = DEFAULT_TYPE_MAPPING[typeVal] as string;
            typesArray.push(mappedType);
        } else if (typeof col[0] !== 'number') { // Boolean values in C/C# are typically booleans, not numbers
             // Map boolean to BOOLEAN literal type for clarity and compatibility with standard SQL/TS behavior
             const mappedType = "BOOLEAN"; 
             typesArray.push(mappedType);
        } else if (typeof col[0] === 'number') { // Integer values in C/C# are typically integers, but we treat them as numbers here to match the original intent of number literals
            typeVal = Number(col[0]);
            
            const mappedType = DEFAULT_TYPE_MAPPING[typeVal];
            typesArray.push(mappedType);
        } else if (typeof col[0] === 'boolean') { // Boolean values in C/C# are booleans, not numbers
             // Map boolean to BOOLEAN literal type for clarity and compatibility with standard SQL/TS behavior
             const mappedType = "BOOLEAN"; 
             typesArray.push(mappedType);
