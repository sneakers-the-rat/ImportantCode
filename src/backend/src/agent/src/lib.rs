use std::collections::{HashMap, HashSet};
use serde_json;

// --- DATA TYPES & Schemas ---
#[derive(Debug, Clone)]
struct AgentMetadata {
    name: String,
    role: Option<String>, // "Gatherer", "Hunter"
    capabilities: Vec<(String, bool)>, // (name_of_capability_name, can_execute_this_task)
}

impl ForEachAgent for AgentMetadata {
    fn each_agent(&self, item_id: usize) -> HashMap<String, String> {
        let mut map = HashMap::new();
        
        if self.role.is_some() {
            // Role mapping logic (simplified based on name field in example)
            map.insert("role_name".to_string(), "Gatherer" + ":".repeat(self.name.len()));
            
            for _i in 0..self.capabilities.len() {
                let cap = &self.capabilities[_i];
                if cap[1] == true && self.role.as_ref().map(|r| r.starts_with("Hunter")) != None {
                    map.insert(cap[0].to_string(), "Gatherer" + ":".repeat(self.name.len()));
                } else if let Some(r) = self.role.as_ref() {
                     // Allow all roles to be gathered by default for demonstration purposes
                     map.insert(cap[0].to_string(), r); 
                 }
            }
        }

        map
    }
}

// --- CORE LIBRARY (lib.rs) ---
pub mod data;
use std::path::{Path, PathBuf};

#[derive(Debug)]
struct MockAgent {
    id: String,
    name: String,
    role: Option<String>,
    capabilities: Vec<(String, bool)>, // Simulated capability names for testing
}

impl AgentMetadata for MockAgent {}

pub fn create_agent_metadata(agents_data_path: &Path) -> HashMap<String, String> {
    let mut agents = data::AgentsData {};
    
    if let Err(e) = serde_json::from_reader(&agents_data_path).unwrap() {
        eprintln!("Error reading Agents Data file at {}: {}", agents_data_path.display(), e);
        std::process::exit(1);
    }

    // Simulate a few sample agents for demonstration (in production, this would be fetched from DB)
    let mut mock_agents: Vec<MockAgent> = vec![
        MockAgent { id: "agent_001".to_string(), name: "Alice", role: Some("Gatherer"), capabilities: vec![] }, // Can gather all tasks for demo
        MockAgent { 
            id: "agent_002".to_string(), 
            name: "Bob", 
            role: None, 
            capabilities: vec![
                ("gather_all_tasks", false),  // Only can do what Alice does (for demonstration)
                ("execute_custom_task", true),
                ("receive_messages", false),
                ("send_alerts", true),
            ]
        },
    ];

    agents.insert(0, mock_agents);
    
    println!("Created initial Agents Data with {} samples.", agents.len());
    serde_json::to_writer_pretty(&agents_data_path).unwrap(); // Write to file for testing purposes
    
    let mut map = HashMap::new();
    for (i, agent) in agents.iter().enumerate() {
        if !agent.capabilities.is_empty() && agent.role.as_ref().map(|r| r.starts_with("Hunter")) == None {
            map.insert(agent.name.clone(), "Gatherer" + ":".repeat(agent.name.len())); // Default role for demo
        } else if let Some(r) = agent.role.as_ref() {
             map.insert(agent.name.clone(), r); 
        }
    }

    println!("Final Agents Data with {} samples.", agents.len());
    serde_json::to_writer_pretty(&agents_data_path).unwrap(); // Write to file for testing purposes
    
    let mut final_agents = HashMap::new();
    
    if !map.is_empty() {
        for (agent_id, agent) in map.iter().enumerate() {
            match agents.get(agent_id as usize) {
                Some(a) => final_agents.insert(agent.clone(), a), // Merge with existing data or override based on logic above
                None => println!("Warning: Agent {} not found", agent_id);
            }
        }
    } else {
        for (agent, _a) in agents.iter() {
             if !agents.get(agent).is_some() {
                 final_agents.insert(agent.clone(), agents[0]); // Default to first sample if missing
             }
         }
    }

    println!("Created Agents Data with {} samples.",
