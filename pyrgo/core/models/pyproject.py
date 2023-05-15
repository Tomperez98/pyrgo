"""project utilities."""
import pathlib
import sys
from typing import Any, Dict, List, Optional

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
import dataclasses

import tomli
from result import Err, Ok, Result
from typing_extensions import assert_never

from pyrgo.core.errors import PyProjectTOMLNotFoundError


@dataclasses.dataclass(frozen=False, eq=False)
class Pyproject:
    """Dataclass representation of `pyproject.toml`."""

    cwd: pathlib.Path
    data: Optional[Dict[str, Any]] = dataclasses.field(default=None, init=False)

    def read_pyproject_toml(self) -> Result[None, PyProjectTOMLNotFoundError]:
        """Read data from `pyproject.toml`."""
        path_to_pyproject = self.cwd.joinpath("pyproject.toml")
        if not path_to_pyproject.exists():
            return Err(PyProjectTOMLNotFoundError(cwd=self.cwd))
        self.data = tomli.loads(path_to_pyproject.read_text(encoding="utf-8"))
        return Ok()

    def _extract_pytest_relevant_paths(self) -> List[str]:
        if not self.data:
            raise RuntimeError
        return self.data["tool"]["pytest"]["ini_options"]["testpaths"]

    def _extract_core_path(self) -> str:
        if not self.data:
            raise RuntimeError
        return self.data["project"]["name"]

    def extract_relevant_paths(self, paths_type: Literal["all", "pytest"]) -> List[str]:
        """Get relevant paths from `pyproject.toml` content."""
        if paths_type == "pytest":
            return self._extract_pytest_relevant_paths()
        if paths_type == "all":
            all_paths: List[str] = []
            all_paths.append(self._extract_core_path())
            all_paths.extend(self._extract_pytest_relevant_paths())
            return all_paths

        assert_never(paths_type)

    def list_pytest_markers(self) -> List[str]:
        """List pytest markers."""
        if not self.data:
            raise RuntimeError

        def _split_and_first_element(x: str) -> str:
            return x.split(":")[0]

        return [
            _split_and_first_element(x=x)
            for x in self.data["tool"]["pytest"]["ini_options"]["markers"]
        ]

    def extract_optional_dependencies(self) -> Dict[str, Any]:
        """Extract optional depedencies."""
        if not self.data:
            raise RuntimeError
        return self.data["project"]["optional-dependencies"]
