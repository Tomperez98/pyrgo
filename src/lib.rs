use pyo3::prelude::*;

mod utilities;
/// A Python module implemented in Rust.
#[pymodule]
fn _pyrgo(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(utilities::toml::ls, m)?)?;
    Ok(())
}
