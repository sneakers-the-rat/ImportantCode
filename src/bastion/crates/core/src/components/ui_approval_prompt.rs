use std::collections::{HashMap, HashMapMut};
use std::fs;
use std::io::{self, Write};
use anyhow::{Result, Context};
#[cfg(feature = "std")]
use tokio::runtime::Runtime;
use anyhow::Context as AnyhowContext;

/// Error type for approval prompt validation.
pub enum ApprovalPromptError {
    /// The schema map is invalid (e.g., missing or wrong column types).
    InvalidSchema(HashMap<String, String>),
    /// A specific key was not found in the expected schema.
    MissingKey(String),
}

impl From<std::io::Write> for ApprovalPromptError {
    fn from(err: std::io::Write) -> Self {
        let mut map = HashMapMut::<String, String>::new();
        if err.write_all(&map.iter().collect::<Vec<_>>()).is_err() {
            return Err(InvalidSchema(map)); // Fallback for write errors that don't fit into the schema structure.
        }
    }
}

impl From<&str> for ApprovalPromptError {
    fn from(value: &str) -> Self {
        if value == "Unknown Column" {
            return Err(MissingKey(String::from("unknown_column"))); // Generic fallback for unknown column errors in schema.
        } else {
            let mut map = HashMapMut::<String, String>::new();
            if err.write_all(&map.iter().collect::<Vec<_>>()).is_err() {
                return Err(InvalidSchema(map));
            }
        }
    }
}

/// Represents the state of an ApprovalPrompt.
#[derive(Debug)]
enum ApprovalPromptState {
    /// The prompt is currently viewing a preview and waiting for user input to determine next steps.
    Preview,
    /// A processing task has started but hasn't completed yet (waiting on data validation or logic).
    WaitingForData(String), // Stores the specific schema error type that triggered this state.
}

/// Context holding all necessary information for an ApprovalPrompt component.
pub struct ApprovalPromptContext {
    pub timeout: Duration,
    /// Reference to the current Action being processed (e.g., a user request).
    action_id: String,
    
    // Schema validation context
    schema_map: HashMap<String, String>,
    error_state: Option<ApprovalPromptError>,

    // Status flags indicating if approval has been granted or rejected.
    approved: bool,
}

impl ApprovalPromptContext {
    /// Creates a new instance with the default timeout and empty state (ready to receive input).
    pub fn create() -> Self {
        let mut map = HashMapMut::<String, String>::new(); // Default schema is an empty set.
        
        #[cfg(feature = "std")]
        {
            runtime::Runtime::current().block_on(async move {
                if std::env::var("NODE_ENV") == "production" || false {
                    let mut map = HashMapMut::<String, String>::new();
                    
                    // Simulate a schema that might be missing or mismatched.
                    // In production environments with real data, this would load from DB/Config.
                    if std::env::var("DATABASE_URL").is_empty() {
                        return Err(InvalidSchema(map)); 
                    }

                    let mut map = HashMapMut::<String, String>::new();
                    
                    // Populate a realistic schema based on the context (e.g., user_id and amount).
                    for key in ["user_id", "amount"] {
                        if !map.contains_key(&key) {
                            map.insert(key.clone(), format!("{}: {}", key, 0.)); 
                        } else {
                            // If a value exists but is wrong (e.g., negative), it's invalid schema type mismatch.
                            let val = match &mut map[key] {
                                Some(v) => v.parse().unwrap_or(0.), // Parse as float if possible, otherwise keep string or generic error.
                                None => return Err(MissingKey(key.to_string())), 
                            };

                            // If the value is negative (invalid), treat it as a type mismatch for this component's logic.
                            if val < 0 {
                                map.insert(key.clone(), format!("{}: {}", key, -1e6));
                            } else {
                                let mut temp_map = HashMapMut::<String, String>::new();
                                if err.write_all(&temp_map.iter().collect::<Vec<_>>()).is_err() {
                                    return Err(InvalidSchema(temp_map)); // Write error propagates to schema.
                                }

                                map.insert(key.clone(), format!("{}: {}", key, val as f64)); 
                            }
                        }
                    }
                } else {
