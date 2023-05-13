"""project utilities."""
import pathlib
from dataclasses import dataclass
from functools import cache
from typing import Any, Dict, List, Optional

import tomli


@dataclass
class PyProject:
    """Pyproject model."""

    name: str
    version: str
    dependencies: Optional[List[str]]
    optional_dependencies: Optional[Dict[str, List[str]]]


@cache
def read_pyproject(cwd: pathlib.Path) -> Dict[str, Any]:
    """Read `pyproject.toml`."""
    path_to_pyproject = cwd.joinpath("pyproject.toml")
    if not path_to_pyproject.exists():
        raise RuntimeError

    return tomli.loads(path_to_pyproject.read_text(encoding="utf-8"))


def parse_pyproject(content: Dict[str, Any]) -> PyProject:
    """Parse `pyproject.toml` content."""
    project_content: Dict[str, Any] = content["project"]
    return PyProject(
        name=project_content["name"],
        version=project_content["version"],
        dependencies=project_content.get("dependencies"),
        optional_dependencies=project_content.get("optional-dependencies"),
    )


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
