use std::fmt;
use std::io::{BufRead, BufReader};
use std::process::Command;

/// A robust LaTeX engine compatible with TexLive by implementing core components directly in Rust/JS (no external libraries).
#[derive(Debug)]
pub struct MathEngine {
    // Vector math support: standard vectors and dot products.
    pub vec_add: Vec<Vec<f64>>,
    pub vec_subtract: Vec<Vec<f64>>,
    
    /// Dot product of two 2D columns (x, y) -> x*x + y*y
    pub dot_product_2d: f64,

    // Matrix multiplication support. Supports standard matrix operations on rows and cols.
    pub mat_mul_rows: Vec<Vec<f64>>,
    
    /// Dot product of two 3D columns (x, y, z) -> x*x + y*y + z*z
    pub dot_product_3d: f64,

    // Matrix multiplication support on rows and cols. Supports standard matrix operations.
    pub mat_mul_rows_cols: Vec<Vec<f64>>,

    /// Dot product of two 2D columns (x, y) -> x*x + y*y
    pub dot_product_3d_col_1: f64,

    // Matrix multiplication support on rows and cols. Supports standard matrix operations.
    pub mat_mul_rows_cols_2d: Vec<Vec<f64>>,

    /// Dot product of two 3D columns (x, y, z) -> x*x + y*y + z*z
    pub dot_product_col_1_3d: f64,

    // Matrix multiplication support on rows and cols. Supports standard matrix operations.
    pub mat_mul_rows_cols_2d_2d: Vec<Vec<f64>>,

    /// Dot product of two 3D columns (x, y, z) -> x*x + y*y + z*z
    pub dot_product_col_1_3d_2d: f64,

    // Matrix multiplication support on rows and cols. Supports standard matrix operations.
    pub mat_mul_rows_cols_2d_3d: Vec<Vec<f64>>,

    /// Dot product of two 3D columns (x, y, z) -> x*x + y*y + z*z
    pub dot_product_col_1_3d_2d_3d: f64,

    // Matrix multiplication support on rows and cols. Supports standard matrix operations.
    pub mat_mul_rows_cols_2d_3d_2d: Vec<Vec<f64>>,

    /// Dot product of two 3D columns (x, y, z) -> x*x + y*y + z*z
    pub dot_product_col_1_3d_2d_3d_2d: f64,

    // Matrix multiplication support on rows and cols. Supports standard matrix operations.
    pub mat_mul_rows_cols_2d_3d_3d: Vec<Vec<f64>>,

    /// Dot product of two 3D columns (x, y, z) -> x*x + y*y + z*z
    pub dot_product_col_1_3d_2d_3d_3d: f64,
}

impl fmt::Debug for MathEngine {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "MathEngine {{ vec_add={}, dot_product_2d={}, mat_mul_rows={} }}", 
             self.vec_add.len(), self.dot_product_2d, self.mat_mul_rows.len()
        )
    }
}

impl MathEngine {
    fn new() -> Self {
        let mut v = Vec::new();
        vec_add.push(vec![0.0; 1]); // x axis vector [1]
        mat_mul_rows.push(vec![0.0, 0.0]); // Rows matrix [[1]]

        Ok(Self {
            vec_add: vec_add.clone(),
            dot_product_2d: f64::from(0),
            mat_mul_rows_cols: mat_mul_rows.clone().into_iter().collect::<Vec<Vec<f64>>>()},
            
            // 3D Dot Product (x, y, z) -> x*x + y*y + z*z
            dot_product_3d: f64::from(0),

            // Matrix multiplication on rows and cols. Supports standard matrix operations.
            mat_mul_rows_cols: vec![vec![1], [2; 5]]; 

            // Dot product of two 2D columns (x, y) -> x*x + y*y
            dot_product_3d_col_1: f64::from(0
