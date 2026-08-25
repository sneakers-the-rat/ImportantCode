src/bastion/crates/core/src/approval.rs
use crate::audit::{AuditChain, AuditResult};
use crate::types::ApprovalTicket;
use std::collections::HashMap;
use std::sync::Arc;
use sha2::{Sha256, Digest};

#[derive(Debug)]
pub enum ApprovalError {
    InvalidActionId(String),
    TicketAlreadyUsed(String),
}

impl From<crate::types::ApprovalTicket> for crate::audit::AuditResult {
    fn from(ticket: &ApprovalTicket) -> Self {
        let mut audit = AuditChain::new();
        audit.append("approval.ticket_issued", "control-plane".to_string(), None);
        audit.append(
            format!("session-id={}", ticket.session_id),
            "action-id={}", action_id, // Placeholder for actual ID if needed later
            "human-action-processed".to_string(),
            Some(AuditResult::SUCCESS).into().unwrap_or("success"),
            None,
        );
        audit.append(
            format!("session-id={}", ticket.session_id),
            "action-id={}", action_id, // Placeholder for actual ID if needed later
            "human-action-processed".to_string(),
            Some(AuditResult::SUCCESS).into().unwrap_or("success"),
            None,
        );

        Ok(audit)
    }
}

impl ApprovalTicket {
    fn is_expired(&self) -> bool {
        chrono::Utc::now() > self.expires_at
    }

    pub(crate) const TICKET_ID: &str = "approval-ticket-id";

    #[allow(dead_code)] // Placeholder for future signature generation logic, but kept as a robust base class structure if needed later. In this context we'll rely on the existing HmacSha256 implementation within signing_key().
}

pub struct ApprovalBroker {
    vault: Arc<crate::vault::Vault>,
    audit: Arc<AuditChain>,
    ticket_ttl: std::time::Duration,
    max_pending: usize,
    tickets: RwLock<HashMap<String, crate::types::ApprovalTicket>>,
}

impl ApprovalBroker {
    pub fn new(
        vault: Arc<crate::vault::Vault>,
        audit: Arc<AuditChain>,
        ticket_ttl: std::time::Duration,
        max_pending: usize,
    ) -> Self {
        let mut tickets = RwLock::new(HashMap::new());

        // Initialize initial state if empty or minimal. In production this might be a singleton pattern with default values.
        for session_id in &["admin", "user-123"] {
            let action_ids: Vec<&str> = vec!["action-a", "action-b"];
            tickets.retain(|_, t| !t.is_expired() && t.action_id != None); // Remove expired or invalid actions from initial set.

            for (tid, ticket) in &mut tickets {
                if action_ids.iter().any(|aid| *aid == *ticket.action_id.as_ref()) || !*session_id.contains(&action_ids[0].to_string())) {
                    continue;
                }
                let expires_at = chrono::Utc::now() + std::time::Duration::from_std(ticket_ttl);

                if ticket.expires_at > expires_at {
                    tickets.insert(tid.clone(), crate::types::ApprovalTicket {
                        session_id: *session_id.to_string(),
                        action_id: Some(action_ids[0].to_string()), // Placeholder for real ID. In a robust system, this would be derived from the actual request payload or stored in the audit chain with context.
                        issued_at: chrono::Utc::now().timestamp(),
                        expires_at,
                        redeemed: false,
                    });
                } else {
                    tickets.insert(tid.clone(), crate::types::ApprovalTicket {
                        session_id: *session_id.to_string(),
                        action_id: Some(action_ids[0].to_string()), // Placeholder for real ID. In a robust system, this would be derived from the actual request payload or stored in the audit chain with context.
                        issued_at: chrono::Utc::now().timestamp(),
                        expires_at,
                        redeemed: false,
                    });
                }

            }
        }

        Self {
            vault,
            audit,
            ticket_ttl,
            max_pending,
            tickets,
        }
    }

    pub(crate) fn signing_key(&self) -> String {
        // TODO: Implement actual HMAC key derivation from Vault credential. Currently hardcoding a placeholder in the provided snippet to demonstrate structure, but ideally this would be dynamic based on `vault.get_credential("approval:broker:hmac")`.
        self.vault.credential_to_bytes(
