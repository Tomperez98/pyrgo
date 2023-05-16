"""project utilities."""
import pathlib
import sys
from typing import Any, Dict, List, Optional

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
import dataclasses

import tomlkit
from result import Ok, Result
from typing_extensions import assert_never


@dataclasses.dataclass(frozen=False, eq=False)
class Pyproject:
    """Dataclass representation of `pyproject.toml`."""

    data: Optional[tomlkit.TOMLDocument] = dataclasses.field(default=None, init=False)

    def read_pyproject_toml(
        self,
        pyproject_path: pathlib.Path,
    ) -> Result[None, Exception]:
        """Read data from `pyproject.toml`."""
        self.data = tomlkit.parse(pyproject_path.read_bytes())
        return Ok()

    def override_pyproject_toml(self, new_path: pathlib.Path) -> None:
        """Override pyrproject toml."""
        if not self.data:
            raise RuntimeError
        data_as_string = tomlkit.dumps(data=self.data, sort_keys=False)
        new_path.write_text(data=data_as_string, encoding="utf-8")

    def project_section(self) -> Dict[str, Any]:
        """Get `project` section."""
        if not self.data:
            raise RuntimeError

        project: Optional[Dict[str, Any]] = self.data.get("project")
        if not project:
            raise RuntimeError
        return project

    def _extract_pytest_relevant_paths(self) -> List[str]:
        if not self.data:
            raise RuntimeError
        tools: Optional[Dict[str, Any]] = self.data.get("tool")
        if not tools:
            raise RuntimeError

        return tools["pytest"]["ini_options"]["testpaths"]

    def _extract_core_path(self) -> str:
        if not self.data:
            raise RuntimeError

        project = self.project_section()

        return project["name"]

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

        tools: Optional[Dict[str, Any]] = self.data.get("tool")
        if not tools:
            raise RuntimeError
        return [
            _split_and_first_element(x=x)
            for x in tools["pytest"]["ini_options"]["markers"]
        ]

    def extract_optional_dependencies(self) -> Dict[str, Any]:
        """Extract optional depedencies."""
        if not self.data:
            raise RuntimeError
        project = self.project_section()

        return project["optional-dependencies"]
