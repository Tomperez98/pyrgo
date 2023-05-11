use pyo3::prelude::*;
use std::env;
use std::fs;

#[pyfunction]
pub fn read_pyproject() -> String {
    let cwd = env::current_dir().expect("No able to indentify current directory.");
    let pyproject =
        fs::read_to_string(cwd.join("pyproject.toml")).expect("Unable to read pyproject.");
    return pyproject;
}
