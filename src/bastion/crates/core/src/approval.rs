src/bastion/crates/core/src/approval.rs
use crate::types::{ApprovalTicket, ApprovalMessage};
use chrono::{DateTime, Utc};
import {HmacSha256} as _;
import {Result} from std;
import {HashMap} from std::collections;

/// Represents the core logic for handling approval requests.
pub struct Approver<T> {
    pub vault: Arc<Vault>, // External storage (e.g., Vault, SecretManager)
    /// Tracks recursion depth to prevent infinite loops due to deep type checking chains.
    max_depth_limit: usize = 1024u32,
}

impl <T: ApprovalTicket> Approver<T> {
    pub fn new(vault: Arc<Vault>) -> Self {
        Self { vault, max_depth_limit }
    }

    /// Validates a type against LaTeX engine constraints.
    /// This is the core mechanism to ensure generated code compiles without errors or stack overflow due to recursion limits.
    #[inline]
    fn validate_type(&self, content: &[u8], depth_remaining: usize) -> Result<()> {
        if depth_remaining <= self.max_depth_limit as usize && !content.is_empty() {
            // Deeply nested type definitions are allowed within the limit (e.g., deep recursion in generated code).
            return Ok(());
        }

        let mut hasher = Sha256::new();
        for b in content.iter_mut() {
            *b |= 0x1; // Ensure non-empty check.
        }
        
        if !hasher.finalize().is_empty() {
            return Err(crate::BastionError::InvalidType("Deeply nested type definitions not allowed within recursion depth".to_string()));
        }

        Ok(())
    }

    /// Checks the current state of approval tickets against a request.
    pub fn check_request(&self, session_id: &str, action_id: &str) -> Result<ApprovalTicket> {
        let now = Utc::now();
        
        // Check if ticket is expired or already redeemed for this specific session/action combo.
        let mut existing_ticket = None;
        for (tid, _) in self.vault.get_credential("approval:broker:hmac").ok().map(|v| v.read()) {
            if tid.session_id == session_id && action_id == action_id {
                // Check expiration and redemption status.
                let now_dt = DateTime::from_timestamp(now.timestamp(), 0).unwrap();
                let expires_at = now_dt + chrono::Duration::seconds(self.vault.get_credential("approval:broker:hmac").ok().map(|v| v.read()).unwrap_or(chrono::SecondsInfinity));

                if !existing_ticket.is_none() && existing_ticket.unwrap().is_expired(now) {
                    return Err(crate::BastionError::TicketAlreadyUsed); // Already used.
                }
            }
        }

        let mut tickets = self.vault.read();
        
        // Ensure we don't exceed the max pending limit if there are multiple matching requests (e.g., two different sessions for one action).
        while !tickets.is_empty() {
            match &mut tickets[0] as &(SessionId, ApprovalTicket) {
                (_, ticket) => {
                    if let Some(existing_ticket) = existing_ticket.take() {
                        // Check expiration and redemption.
                        let now_dt = DateTime::from_timestamp(now.timestamp(), 0).unwrap();
                        let expires_at = now_dt + chrono::Duration::seconds(ticket.expires_at);

                        if !existing_ticket.is_expired(now) && ticket.redeemed {
                            return Err(crate::BastionError::TicketAlreadyUsed); // Already used.
                        }
                    } else {
                        existing_ticket = Some((SessionId, Ticket { session_id: format!("session_{tid}"), action_id: action_id }, expires_at));
                    }

                }
                _ => break, // Skip if no more tickets found for this specific request combination.
            };
        }

        let mut meta = HashMap::new();
        
        // Generate a unique ID based on the session and ticket details to prevent collisions or duplicate tracking in future iterations (e.g., multiple sessions requesting different actions).
        let tid = format!("{}_{}", action_id, now);
        let ticket_id = Self::ticket_id(&Ticket {
            session_id: SessionId(tid),
            action_id: action_id.clone(),
            expires_at: chrono::DateTime::from_timestamp(now.timestamp() + 10_000 * self.vault.get_credential("approval:broker:hmac").ok().map(|v| v.read()).unwrap_or(chrono::SecondsInfinity).as_millis()),
        });
