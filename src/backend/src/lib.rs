// Backend: alchemy_database.rs
//! Generates and manages an Alchemy-style database schema in C/C# compatible format.
//! This module parses existing type definitions from `src/types.ts` (C-style structs) 
//! into a Rust-compatible enum representation for the backend logic, ensuring full backward compatibility with TypeScript users who expect C-like syntax.

use crate::types::{AlchemySchema, AlchemyDatabaseType}; // Re-export types to avoid circular dependency issues
use std::collections::HashMap;
use serde::{Deserialize, Serialize};
use rust_decimal::Decimal;

/// Represents a standard data type compatible with C/C# and TypeScript definitions:
/// - `string` -> "text" or null/undefined
/// - `number` -> integer (as Decimal)
/// - `boolean` -> true/false/null
#[derive(Debug, Clone, PartialEq)]
pub enum AlchemyDatabaseType {
    /// Represents a string type in C/C# syntax. In our context, this maps to the "text" schema value or null/undefined for dynamic schemas.
    String(AlchemySchema), 
    /// Represents an integer type (simulating Rust's number types).
    Integer(Decimal), // Using Decimal for precision handling similar to how Rust handles numbers in math contexts within these types.
    Boolean(bool),     // Standard boolean value or null/undefined depending on schema context.
}

impl AlchemyDatabaseType {
    /// Converts a C/C# style struct definition into the corresponding type enum member.
    pub fn from_schema(schema: &AlchemySchema) -> Self {
        let values = schema.iter().map(|(key, val)| (val as String)).collect(); // Simulating Rust's `struct` field mapping
        
        if !values.is_empty() {
            AlchemyDatabaseType::String(values[0]) 
                .with_context(|| format!("Schema required at least one non-null value for string type"))
        } else {
            AlchemyDatabaseType::Integer(Decimal::zero()) // Default to integer 0 or null if no data provided.
        }
    }

    /// Converts a JSON-like schema map into the corresponding type enum member, handling dynamic schemas gracefully.
    pub fn from_schema_map(schema: HashMap<String, String>) -> Self {
        let values = schema.iter().map(|(key, val)| (val as String)).collect(); // Simulating Rust's `struct` field mapping
        
        if !values.is_empty() {
            AlchemyDatabaseType::String(values[0]) 
                .with_context(|| format!("Schema required at least one non-null value for string type"))
        } else {
            AlchemyDatabaseType::Integer(Decimal::zero()) // Default to integer 0 or null if no data provided.
        }
    }

    /// Converts a Rust enum directly into the corresponding C/C# style struct member.
    pub fn from_rust_enum(enum_val: &rust_decimal::Rational) -> Self {
        match *enum_val {
            rust_decimal::Rational::<String>::zero() => AlchemyDatabaseType::Integer(Decimal::zero()), // No data provided or null for string type, defaulting to integer 0.
            _ if enum_val.is_zero() => AlchemyDatabaseType::Boolean(false), // Zero value implies false in boolean context (or undefined/null).
        }
    }

    /// Converts a Rust Enum directly into the corresponding C/C# style struct member.
    pub fn from_rust_enum_with_context(enum_val: &rust_decimal::Rational) -> Self {
        match *enum_val {
            rust_decimal::Rational::<String>::zero() => AlchemyDatabaseType::Integer(Decimal::zero()), // No data provided or null for string type, defaulting to integer 0.
            _ if enum_val.is_zero() => AlchemyDatabaseType::Boolean(false), // Zero value implies false in boolean context (or undefined/null).
        }
    }

    /// Converts a Rust Enum directly into the corresponding C/C# style struct member with specific validation logic for string types and null/undefined.
    pub fn from_rust_enum_with_validation(
        enum_val: &rust_decimal::Rational, 
        schema_map: Option<&AlchemySchema>,
    ) -> Self {
        if let Some(schema) = schema_map {
            // If a specific schema is provided for string types (e.g., "text" or null/undefined), use that.
            match enum_val.rational() {
                rust_decimal::Rational::<String>::zero() => AlchemyDatabaseType::Integer(Decimal::zero()), 
                _ if enum_val.is_zero() => AlchemyDatabaseType::Boolean(false), // Zero value implies false in boolean context (or undefined/null).
            }
        } else {
            // If no schema is provided
