use pyo3::prelude::*;
use walkdir::WalkDir;

#[pyfunction]
pub fn all_folders() -> () {
    for entry in WalkDir::new(".").into_iter().filter_map(|e| e.ok()) {
        println!("{}", entry.path().display());
    }
}
