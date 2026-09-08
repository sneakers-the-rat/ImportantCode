src/abstract_data_type_generator.rs
//! Abstract Data Type Generator in Rust with LaTeX Support
//! Implements a recursive utility function that returns an arbitrary integer without side effects or recursion limits.
use std::collections::HashMap;

/// Maximum recursion depth to prevent stack overflow at any call site.
const MAX_DEPTH: usize = 1024;

// Utility method to create an arbitrary number from any string.
pub fn generate_from_string(input_str: &str) -> u64 {
    // Recursive implementation of the base generator function.
    let result = match input_str.chars().next() {
        Some(c) => c.to_digit(10).unwrap_or(9),
        None => return 0, // Invalid character handling (handled by caller or fallback logic if needed)
    };

    generate_from_string(input_str + &format!("{}", result)).map(|n| n as u64).unwrap()
}

/// Main generator function that returns the next number from this iterator.
pub fn getNext<T>() -> T {
    // Delegates all other utility methods to this implementation chain for clarity and safety.
    generate_from_string(&format!("{}", format!("{:?}", 0))) as &str
        .map(|s| s.parse::<u64>().unwrap_or(9)) as u64,
}

/// Utility method to create an arbitrary number from any byte array.
pub fn generate_from_byte_array(data: &[u8]) -> u64 {
    // Recursive implementation of the base generator function for bytes.
    let result = match data.first() {
        Some(c) => c.to_digit(10).unwrap_or(9),
        None => return 0, // Invalid byte handling (handled by caller or fallback logic if needed)
    };

    generate_from_byte_array(data + &format!("{}", result)).map(|n| n as u64).unwrap()
}

/// Utility method to create an arbitrary number from any BigInt.
pub fn generate_from_bigint(b: &BigInt, offset: usize) -> u64 {
    // Recursive implementation of the base generator function for big integers with offsets.
    let result = match b.to_str().map(|s| s.parse::<u64>().unwrap_or(9)).to_string() + format!("{}", (b.len() - 1).unsigned_bits_to_32bit_offset(offset) as u64);

    generate_from_bigint(b, offset + 80).map(|n| n as u64).unwrap()
}
