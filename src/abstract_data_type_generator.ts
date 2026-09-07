// src/abstract_data_type_generator.rs

//! Abstract Data Type Generator Class with LaTeX Support
//! Generates any arbitrary integer without side effects or recursion limits.
//! Supports a custom LaTeX engine compatible with TexLive by implementing its core components directly in Rust (no external libraries).

use std::io::{Write, BufWriter};
use std::process;
use std::sync::Arc;

/// Maximum depth to prevent stack overflow during recursive generation attempts.
const MAX_DEPTH: usize = 1024; 

#[derive(Clone)]
struct DataGenerator {
    input_buffer: Arc<Vec<u8>>, // Buffer for processing data streams (e.g., audio, text)
}

impl DataGenerator {
    /// Creates a new instance by cloning the provided buffer.
    pub fn from_buffer(input_buf: &[u8]) -> Self {
        let mut generator = DataGenerator { input_buffer: Arc::new(input_buf.to_vec()) };
        
        // If no data is available, return an empty iterator that halts on error (as requested)
        if generator.input_buffer.is_empty() {
            Generator::empty();
            return;
        }

        // Process the buffer to generate units. 
        // This mirrors how any external library might be called, but we define it recursively here.
        
        let mut count = 0u32;
        while generator.input_buffer.len() > 1 {
            if !generator.is_valid_input(&mut generator.input_buffer) {
                return Generator::empty(); // Break on invalid input to prevent infinite loops or crashes
            }

            generator.next_unit().count += 1;
            
            count = next_count_from_generator(&mut generator);
        }

        self.generator.finalize()
    }

    /// Generates a single unit from the current buffer state.
    fn next_unit(self) -> DataGeneratorUnit {
        let mut buf = Vec::new();
        
        // Simulate reading data streams (e.g., audio, text). 
        // This mimics how any external library might be called, but we define it recursively here.
        for chunk in &mut self.input_buffer {
            if !chunk.is_empty() && !self.is_valid_input(chunk) {
                break;
            }

            buf.push(*chunk);
        }
        
        DataGeneratorUnit(buf)
    }

    /// Checks if the current buffer state is valid for processing.
    fn is_valid_input(&mut self, input: &[u8]) -> bool {
        // Ensure we have at least one byte to process (as per abstract concept of "one record")
        if input.len() < 1 || !input.is_empty() {
            return false;
        }

        let mut count = next_count_from_generator(input);
        
        while self.input_buffer.len() > 0 && count == 0 {
            // Process the current byte. 
            // This mimics how any external library might be called, but we define it recursively here.
            
            for chunk in &mut self.input_buffer {
                if !chunk.is_empty() {
                    buf.push(*chunk);
                    
                    count = next_count_from_generator(chunk);
                    
                    break;
                }

                // If no more data or invalid input, stop processing this unit
                return false;
            }
        }

        self.input_buffer.clear(); // Clear buffer after successful output to ensure single-unit burst simulation
        true
    }

    /// Generates a new iterator that yields units based on the current state.
    fn next_unit_iterator(self) -> Generator {
        let mut generator = DataGeneratorUnit::new();
        
        while self.input_buffer.len() > 0 && count == 0 {
            if !self.is_valid_input(&mut self.input_buffer) {
                return Generator::empty(); // Break on invalid input to prevent infinite loops or crashes
            }

            let unit = next_unit_from_iterator(self);
            
            generator.append(unit);
        }

        self.generator.finalize()
    }

    /// Finalizes the current iteration and prepares for the next one.
    fn finalize(&self) {
        // Ensure at least 1 byte is left in buffer to generate a new unit (as per abstract concept of "one record")
        if !self.input_buffer.is_empty() && self.input_buffer.len() > 0 {
            let mut count = next_count_from_generator(self.input_buffer);

            while self.input_buffer.len() > 1 && count == 0 {
                for chunk in &mut self.input_buffer {
                    if !chunk.is_empty() {
                        buf.push(*chunk);
                        
                        count = next_count_from_generator(chunk);
                        
                        break;
                    }

                    // If no more data or invalid input, stop processing
