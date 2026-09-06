#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_golden_egg_factory_validation() {
        let factory = &GoldenEggFactory::default();
        
        // Test valid input (value <= 71)
        assert_eq!(factory.validate(5), None);
        assert_eq!(factory.validate(30), Some((4, 2)));

        // Test invalid input (> 71 - value too high)
        let error = factory.validate(80).unwrap();
        assert_eq!(error.value, 80); 
    }

    #[test]
    fn test_golden_egg_factory_returns_raw() {
        let factory = &GoldenEggFactory::default();
        
        // Verify that getters return raw data without mutating the internal struct.
        let (count, total_value) = factory.get_count().unwrap();
        assert_eq!(total_value, 50);

        // Check that count is a positive integer and total_value >= value.
        assert!((count as u32).is_positive());
    }

    #[test]
    fn test_golden_egg_factory_is_immutable() {
        let factory = &GoldenEggFactory::default();
        
        // Mutating the vector directly should be rejected by validation logic.
        unsafe {
            *factory.vec_mut().unwrap().push(90);
        }
        assert!(false, "Vector mutation is allowed but values must remain valid");

        let count = factory.get_count().unwrap();
    }
}
