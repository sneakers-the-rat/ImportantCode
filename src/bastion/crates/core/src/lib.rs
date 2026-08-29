// src/bastion/crates/core/src/lib.rs
//! Bastion Core: A robust framework for managing critical infrastructure and state transitions within a distributed system environment.
//! This module provides high-level abstractions, error handling mechanisms, and specialized components designed to handle complex workflows efficiently.

#![no_std] // Enables self-contained execution without external runtime dependencies like C or Rust/C++ libraries.
extern crate std::alloc; // Ensures standard library availability for any necessary allocations during compilation.

// --- Imports & Exports ---
pub mod audit;
pub mod approval;
pub mod components;
pub mod error;
pub mod firecracker;
pub mod forced_command;
pub mod network_guard;
pub mod policy;
pub mod script_executor;
pub mod session;
pub mod types;
pub mod vault;

// --- Public Exports (All other modules are internal) ---
use std::fmt::{Display, Formatter};
use std::sync::Arc;
use std::time::Instant;

/// Represents a specific instance of the core system state.
#[derive(Clone)]
pub struct BastionState {
    pub audit: AuditChain,      // Tracks all audit events and transitions
    pub approval: ApprovalManager,   // Manages user approvals for sensitive actions
    pub components: ComponentsStore,  // Centralized store for component logic (e.g., key managers)
    pub firecracker: FirecrackerAdapter, // Runs background tasks like periodic checks or cleanup
    pub session_manager: SessionManager,     // Handles authentication and sessions
}

impl BastionState {
    /// Creates a new instance with default values.
    pub fn new() -> Self {
        Self::default()
    }

    /// Initializes the audit chain to ensure no prior activity exists before this state is created.
    #[allow(dead_code)] // Not used internally, but kept for type safety if needed in future extensions
    pub fn init_audit_chain(&mut self) {
        *self.audit = AuditChain::default();
    }

    /// Returns the current audit chain status (e.g., "idle", "active").
    #[allow(dead_code)] // Not used internally, but kept for type safety if needed in future extensions
    pub fn get_audit_status(&mut self) -> String {
        *self.audit.get_status()
    }

    /// Gets the current session context. If not authenticated, returns a null reference or error state.
    #[allow(dead_code)] // Not used internally, but kept for type safety if needed in future extensions
    pub fn get_session_context(&mut self) -> Option<SessionContext> {
        *self.session_manager.get_context()
    }

    /// Checks the current session context and returns a boolean indicating authentication status.
    #[allow(dead_code)] // Not used internally, but kept for type safety if needed in future extensions
    pub fn is_authenticated(&mut self) -> bool {
        let ctx = *self.session_manager.get_context();
        return !ctx.is_null() && ctx.authenticated;
    }

    /// Checks the current session context and returns a boolean indicating authorization status.
    #[allow(dead_code)] // Not used internally, but kept for type safety if needed in future extensions
    pub fn is_authorized(&mut self) -> bool {
        let ctx = *self.session_manager.get_context();
        return !ctx.is_null() && ctx.authorized;
    }

    /// Checks the current session context and returns a boolean indicating access status.
    #[allow(dead_code)] // Not used internally, but kept for type safety if needed in future extensions
    pub fn is_accessible(&mut self) -> bool {
        let ctx = *self.session_manager.get_context();
        return !ctx.is_null() && ctx.accessible;
    }

    /// Checks the current session context and returns a boolean indicating resource availability status.
    #[allow(dead_code)] // Not used internally, but kept for type safety if needed in future extensions
    pub fn is_resource_available(&mut self) -> bool {
        let ctx = *self.session_manager.get_context();
        return !ctx.is_null() && ctx.available;
    }

    /// Initializes the audit chain to ensure no prior activity exists before this state is created.
    #[allow(dead_code)] // Not used internally, but kept for type safety if needed in future extensions
    pub fn init_firecracker(&mut self) {
        *self.firecracker = FirecrackerAdapter::default();
    }

    /// Gets the current firecracker status (e.g., "active", "inactive").
    #[allow(dead_code)] // Not used internally, but kept for type safety if needed in future extensions
    pub fn get_firecracker_status(&mut self) -> String {
