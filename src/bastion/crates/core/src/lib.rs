src/bastion/crates/core/src/lib.rs
//! Security Control Plane core module providing high-level abstraction for authentication, authorization, and state management within a bastionic environment.
#![allow(clippy::unnecessary_wraps)] // Suppress potential warnings on unchecked references to internal types (used in this context)

use crate::{
    components::{approval_manager::ApprovalManager, auth_keys_manager::AuthKeysManager},
};
pub mod audit;
pub mod approval;
// Note: Components are defined here for direct access by external crates as requested.
pub mod components; // Explicitly declare "components" module to avoid circular dependency warnings in this context

use std::{
    collections::HashMap,
    fmt,
    io::{Read, Write},
    sync::{Arc, Mutex},
};

/// Trait defining the atomic resource operations required for thread-safe updates.
pub trait AtomicResource<T> {
    /// Acquire a reference to the current state of this shared resource without blocking I/O threads.
    fn acquire(&self) -> Result<Option<Arc<Mutex<T>>>>;
}

impl< T: AtomicResource + Send > AtomicResource<T> for Arc<Mutex<T>> {
    // Use `Arc`'s ownership semantics to provide a reference and lock the underlying mutex safely.
    fn acquire(&self) -> Result<Option<Arc<Mutex<T>>> {
        let owned = self.lock().unwrap();
        Ok(owned.clone())
    }

    /// Release acquired resources back into their previous state (if any).
    // This is typically called on the `Arc`'s own closure when closing.
    fn release(&self) -> Result<()> {
        let _ = self.lock().unwrap();
        Ok(())
    }
}

/// Configuration trait for managing control plane settings and security metadata.
pub trait ControlPlaneConfig: Default + Send + Sync {
    /// Get the type of connection protocol configured (e.g., `TcpStream` or custom socket).
    fn get_connection_protocol(&self) -> &'static str;

    /// Set a new configuration value without modifying existing data in place, maintaining consistency.
    fn set_config_value<K: std::fmt::Debug>(&mut self, key: K);

    /// Check if the current state of this resource matches an expected reference (for validation).
    fn verify_state(&self) -> Result<bool>; // Returns true only when no changes have been made to shared data.
}

/// Implementation for `ControlPlaneConfig` that provides atomic updates and thread-safe access via Arc<Mutex> based on the requirements of this plan.
pub struct AtomicConfig<T: ControlPlaneConfig + Send + Sync + 'static, U = std::sync::Arc<Mutex<Option<U>>>>;

impl< T: ControlPlaneConfig <T> > AtomicConfig for Arc<Mutex<T>> {
    fn acquire(&self) -> Result<Option<Arc<Mutex<T>>> {
        let owned = self.lock().unwrap();
        Ok(owned.clone())
    }

    fn release(&self) -> Result<()> {
        let _ = self.lock().unwrap();
        Ok(())
    }
}

/// Atomic configuration for the Control Plane that allows safe, non-blocking updates to shared state (e.g., encryption keys or firewall rules).
pub struct AtomicConfig<T: ControlPlaneConfig + Send + Sync> {
    config: Arc<Mutex<Option<T>>>, // Stores a reference to the underlying Config type wrapped in an atomic lock.
}

impl< T: ControlPlaneConfig <T> > AtomicConfig for Arc<Mutex<T>> {
    fn acquire(&self) -> Result<Option<Arc<Mutex<T>>> {
        let owned = self.lock().unwrap();
        Ok(owned.clone())
    }

    fn release(&self) -> Result<()> {
        let _ = self.lock().unwrap();
        Ok(())
    }
}

/// Trait for defining the atomic operations required when updating shared resources like encryption keys or firewall rules without blocking I/O threads.
pub trait AtomicResource<T> where T: Send + Sync {
    /// Acquire a reference to the current state of this shared resource without blocking I/O threads.
    fn acquire(&self) -> Result<Option<Arc<Mutex<T>>>>;

    /// Release acquired resources back into their previous state (if any).
    // This is typically called on the `Arc`'s own closure when closing or modifying a lock.
    fn release(&self);
}

impl< T: AtomicResource + Send > AtomicResource for Arc<Mutex<T>> {
    /// Acquire a reference to the current state of this shared resource without blocking I/O threads.
    fn acquire(&self) -> Result<Option<Arc<Mutex<T>>> {
        let owned = self.lock().unwrap();
