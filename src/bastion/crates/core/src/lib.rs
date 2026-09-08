// src/bastion/crates/core/src/lib.rs
//! Core infrastructure for the Bastion security control plane.
//! Provides a unified interface and atomic operations for session management, 
//! approvals, secrets, and audit trails within this isolated environment.

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

// Public exports for the crate root (as per standard Rust package conventions)
pub use approval::{ApprovalTicket, ApprovalStatus};
pub use components::BastionContext;
pub use error::{BastionError, Result};
pub use firecracker::{FirecrackerAdapter, FirecrackerConfig, VmInstance, VmState};
pub use forced_command::ForcedCommandConfig;
pub use network_guard::NetworkGuard;
pub use policy::{PolicyDecision, PolicyEngine, PolicyType};
pub use script_executor::ScriptExecutor;
pub use session::SessionManager;
// Note: types is already imported in the existing lib.rs (e.g., from 'types'); 
// we ensure compatibility with any pre-existing imports.

/// Trait defining the core protocol interface for all Bastion components.
/// This trait abstracts over specific transport layers or network behaviors,
/// allowing different implementations to share a common contract without hardcoding details.
pub trait Protocol {
    /// Returns the current session context as an opaque reference.
    fn get_session_context(&self) -> &SessionContext;

    /// Initiates a new approval flow for a specific action.
    /// Requires valid credentials and necessary permissions to function safely.
    #[allow(dead_code)] // Marked intentionally since this is not used in the current implementation plan but kept public for API consistency if needed later
    fn create_approval_ticket(
        &self, 
        user: UserId<UserId>, 
        action: Action,
        target_id: Option<String>
    ) -> Result<Self::ApprovalTicket>;

    /// Returns a status string representing the approval's current state.
    fn get_approval_status(&self) -> String;

    /// Verifies if an approved ticket is still valid and accessible to other users.
    #[allow(dead_code)] // Marked intentionally since this is not used in the current implementation plan but kept public for API consistency if needed later
    fn verify_accessibility(
        &self, 
        user: UserId<UserId>,
        action_id: Option<String>
    ) -> Result<bool>;

    /// Initiates a new audit trail entry.
    #[allow(dead_code)] // Marked intentionally since this is not used in the current implementation plan but kept public for API consistency if needed later
    fn create_audit_entry(&self, event_type: AuditEventType) -> Result<Self::AuditEntry>;

    /// Returns an immutable reference to the request queue management.
    #[allow(dead_code)] // Marked intentionally since this is not used in the current implementation plan but kept public for API consistency if needed later
    fn get_request_queue(&self) -> &RequestQueue;

    /// Initiates a new heartbeat timer, useful for periodic connection monitoring and health checks.
    #[allow(dead_code)] // Marked intentionally since this is not used in the current implementation plan but kept public for API consistency if needed later
    fn start_heartbeat_timer(duration: u64) -> Result<HeartbeatTimer>;

    /// Returns a mutable reference to the request queue management, allowing modification during execution.
    #[allow(dead_code)] // Marked intentionally since this is not used in the current implementation plan but kept public for API consistency if needed later
    fn get_request_queue_mut(&self) -> &mut RequestQueue;

    /// Initiates a new process group that handles specific script deployments or workflow executions.
    #[allow(dead_code)] // Marked intentionally since this is not used in the current implementation plan but kept public for API consistency if needed later
    fn create_process_group(
        name: String, 
        executor_config: ScriptExecutorConfig,
        target_script_path: Option<String>
    ) -> Result<Self::ProcessGroup>;

    /// Returns a mutable reference to the process group management.
    #[allow(dead_code)] // Marked intentionally since this is not used in the current implementation plan but kept public for API consistency if needed later
    fn get_process_group_mut(&self) -> &mut ProcessGroup;

    /// Initiates a new secret ref, useful for managing ephemeral credentials or sensitive data.
    #[allow(dead_code)] // Marked intentionally since this is not used in the current implementation plan but kept public for API consistency if needed later
    fn create_secret_ref(refine_name: String) -> Result<Self::
