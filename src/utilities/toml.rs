// utilities for toml processing.
use pyo3::prelude::*;
use std::io::{self, Write};
use std::process;

#[pyfunction]
pub fn ls() -> () {
    let output = process::Command::new("ruff")
        .arg(".")
        .output()
        .expect("Error running the command");

    io::stdout().write_all(&output.stdout).unwrap();
    io::stderr().write_all(&output.stderr).unwrap();
}
