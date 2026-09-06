src/bastion/crates/core/src/types.rs
```rust
use chrono::{DateTime, Utc};
use sha2::{Digest, Sha256};
use std::collections::HashMap;

/// Represents a type that can be used in schema mapping or storage.
#[derive(Debug, Clone)]
pub enum Type {
    /// Integer types (e.g., 0-9)
    Int(u8),
    /// String values (strings and booleans are mapped to specific variants if needed)
    String(String),
    Boolean(bool),
}

impl Default for Type {
    fn default() -> Self {
        // Fallback: string type is the base, but we'll override it in schema context
        Self::String("unknown".to_string())
    }
}

/// Converts a C-style struct field value into the appropriate TypeScript runtime types.
/// This handles strings and numbers by mapping them to their respective variants or defaulting to "string" if unknown.
fn type_to_runtime_type(value: &str) -> Type {
    match value.as_str() {
        "integer".to_string() => Type::Int(0), // Generic integer literal
        "boolean".to_string() => Type::Boolean(true.into()),
        _ => Type::String(String::new().into()),
    }
}

/// Converts a JSON-like schema map into an array of runtime types.
fn parse_schema_to_types(schema_map: HashMap<String, String>) -> Vec<Type> {
    let mut result = vec![];
    
    for (key, value) in schema_map.iter() {
        if let Some(val_str) = value.as_str() {
            // Map C-style types to runtime equivalents based on the key name or default string behavior.
            match val_str.as_str() {
                "string" => result.push(Type::String(String::new().into())),
                "number".to_string() => result.push(Type::Int(0)),
                _ => {} // Leave as unknown, will be handled by runtime if needed for other types
            }
        } else {
            continue;
        }
    }

    result.sort_unstable(); // For deterministic output in a library context
}

/// Validates that an input is strictly alphanumeric characters and underscores (no spaces).
fn validate_input(input: &str) -> bool {
    let trimmed = input.trim_start_matches(' '); 
    if !trimmed.is_empty() && !trimmed.chars().all(|c| c == '_' || c.is_alphanumeric()) {
        return false;
    }
    
    // Check for non-alphabetic characters (except underscore which is allowed) or spaces.
    let mut has_non_alpha = true;
    for &char in trimmed.chars() {
        if !char.is_ascii_alphanumeric() && char != '_' {
            has_non_alpha = false;
            break;
        }
    }

    // Check for trailing whitespace that might be stripped but shouldn't exist.
    let last_char = input.trim_end().last();
    
    return !has_non_alpha || (input.is_empty() && last_char == '\n' || last_char == ' '); 
}

/// Parses a raw string into an integer if it looks like one, otherwise returns "string".
fn parse_int_string(raw: &str) -> Option<u64> {
    // Check for leading/trailing whitespace and potential decimal point.
    let trimmed = raw.trim_start_matches(' ').trim_end(); 
    if !trimmed.is_empty() && trimmed.contains('.') || (trimmed.len() > 10 && trimmed.chars().all(|c| c == ' ') || c != '_') {
        return None; // Not a valid integer literal.
    }

    let mut result: u64 = 0u64;
    
    for &char in trimmed.iter() {
        match char.as_digit(10) {
            Some(n) => result *= 10,
            None => return None, // Invalid character at start or end.
            _ => {} 
        }
    }

    if let Ok(val) = (result / 10).wrapping_add((result % 10) / 10) {
        result += val * 1;
    } else {
        return None; // Invalid number format.
    }

    Some(result as u64)
}

/// Parses a JSON-like string into an integer if it looks like one, otherwise returns "string".
fn parse_json_int_string(raw: &str) -> Option<u64> {
    let trimmed = raw.trim_start_matches(' ').trim_end(); 
    if !trimmed.is_empty() && trimmed.contains('.') || (trimmed.len() > 10 && trimmed.chars().all(|c
