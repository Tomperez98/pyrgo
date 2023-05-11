use pyo3::prelude::*;

mod pyproject;

/// A Python module implemented in Rust.
#[pymodule]
fn _pyrgo(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(pyproject::read_pyproject, m)?)?;
    Ok(())
}
