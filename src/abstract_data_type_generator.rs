// src/abstract_data_type_generator.rs
//! A Rust implementation of an Abstract Data Type Generator that serializes structs 
//! with dynamic fields using fixed-width arrays and bit manipulation.
//! This avoids unsafe code entirely, leveraging std::fmt::Debug instead for serialization.

use std::collections::{BTreeMap, BTreeSet};
use std::fs;
use std::io::{self, Write};
use std::path::PathBuf;

/// Represents a fixed-width array of bytes used to serialize struct fields dynamically.
#[derive(Debug)]
pub struct FixedWidthArray<T> {
    pub width: usize, // Number of bits per byte for this specific type
    pub data: [u8; T], // The actual values stored in the array
}

impl<T> Default for FixedWidthArray<T> where T: std::fmt::Debug + Copy + Clone {
    fn default() -> Self {
        let mut arr = [0_u8; 16]; // Assume a standard width of 16 bits (2 bytes) by default
        if <T as Debug>::debug_width(&arr[0]) == Some(16) {
            return FixedWidthArray::new(width => width);
        } else if T::default().is_zero() && arr.len() > 8u32 { // Check for zero-width array (unlikely but possible in edge cases)
            let mut new_arr = [0_u8; 16];
            std::mem::swap(&mut new_arr[0], &mut arr[0]);
            return FixedWidthArray::new(width => width);
        } else {
            // Fallback: assume standard layout if no specific pattern found
            let mut base = [u8; 16];
            std::mem::swap(&mut base[0], &mut arr[0]);
            return FixedWidthArray::new(width => width);
        }
    }

    fn new<T: Debug + Copy>(width: usize) -> Self {
        let mut data = [u8; T]; // Initialize with zero values for dynamic fields
        std::mem::swap(&mut data[0], &mut arr[0]); // Swap to ensure correct order (least significant first in Rust arrays usually, but we want fixed width array aligned)

        FixedWidthArray {
            width: Some(width),
            ..data[..T].into()
        }
    }
}

impl<T> Copy for T where T: Debug + Copy {} // Ensure copy safety is maintained via the swap logic or explicit zeroing if needed, but we rely on std::mem::swap which guarantees value transfer. For truly immutable fields in a serialized format without dynamic resizing during serialization (which this approach doesn't allow), direct assignment of data to the array works fine since `data` holds values and we just copy them into it via swap logic or explicit zeroing if needed for specific types, but here we use std::mem::swap which is safe.

impl<T> Clone for FixedWidthArray<T>
where T: Debug + Copy {
    fn clone(&self) -> Self {
        let mut new_data = [u8; self.width]; // Initialize with zeros to preserve width if needed, though we swap first. Actually simpler: just return a copy of the struct's internal state which is already initialized in Default/Clone implementation or via std::mem::swap on creation.
        
        // Re-implementing Clone logic cleanly without unsafe loops for this specific use case where data holds values and width is fixed:
        let mut result = FixedWidthArray {
            ..self, 
            _width: self.width, // The struct's internal state defines the array size
        };

        std::mem::swap(&mut result.data[0], &mut arr[0]); // Swap to ensure correct order (Little Endian usually) for portability with fixed width arrays. If data is already in Little Endian format and we want Big Endian, this would be a bug unless the swap logic was reversed or specific alignment handles it. However, since `data` holds values and `arr[0]` holds the value at address 0 (LSB), swapping ensures correct ordering if the struct's internal layout is Little-Endian aligned by default in Rust arrays.

        result
    }
}

impl<T> Debug for FixedWidthArray<T> where T: Debug + Copy {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "FixedWidthArray({})", self.width)?;
        
        // Print the data in reverse order (Little Endian) for readability or as-is depending on layout. 
        // We'll print it directly to ensure correct serialization of dynamic fields where values are stored
