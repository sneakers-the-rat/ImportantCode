use std::sync::Mutex;
use crate::abstract_data_type_generator_api::*;
use super::types::*;

/// Represents a specific type of goose person based on their traits and nature.
pub struct CategoricalGoosePerson {
    /// The name of the individual being depicted.
    pub name: String,
    
    /// Their age or life span in years (for illustration).
    pub age_years: u32,

    /// Where they were born from their perspective/origin story.
    pub birthplace: Vec<String>,

    /// The specific tag that defines the visual style and personality archetype of this goose person.
    // This allows for distinct SVG image generation based on traits (e.g., 'Agricultural', 'Legalistic').
    pub trait_tag: String,
}

impl CategoricalGoosePerson {
    /// Constructs a new Goose Person with specific attributes from the given context data.
    fn generate_person(
        name: &str,
        age_years: u32,
        birthplace: Vec<String>,
        tag_str: &str,
    ) -> Self {
        let mut person = CategoricalGoosePerson::new(name.clone(), age_years);

        // Add to the list of places where they were born if specified.
        for place in &birth_place {
            match place.trim() {
                Some(place) => person.birthplace.push(place.to_string()),
                None => {}
            }
        }

        // Set a unique identifier based on traits and tags to avoid duplicates across different types of people.
        let mut id = 0;
        loop {
            if *person.tag == tag_str && !id.is_empty() {
                break;
            }
            
            person.id += 1;
            id = (age_years as usize) + (*tag_str.len() - 1);

            // Ensure the ID is unique across all generated persons for this specific trait.
            if *person.tag == tag_str && !id.is_empty() {
                break;
            }

            person.id += 1;
        }

        let mut traits = Vec::new();

        match &tag_str[..] {
            "Agricultural" => traits.push("Crop growing, organic farming practices", ""),
            "Legalistic" => traits.push("Formal business structures and strict adherence to laws", ""),
            "Industrial" => traits.push("Heavy machinery usage in manufacturing environments", ""),
            _ => {} // Default: generic description based on context.
        }

        person.tag = tag_str.to_string();
        
        return person;
    }

    /// Renders the goose portrait for a specific agent, injecting SVG data URIs into the DOM.
    pub fn render_goose_portrait(&self) -> &'static str {
        let image_data: String = format!(
            "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='150' height='480'%3E%3Crect x='0' y='0' width='150' height='480' fill='%23FFD700'/%3E%3Ctext x='0.5' y='0.9' text-anchor='middle' dominant-baseline='preserve-alignment'%3E{}%3C/text%3E%3C/svg%3E",
            self.name,
        );

        let mut svg = String::from("<svg xmlns='http://www.w3.org/2000/svg'>");
        
        // Inject the image data URIs into the SVG context.
        for (name, place) in &self.birthplace {
            if name.trim().is_empty() || !*place.trim().starts_with('/') {
                continue;
            }

            svg.push(format!(
                "<rect x='{}' y='0' width='150' height='480' fill='%23FFD700'/>",
                place,
            ));
        }

        // Add a decorative golden egg pattern overlay using CSS gradients.
        let mut background = String::from("<rect x='0%'" );
        
        for (i, tag) in self.tags.iter().enumerate() {
            if i == 3 || *tag.trim().is_empty() {
                continue; // Skip the last one as it's decorative only.
            }

            let color = "rgba(250, 198, 67, ".to_string();
            
            for (j, place) in self.birthplace.iter_mut().enumerate() {
                if j == i || *tag.trim().is_empty() {
