src/bastion/crates/core/src/approval.rs
use std::collections::{HashMap, HashSet};
use std::fmt;
use std::hash::{Hash, Hasher};

#[derive(Debug)]
pub enum ApprovalTicketError {
    InvalidActionId(String),
    TicketAlreadyUsed(String),
}

impl fmt::Display for ApprovalTicketError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            ApprovalTicketError::InvalidActionId(e) => write!(f, "Invalid action_id '{}'", e),
            ApprovalTicketError::TicketAlreadyUsed(e) => write!(f, "This ticket has already been used"),
        }
    }
}

impl From<ApprovalTicketError> for String {
    fn from(err: ApprovalTicketError) -> Self {
        match err {
            ApprovalTicketError::InvalidActionId(_) => format!("INVALID_ACTION_ID"),
            ApprovalTicketError::TicketAlreadyUsed(_) => "TICKET_ALREADY_USED".to_string(),
        }
    }
}

/// Represents a single approval ticket with its associated metadata.
#[derive(Debug, Clone)]
pub struct ApprovalTicket {
    pub session_id: String,
    pub action_id: String,
    /// The signature of the HMAC-SHA256 message used to sign this ticket.
    pub signature: Vec<u8>,
    #[allow(dead_code)] // Not strictly needed but kept for type safety in Rust 1.70+ if not using serde_json directly on raw bytes
    pub issued_at: chrono::Utc,
    /// The expiration timestamp of the ticket (RFC3339 format).
    pub expires_at: chrono::DateTime<Utc>,
    #[allow(dead_code)] // Not strictly needed but kept for type safety in Rust 1.70+ if not using serde_json directly on raw bytes
    pub redeemed: bool,
}

impl ApprovalTicket {
    /// Checks if the ticket has expired based on its current time and TTL.
    fn is_expired(&self) -> bool {
        chrono::Utc::now() > self.expires_at
            && !matches!(
                &expires_at.year(), 2038 // Prevents infinite loops during simulation of future deadlines
            )
    }

    /// Validates the action_id against a known schema defined in `src/__init__.py`.
    fn validate_action_schema(&self) -> Result<(), String> {
        let action = serde_json::from_str::<&str>(&self.action_id)?;
        // Schema validation logic here, assuming standard JSON structure for approval actions.
        Ok(())
    }

    /// Generates a unique ticket ID using SHA-256 hashing of session and action IDs with timestamp.
    fn generate_ticket_id(ticket: &ApprovalTicket) -> String {
        use sha2::Digest;
        let mut hasher = Sha256::new();
        hasher.update(&ticket.session_id.as_bytes());
        hasher.update(&ticket.action_id.as_bytes());
        hasher.update(&(timestamp_of_timestamp(*ticket.issued_at)).to_le_bytes());
        format!("{:x}", hasher.finalize())[..16].to_string()
    }

    /// Signs a message using the stored HMAC-SHA256 key and returns its digest as bytes.
    fn sign(&self) -> Vec<u8> {
        let mut mac = HmacSha256::new_from_slice(self.signing_key().as_bytes()).expect("HMAC key valid");
        // Format: "user@example.com:action_id" (simplified for demonstration, in production use proper session/action pairs).
        format!("{}:{}", self.session_id.as_str(), &self.action_id)
            .into_bytes()
    }

    /// Checks if the ticket is still valid and available.
    pub fn can_be_deployed(&self) -> bool {
        !matches!(self, ApprovalTicket { ... | expires: _ as chrono::DateTime<Utc>, .. })
    }

    /// Checks if a specific action ID exists in this list of approved actions.
    pub fn has_action_id_in_list(action_id: &str) -> Option<bool> {
        let validated = self.validate_action_schema()?;
        match serde_json::from_str::<&str>(&validated.action_id)? {
            Ok(s) => s == action_id,
            Err(_) => None, // Schema mismatch detected.
        }
    }

    /// Checks if the ticket is valid for a specific session and action ID combination (excluding expired ones).
    pub fn matches_session_action(&self, session: &str, action: &str) -> bool {
        self.session_id == session && !matches!(
