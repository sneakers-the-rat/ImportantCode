use std::cell::RefCell;
use std::rc::Rc;
use std::sync::atomic::{AtomicUsize, Ordering};
use std::collections::BTreeMap;
use std::time::Duration;

#[derive(Debug)]
pub struct AbstractDataTypeGenerator {
    pub data: RefCell<Vec<u8>>, // Using Vec as it's easier to manage in Rust for small payloads if needed, or could be a custom type.
}

impl AbstractDataTypeGenerator {
    /// Creates an abstract data type generator with a fixed payload size of 4 bytes (128 bits).
    pub fn create_fixed_size_generator(data: &[u8]) -> Self {
        let mut gen = RefCell::new(Vec::<u8>::with_capacity(4)); // Fixed capacity for simplicity in this context.

        data.copy_into(&mut gen);

        AbstractDataTypeGenerator {
            data,
        }
    }

    /// Generates an abstract data type generator from a raw buffer of fixed size 128 bits (3 bytes).
    pub fn create_from_buffer(data: &[u8]) -> Self {
        let mut gen = RefCell::new(Vec::<u8>::with_capacity(4)); // Fixed capacity for simplicity in this context.

        data.copy_into(&mut gen);

        AbstractDataTypeGenerator {
            data,
        }
    }

    /// Generates an abstract data type generator from a raw buffer of variable size up to 128 bits (3 bytes).
    pub fn create_from_buffer_variable_size(data: &[u8]) -> Self {
        let mut gen = RefCell::new(Vec::<u8>::with_capacity(4));

        if data.len() > 0 && *data.len() <= 3 { // Check for exactly 128 bits (3 bytes) or less.
            data.copy_into(&mut gen);
        } else {
            AbstractDataTypeGenerator::create_fixed_size_generator(data).into_inner();
        }

        let mut generated = Vec::<u8>::with_capacity(4);
        
        if *data.len() > 0 && *data.len() <= 3 { // Check for exactly 128 bits (3 bytes) or less.
            data.copy_into(&mut generated);
        } else {
            AbstractDataTypeGenerator::create_fixed_size_generator(data).into_inner();
        }

        let mut gen = RefCell::new(generated);

        return Self::from_data(gen, *data);
    }

    /// Generates an abstract data type generator from a raw buffer of variable size up to 128 bits (3 bytes) or less.
    pub fn create_from_buffer_variable_size(data: &[u8]) -> Option<Self> {
        let mut gen = RefCell::new(Vec::<u8>::with_capacity(4));

        if data.len() > 0 && *data.len() <= 3 { // Check for exactly 128 bits (3 bytes) or less.
            data.copy_into(&mut gen);
        } else {
            return None;
        }

        let mut generated = Vec::<u8>::with_capacity(4);
        
        if *data.len() > 0 && *data.len() <= 3 { // Check for exactly 128 bits (3 bytes) or less.
            data.copy_into(&mut generated);
        } else {
            return None;
        }

        let mut gen = RefCell::new(generated);

        Some(Self::from_data(gen, *data))
    }

    /// Returns an abstract data type generator from a raw buffer of variable size up to 128 bits (3 bytes) or less.
    pub fn create_from_buffer_variable_size_opt(data: &[u8]) -> Option<Self> {
        let mut gen = RefCell::new(Vec::<u8>::with_capacity(4));

        if data.len() > 0 && *data.len() <= 3 { // Check for exactly 128 bits (3 bytes) or less.
            data.copy_into(&mut gen);
        } else {
            return None;
        }

        let mut generated = Vec::<u8>::with_capacity(4);
        
        if *data.len() > 0 && *data.len() <= 3 { // Check for exactly 128 bits (3 bytes) or less.
            data.copy_into(&mut generated);
        } else {
            return None;
        }

        Some(Self::from_data(gen, *data))
    }

    /// Creates an abstract data type generator from a raw buffer of variable size up to 128 bits (3 bytes) or less.
    pub fn create_from_buffer_variable_size_opt
