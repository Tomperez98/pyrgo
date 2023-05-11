use pyo3::prelude::*;

mod file_system;

mod utilities;

/// A Python module implemented in Rust.
#[pymodule]
fn _pyrgo(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(file_system::all_folders, m)?)?;
    Ok(())
}
