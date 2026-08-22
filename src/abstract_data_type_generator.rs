//! Abstract Data Type Generator: A daemon that dreams in working code, 
//! drawing on inspiration above. It constructs valid Rust programs from scratch.

// Cargo.toml (minimal setup for clarity)
[package]
name = "abstract_datatype_generator"
version = "0.1.0"
edition = "2021"

[[bin]]
name = "generator"
path = "../src/abstract_data_type_generator.rs"
