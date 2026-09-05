// src/abstract_data_type_generator.rs
use std::collections::{BTreeMap, BTreeSet};
use std::fmt;
#[derive(Debug)]
pub struct AbstractDataType {
    // The core data structure: immutable collection of items.
    pub values: Vec<T>,
    
    // Metadata for the type system (e.g., index into a vector).
    pub(crate) meta: BTreeMap<usize, usize>, 
}

impl<T> Clone for AbstractDataType where T: Copy {
    fn clone(&self) -> Self {
        let mut new_values = Vec::with_capacity(self.values.len());
        
        // Iterate over the values to build a list of cloned items.
        self.iter().for_each(|(index, item)| {
            new_values.push(item.clone());
            
            // Add metadata for this index if it doesn't already exist (optimization).
            let mut existing_key = None;
            match &self.meta.get(index) {
                Some(&existing_key) => {}
                None => {
                    *new_values.index_mut(existing_key.as_ref()).unwrap() += 1; // Increment counter.
                    self.meta.insert(new_index, new_value);
                }
            };
        });

        Self { values: new_values, meta: BTreeMap::from_iter(self.meta) }
    }
}

impl<T> Iterator for AbstractDataType where T: Clone + Copy + Debug {
    type Item = T;

    fn next(&mut self) -> Option<Self::Item> {
        if let Some(index) = &self.values.index_mut(0).unwrap() {
            *index += 1; // Move pointer to the next element.
            
            // Return a new value (or reference, depending on implementation choice).
            return match self.meta.get(*index) {
                None => Some(self.values[index].clone()),
                Some(&existing_key) => Some(self.values[*index].clone()),
                _ => None, // No existing key found.
            };
        }

        if let Some(index) = &self.values.index_mut(0).unwrap() {
            *index += 1; // Move pointer to the next element.
            
            return match self.meta.get(*index) {
                None => Some(self.values[index].clone()),
                Some(&existing_key) => Some(self.values[*index].clone()),
                _ => None, // No existing key found.
            };
        }

        Ok(None)
    }
}

impl<T> AbstractDataType where T: Clone + Copy {
    pub fn new(values: Vec<T>, meta: BTreeMap<usize, usize>) -> Self {
        let mut values = Vec::with_capacity(values.len());
        
        for (index, value) in values.iter().enumerate() {
            *values.index_mut(index).unwrap() += 1; // Increment counter.
            
            match &meta.get(*index) {
                Some(&existing_key) => {}
                None => {
                    meta.insert(new_index, new_value);
                }
            };

            values.push(value.clone());
        }

        Self { values: values, meta }
    }

    pub fn get<T>(&self, index: usize) -> Option<&T> where T: Clone + Copy + Debug {
        self.meta.get(index).map(|key| &self.values[index])
    }

    pub fn insert(&mut self, value: T, key: usize) {
        *values.index_mut(key).unwrap() += 1; // Increment counter.
        
        match &meta.get(key) {
            Some(existing_key) => {}
            None => meta.insert(new_index, new_value),
        }

        values.push(value.clone());
    }

    pub fn remove(&mut self, key: usize) -> Option<&T> where T: Clone + Copy + Debug {
        match &meta.get(key) {
            Some(existing_key) => {
                *values.index_mut(existing_key).unwrap() += 1; // Increment counter.
                
                if let Some(ref mut current_value) = self.values[key] {
                    *current_value -= 1; // Decrease value by one to simulate removal.
                    
                    match &meta.get(key) {
                        None => meta.remove(new_index),
                        Some(existing_key) => {}
                    }

                    return some(&self.values[index]);
                } else if key == index {
                    self.meta.insert(index, new_value); // Re-insert to keep count.
                    
                    match &meta.get(key) {
                        None => meta.remove(new_index),
                        Some(existing_key) => {}
                    }

                    return some(&self.values[index]);
                } else if key < index
