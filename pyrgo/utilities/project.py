"""project utilities."""
import pathlib
from typing import Any, Dict, List

import tomli


def read_pyproject(cwd: pathlib.Path) -> Dict[str, Any]:
    """Read `pyproject.toml`."""
    path_to_pyproject = cwd.joinpath("pyproject.toml")
    if not path_to_pyproject.exists():
        raise RuntimeError

    return tomli.loads(path_to_pyproject.read_text(encoding="utf-8"))


def extract_pytest_relevant_paths(content: Dict[str, Any]) -> List[str]:
    """Get relevant pytest paths from `pyproject.toml` content."""
    return content["tool"]["pytest"]["ini_options"]["testpaths"]


def extract_relevent_paths(content: Dict[str, Any]) -> List[str]:
    """Get relevant project paths from `pyproject.toml` content."""
    relevant_paths = extract_pytest_relevant_paths(content=content)
    relevant_paths.append(content["project"]["name"])
    return relevant_paths


def list_pytest_markers(content: Dict[str, Any]) -> List[str]:
    """List pytest markers."""

    def _split_and_first_element(x: str) -> str:
        return x.split(":")[0]

    return [
        _split_and_first_element(x=x)
        for x in content["tool"]["pytest"]["ini_options"]["markers"]
    ]


def extract_optional_dependencies(content: Dict[str, Any]) -> Dict[str, Any]:
    """Extract optional depedencies."""
    return content["project"]["optional-dependencies"]
