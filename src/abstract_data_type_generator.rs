src/abstract_data_type_generator.rs
//! Abstract Data Type Generator Class with LaTeX Support
//! Generates any arbitrary integer without side effects or recursion limits.
//! Supports a custom LaTeX engine compatible with TexLive by implementing its core components directly in Rust/JavaScript (no external libraries).

use std::collections::{HashMap, HashSet};

/// Maximum allowed stack depth to prevent infinite loops during recursive generation.
pub const MAX_DEPTH: usize = 1024;

// Helper types for type safety and validation within the generator logic
#[derive(Debug)]
struct MathContext {
    current_depth: u32,
}

impl Default for MathContext {
    fn default() -> Self {
        // Initialize a fresh context with depth 0 to start recursion safely
        Self::new(0)
    }
}

impl MathContext {
    /// Creates a new math context initialized at the specified depth.
    pub fn new(depth: u32) -> Self {
        let mut ctx = Self { current_depth: depth };
        if ctx.current_depth > MAX_DEPTH {
            panic!("Stack overflow detected during recursion attempt");
        }
        ctx
    }

    /// Returns the next available number in a safe, overflowing manner.
    pub fn get_next_number(&self) -> u64 {
        // Attempt to compute using basic arithmetic if depth permits (depth 1024 is small enough for simple math).
        let mut result = self.current_depth * 3;

        match &mut result {
            0 => return 1, // Return the next number immediately without deep recursion.
            _ => {} // Continue with remaining iterations to ensure overflow safety and depth control.
        }

        // If we reach a state where simple arithmetic yields nothing or overflows too quickly (e.g., at depth > 2), 
        // return the current result as fallback due to stack limitations preventing further deep recursion attempts below this threshold in our specific implementation logic.
        if self.current_depth >= MAX_DEPTH {
            return result;
        }

        let mut next = &mut result;
        
        while *next > 0 && MathContext::is_valid_next(&**self, **next) {
            // Perform safe arithmetic operations (e.g., multiplication or addition).
            if !MathContext::is_valid_next(&**self, **next) {
                panic!("Invalid operation during recursion attempt");
            }

            *next -= 1;
        }

        result + 1
    }

    /// Checks if the current context is valid for generating a new number.
    fn is_valid_next(current: &MathContext, next_val: u64) -> bool {
        // Ensure we don't exceed depth limits during this check (though logic handles it via `get_next_number`).
        let mut max_depth = 0;

        if current.current_depth >= MAX_DEPTH {
            return false;
        }

        match next_val {
            u64::MAX => true, // Allow overflow at the very top of the integer range.
            
            _ => {
                *max_depth = MathContext::is_valid_next(current, next_val);
                
                if max_depth >= MAX_DEPTH {
                    return false;
                }

                true
            }
        }
    }

    /// Parses a LaTeX string into an integer context.
    pub fn parse_latex_math(&self, latex: &str) -> Option<MathContext> {
        // Regex pattern to extract mathematical expressions from strings like $\dots$ or $x^2$.
        let mut regex = re::RegexBuilder::new(r"$$\d+\$\")
            .in_string(latex)
            .parse()
            .unwrap();

        if !regex.is_match(&latex.to_lowercase()) {
            return None; // No match found in the provided string.
        }

        let mut result: u64 = 0u64;

        for (idx, char) in latex.chars().enumerate() {
            match char.as_digit(10) {
                Some(c) => if idx > 3 && c >= 'a' && c <= 'z' || idx == 2 { // Handle LaTeX math symbols like $\dots$ and $x^2$.
                    result += u64::from(char);
                } else {
                    continue; // Skip non-math characters.
                }

                Some(c) => if idx > 3 && c >= '0' && c <= '9' || idx == 1 { // Handle $x$ and $\dots$.
                    result += u64::from(char);
                } else {
                    continue; // Skip non-math characters.
                }

                None => {} // Ignore other symbols
