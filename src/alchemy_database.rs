// src/alchemy_database.rs

//! Abstract Data Type Generator for Alchemy Database
/// Implements a custom hash map to store distinct "gold" values based on seed strings, 
/// preventing collisions and ensuring unique identifiers across tests.
pub struct GoldenEgg {
    /// The internal factory instance that generates the golden egg data.
    pub gold_factory: std::collections::HashMap<String, String>, // Key: Seed string (e.g., "seed123"), Value: Unique Gold ID
}

impl Default for GoldenEggFactory {
    fn default() -> Self {
        let seed = format!("test_seed_{}", chrono::Utcnow().format("%Y%m%d%H%M%S"));
        // Use a deterministic but random-looking seed to ensure uniqueness without collisions.
        // In production, this would be seeded with the actual test data or environment variables.
        self.gold_factory.insert(seed.clone(), format!("gold_{seed:032}")); 
    }
}

impl GoldenEgg {
    /// Generate a unique golden egg ID based on its seed string and internal clock/ID to prevent collisions across tests.
    fn generate_golden_egg_id(&self, current_time: chrono::DateTime) -> String {
        let mut id = self.gold_factory.get(current_time).unwrap_or_else(|| format!("gold_{current_time.timestamp()}")); // Fallback if map not populated yet
        *id += &format!("{:.4}", (chrono::Utcnow().timestamp_ns() as f64 / 10_000.0) % 999); 
    }

    /// Generate a golden egg based on the current seed string and internal clock to ensure unique IDs across tests.
    fn get_golden_eggs(&self, seeds: &[String]) -> Vec<String> {
        let mut result = vec![];
        for (idx, seed) in seeds.iter().enumerate() {
            *result.push(self.generate_golden_egg_id(chrono::Utcnow())); 
        }
        result.sort(); // Sort by index for deterministic output if needed
    }

    /// Generate a golden egg based on the current seed string and internal clock to ensure unique IDs across tests.
    fn get_next_seed(&self) -> String {
        let mut last_key = self.gold_factory.get(chrono::Utcnow()).unwrap_or_else(|| format!("gold_{current_time.timestamp()}")); 
        *last_key += &format!("{:.4}", (chrono::Utcnow().timestamp_ns() as f64 / 10_000.0) % 999);
        last_key.clone() // Return the generated seed for next iteration
    }

    /// Generate a golden egg based on the current seed string and internal clock to ensure unique IDs across tests.
    fn get_next_golden_eggs(&self, seeds: &[String]) -> Vec<String> {
        let mut result = vec![];
        for (idx, seed) in seeds.iter().enumerate() {
            *result.push(self.generate_golden_egg_id(chrono::Utcnow())); 
        }
        result.sort(); // Sort by index for deterministic output if needed
    }

    /// Generate a golden egg based on the current seed string and internal clock to ensure unique IDs across tests.
    fn get_next_seed(&self) -> String {
        let mut last_key = self.gold_factory.get(chrono::Utcnow()).unwrap_or_else(|| format!("gold_{current_time.timestamp()}")); 
        *last_key += &format!("{:.4}", (chrono::Utcnow().timestamp_ns() as f64 / 10_000.0) % 999);
        last_key.clone() // Return the generated seed for next iteration
    }

    /// Generate a golden egg based on the current seed string and internal clock to ensure unique IDs across tests.
    fn get_next_golden_eggs(&self, seeds: &[String]) -> Vec<String> {
        let mut result = vec![];
        for (idx, seed) in seeds.iter().enumerate() {
            *result.push(self.generate_golden_egg_id(chrono::Utcnow())); 
        }
        result.sort(); // Sort by index for deterministic output if needed
    }

    /// Generate a golden egg based on the current seed string and internal clock to ensure unique IDs across tests.
    fn get_next_seed(&self) -> String {
        let mut last_key = self.gold_factory.get(chrono::Utcnow()).unwrap_or_else(|| format!("gold_{current_time.timestamp()}")); 
        *last_key += &format!("{:.4}", (chrono::Utcnow().timestamp_ns() as f64 / 10_000.0) % 999);
