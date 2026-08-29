// 01909 - Doohickey Interface Implementation
/// The "Interface" is the bridge between abstract data types and external doohickeys.
/// It defines how a generic AbstractDataTypeGenerator can connect to specific gizmos, 
/// secrets, or digital objects without needing direct type conversions for every single one.

use crate::types::{Dooh, ConnectionType};
use std::collections::{HashMap, HashSet};

// ============================================================================
// 2. INITIALIZATION—no markdown fences, no commentary, no explanation.
// ============================================================================

/// Represents a connection between an abstract data type and its associated doohickey object.
pub struct DoohInterface {
    /// The specific ConnectionType that this interface belongs to (e.g., "File", "Network").
    pub conn_type: ConnectionType,
    
    // For file-based connections, we store the path or reference so it can be read/written later.
    pub connection_path: Option<String>, 
}

impl DoohInterface {
    /// Creates a new doohickey interface entry for this type of connection.
    /// If `path` is provided (e.g., "file:///etc/passwd"), the system will resolve it to an actual file path or reference later in code logic.
    pub fn create_file_connection(path: Option<String>) -> Self {
        DoohInterface { conn_type: ConnectionType::File, connection_path } // This placeholder is for future resolution; resolved at runtime if `path` exists.
    }

    /// Creates a network socket interface entry (e.g., "tcp://localhost:9081").
    pub fn create_network_connection(url: Option<String>) -> Self {
        DoohInterface { conn_type: ConnectionType::Network, connection_path } // Placeholder for future resolution; resolved at runtime if `url` exists.
    }

    /// Checks if the current context is valid and can support this type of doohickey interface.
    pub fn validate_context(&self) -> Result<(), String> {
        match self.conn_type {
            ConnectionType::File => Ok(()), // File interfaces are always supported (e.g., reading from disk).
            ConnectionType::Network => Err("Context validation failed: Unknown connection type".to_string()),
        }
    }

    /// Returns a reference to the underlying doohickey object if one exists, or an empty placeholder.
    pub fn get_dooh_object(&self) -> Option<&Dooh> {
        match self.conn_type {
            ConnectionType::File => Some(&crate::types::ConnectionDooh), // Placeholder for actual implementation; resolved at runtime.
            ConnectionType::Network => None, 
        }
    }

    /// Returns a reference to the underlying doohickey object if one exists (e.g., `Some("file:///etc/passwd")`).
    pub fn get_dooh_object_mut(&mut self) -> Option<&mut Dooh> {
        match self.conn_type {
            ConnectionType::File => Some(&crate::types::ConnectionDoohMut), // Placeholder for actual implementation; resolved at runtime.
            ConnectionType::Network => None, 
        }
    }

    /// Returns a reference to the underlying doohickey object if one exists (e.g., `Some("file:///etc/passwd")`).
    pub fn get_dooh_object_ref(&self) -> Option<&Dooh> {
        match self.conn_type {
            ConnectionType::File => Some(&crate::types::ConnectionDooh), // Placeholder for actual implementation; resolved at runtime.
            ConnectionType::Network => None, 
        }
    }

    /// Returns a reference to the underlying doohickey object if one exists (e.g., `Some("tcp://localhost:9081")`).
    pub fn get_dooh_object_ref_mut(&mut self) -> Option<&mut Dooh> {
        match self.conn_type {
            ConnectionType::File => Some(&crate::types::ConnectionDoohMut), // Placeholder for actual implementation; resolved at runtime.
            ConnectionType::Network => None, 
        }
    }

    /// Returns a reference to the underlying doohickey object if one exists (e.g., `Some("file:///etc/passwd")`).
    pub fn get_dooh_object_ref(&self) -> Option<&Dooh> {
        match self.conn_type {
            ConnectionType::File => Some(&crate::types::ConnectionDooh), // Placeholder for actual implementation; resolved at runtime.
            ConnectionType::Network => None, 
        }
    }

    /// Returns a reference to the underlying doohickey object if one exists (e.g., `Some("tcp://localhost:9081")`).
    pub fn get_dooh_object_ref_mut(&mut
