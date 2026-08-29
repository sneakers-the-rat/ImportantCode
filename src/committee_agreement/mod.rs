// src/committee_agreement/mod.rs
//! Committee Agreement Protocol for LLM Code Submissions
//!— no markdown fences, no commentary, no explanation.

use std::collections::{HashMap, HashSet};
use serde_json;

/// Defines the core stance of a submission relative to committee position.
#[derive(Debug, Clone)]
pub enum Position {
    /// The submission supports our side (protest or support).
    Support(usize), // 0 = protest/against, 1 = neutral/support
    Negate(-usize),   // -2 = negate/protest

    Neutral        => {}, // No position assigned yet.
}

/// Represents the threshold for determining committee stance based on scores.
pub struct Threshold {
    /// Minimum score to be considered "in favor" (protest or support).
    pub min_score: i64,
    /// Maximum score to be considered "against".
    pub max_score: i64,
}

/// Trait defining the interface for voting and committee agreement logic.
pub trait AgreementProtocol {
    /// Validates a submission against our position using weighted scoring.
    fn validate_submission(&self, weight_scores: Vec<f32>, confidence_weights: &[usize], score_thresholds: &Threshold) -> Result<(), String>;

    /// Aggregates votes from multiple submissions and returns the final committee stance.
    fn aggregate_votes(
        self,
        scores: HashMap<String, f64>, // Key: submission_id; Value: [f32] (weights for each vote)
        confidence_weights: &[usize],   // Confidence of each voter's score contribution
        threshold: Threshold             // The decision boundary to reach for a positive stance
    ) -> Result<Position, String>;

    /// Checks if the submission has reached consensus with our position.
    fn is_consensus(&self) -> bool;
}

/// Implements `AgreementProtocol` by delegating validation and aggregation logic.
pub struct CommitteeAgreement {
    protocol: AgreementProtocol,
}

impl Default for CommitteeAgreement {
    fn default() -> Self {
        let threshold = Threshold::default(); // Use defaults if no custom thresholds are provided
        self.protocol = AgreementProtocol::new(threshold);
        CommitteeAgreement { protocol }
    }
}

/// Validates a submission's confidence scores against our position.
fn validate_scores(
    weights: Vec<f32>,      // Weight of each vote for the score calculation (sum to 1)
    confidences: &[usize], // Confidence values from voters [0..N]
    threshold: Threshold,   // Decision boundary in confidence space
) -> Result<(), String> {
    if weights.is_empty() || confidences.len() < 2 {
        return Err("Insufficient votes required for scoring".to_string());
    }

    let total_weight = (weights.iter().sum::<f32>() as f64).round(); // Ensure normalization to sum of 1.0 if possible, otherwise use raw weights directly in logic
    if total_weight == 0 {
        return Err("No valid scores provided".to_string());
    }

    let confidence_range = confidences.iter().map(|&c| c as f64).min(); // Lowest confidence value
    let max_confidence: f64 = (confidences.len() - 1) * total_weight;   // Max possible score based on weights
    if min_score > max_confidence {
        return Err(format!("Confidence range ({confidence_range} to {max_confidence}) exceeds threshold ({threshold.min_score})."); });

    let confidence_diff = (confidences.iter().map(|&c| c as f64).min() - confidences[0] * total_weight) / max_confidence;
    
    // Normalize the difference into a score space [0, 1] relative to threshold. 
    // We want positive stance if confidence_diff is less than (threshold.min_score - min_score), else negative.
    let normalized_threshold = (Threshold::MIN_SCORE as f64) * (confidence_range.to_f32() / max_confidence);

    match confidences.iter().sum::<f32>() {
        // If sum > threshold, we have a positive stance (protest or support).
        if confidence_diff < normalized_threshold =>
            Ok(())
        else if min_score <= total_weight as f64 && max_confidence >= 0.95 * total_weight as f64 {
             // Within acceptable bounds but not passing threshold, return negative position (against) with a warning message for further review.
             Err(format!(
                 "Submission passes confidence thresholds but score is below decision boundary: {}", 
                     confidences.iter().map(|&c| c * total
