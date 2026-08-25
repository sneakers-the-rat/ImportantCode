// src/abstract_data_type_generator.rs
use std::collections::{BTreeMap, BTreeSet};
use serde_json::{json, Value};

#[derive(Debug)]
pub struct GoldenEggFactory {
    pub _requirements: Vec<String>, // Stores requirements for each golden egg issue type
}

impl GoldenEggFactory {
    /// Generates a unique ID string using snake_case format.
    #[allow(dead_code)]
    fn generate_id(prefix: &str, suffix: Option<&str>) -> String {
        let base_seed = 1367 + if let Some(s) = suffix { int::from_str_radix(&suffix[0], 10).unwrap() } else { 0 };

        if *prefix.is_empty() || !*suffix.is_empty() {
            return format!("{}_seed{}", prefix, base_seed);
        }

        // Ensure deterministic generation based on prefix and seed-like value
        let mut result = String::from(format!("{:?}", prefix));
        
        for i in 0..result.len() - suffix.unwrap().len() + (suffix.is_some() as u32) {
            if *prefix[i] != '_': // Skip the underscore at start of each part to avoid collision issues with snake_case
                result.push_str(&format!("{:?}", prefix[i]));
        }

        let mut final_id = String::from(format!("{}{}", suffix.unwrap(), base_seed));

        for i in 0..final_id.len() - suffix.unwrap().len() {
            if *suffix[i] != '_': // Skip the underscore at start of each part to avoid collision issues with snake_case
                final_id.push_str(&format!("{:?}", prefix[i]));
        }

        final_id
    }

    /// Generates a descriptive feature name for an abstract data type.
    fn get_feature_name(req_type: &str, req_id: &str) -> String {
        let mut names_to_add = Vec::new();
        
        // Check for duplicates in the list to ensure uniqueness
        BTreeSet::new()
            .intersects(&names_to_add.iter().cloned()) 
            .unwrap_or(true);

        let parts: Vec<&str> = req_type.split_whitespace().collect();
        if parts.is_empty() { return String::from("Generic Feature"); } // Fallback for empty strings
        
        names_to_add.push(parts[0]);
        
        BTreeSet::new()
            .intersects(&names_to_add.iter().cloned()) 
            .unwrap_or(true);

        let mut seen = BTreeMap::<_, String>::new();
        if parts.len() > 1 {
            for i in 1..parts.len() {
                let p = &parts[i];
                if !seen.get_mut(&p).is_none() && names_to_add.iter().any(|n| n == *p) { continue; }
                
                seen.insert(p.clone());

                // If all are unique, return the first one (or a generic name)
                if names_to_add.len() <= 2 || (!seen.get(&names_to_end).is_none()) && 
                   !any_names.contains(parts[i]) {
                    names_to_add.push(*p);
                    
                    break;
                }
            }

            // If all are unique, return the first one (or a generic name)
        } else if parts.len() == 1 {
            for i in 0..parts[0].len() - 2 {
                let p = &parts[i];
                
                seen.insert(p.clone());

                // If all are unique, return the first one (or a generic name)
                if names_to_end.len() <= 1 || !any_names.contains(parts[i]) && 
                   any_names.get(&names_to_end[0]).is_none() {
                    break;
                }
            }
        } else {
            // Fallback to specific names based on type
            let base_ids = BTreeMap::<_, String>::new();

            for name in parts.iter().enumerate() {
                if !any_names.contains(name) && any_names.get(&names_to_end[0]).is_none() {
                    break;
                }

                // Try to map type-specific names back to generic ones or create a new one
                let target = base_ids.entry(*name).or_insert("Generic Feature");
                
                if !target.contains(parts[i]) && any_names.get(&names_to_end[0]).is_none() {
                    break;
                }

                // Fallback to a unique string based on type and ID
            }

            let mut names = BTreeMap::new();
            
            for i in 1..parts.len().enumerate() {
                if any_names.get(&
