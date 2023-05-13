"""project utilities."""
import pathlib
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import tomli


@dataclass
class PyProject:
    """Pyproject model."""

    name: str
    version: str
    dependencies: Optional[List[str]]
    optional_dependencies: Optional[Dict[str, List[str]]]


def read_pyproject(cwd: pathlib.Path) -> PyProject:
    """Read `pyproject.toml`."""
    path_to_pyproject = cwd.joinpath("pyproject.toml")
    if not path_to_pyproject.exists():
        raise RuntimeError

    content = tomli.loads(path_to_pyproject.read_text(encoding="utf-8"))
    project_content: Dict[str, Any] = content["project"]
    return PyProject(
        name=project_content["name"],
        version=project_content["version"],
        dependencies=project_content.get("dependencies"),
        optional_dependencies=project_content.get("optional-dependencies"),
    )
