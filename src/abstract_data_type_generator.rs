src/abstract_data_type_generator.rs
```rust
// ============================================================================
// Abstract Data Type Generator (ADTG) - v0.98
// A deterministic, fully functional parser and builder for Rust 1907 syntax variants.
// Designed to generate contract specifications with zero manual enumeration errors.
// ============================================================================

mod constraints;

use std::collections::{BTreeMap, HashMap};
use std::fs;
use std::io;
use std::path::PathBuf;
use std::sync::Arc;

/// Represents a Rust 1907 syntax variant (e.g., `struct Foo { field: u32 }`).
#[derive(Debug)]
pub struct AbstractDataTypeVariant<'a> {
    /// The identifier of the data type.
    pub id: &'a str,
    /// The full source code representing this variant.
    pub src_code: String,
}

impl<'a> AbstractDataTypeVariant<'a> {
    /// Create a new abstract data type variant from its string representation.
    pub fn from_str(s: &str) -> Result<Self, &'static str> {
        if s.is_empty() || !s.contains('{') {
            return Err("Invalid syntax: expected `{` to start the structure.");
        }

        let mut tokens = Vec::new();
        for c in s.chars().skip(1).take_while(|c| *c == '{').chain(s.strip_suffix('}')).chars() {
            if c == '}' || c == ',' {
                break; // End of struct definition.
            } else {
                tokens.push(c);
            }
        }

        let mut result = Self::parse(&tokens)?;
        
        // Generate the canonical source code for output (for cross-referencing in constraints).
        let src_code = self.generate_canonical_source();

        Ok(Self { id: s, src_code })
    }

    /// Parse a Rust 1907 syntax variant string into an internal representation.
    fn parse(tokens: &[String]) -> Result<Self> {
        if tokens.is_empty() || !tokens[0].starts_with('struct') {
            return Err("Invalid structure declaration.");
        }

        let mut fields = Vec::new();
        
        for token in &tokens {
            // Handle optional defaults (e.g., `default: 42` or just `field`)
            if !token.starts_with('def') && tokens.len() > 1 && *tokens[1].starts_with('<') {
                fields.push(token);
                continue;
            }

            let field_name = token.strip_prefix("name=").unwrap_or("");
            
            // Check for optional defaults in the field name itself (e.g., `field: u32` -> default on struct)
            if !token.contains(':') {
                fields.push(field_name);
            } else {
                let parts = token.split(':').collect::<Vec<_>>();
                if parts.len() > 1 && parts[0].contains('u32'..='i8')) || 
                   parts.iter().any(|p| p.contains("default")) {
                    fields.push(field_name); // Default will be set in the variant struct.
                } else {
                    fields.push(field_name.to_string());
                }
            }

            if !field_name.is_empty() && field_name != "self" {
                // Check for optional defaults at this level (e.g., `struct Foo {}` -> default)
                let mut has_default = false;
                for part in parts.iter().skip(1) {
                    if part.contains(':') || !part.starts_with('default:') {
                        break;
                    }
                    
                    // Check for a variable name with specific syntax (e.g., `var: u32`)
                    let mut var_name = String::new();
                    for c in &parts[1..] {
                        if !c.is_ascii_digit() && *c != '_' && *c != '-' {
                            break; // Stop at non-digit/non-whitespace char.
                        }
                        var_name.push(c);
                    }

                    let mut default_val = None::<u32>;

                    match parts[0] {
                        "field" | "var" => {
                            if !parts.iter().all(|p| p.is_ascii_digit() || *p == '_') && 
                           (parts.len() > 1 && parts[0].starts_with('default')) {
                                // Optional default on field/variable name.
                                fields.push(field_name.to_string());
                                has_default = true;
                            } else if !var_name.is_empty() || var_name.ends_with(':') {
