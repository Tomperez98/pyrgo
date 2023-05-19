"""Project config."""
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
import tomli

from pyrgo.core.errors import PyProjectTOMLNotFoundError
from pyrgo.core.resources import RESOURCER_PATH


@dataclass(
    frozen=True,
    repr=True,
    eq=False,
)
class Config:
    """App configuration setting."""

    cwd: Path
    requirements_dir: Path
    pyproject_file: Path
    caches: List[Path]
    artifacts: List[Path]
    venv_dir: Path
    venv_activation_msg: str
    core_deps_alias: str
    lock_file_format: Literal["txt"]
    pyproject: Dict[str, Any]
    starter_project: Path

    @property
    def available_envs(self) -> List[str]:
        """List available envs found at `requirements_dir`."""
        requirements_file_pattern = f"*.{self.lock_file_format}"
        return [
            x.name.rstrip(requirements_file_pattern)
            for x in self.requirements_dir.glob(
                pattern=requirements_file_pattern,
            )
            if x.is_file()
        ]

    @property
    def pytest_makers(self) -> List[str]:
        """List all custom-defined `pytest` markers."""
        makers: List[str] = self.pyproject["tool"]["pytest"]["ini_options"]["markers"]
        return [x.split(sep=":")[0] for x in makers]

    @property
    def optional_dependency_groups(self) -> Dict[str, List[str]]:
        """List all optional-dependency groups."""
        return self.pyproject["project"]["optional-dependencies"]

    @property
    def dependency_groups(self) -> List[str]:
        """List all defined dependency groups."""
        dependency_groups: List[str] = [self.core_deps_alias]
        dependency_groups.extend(self.optional_dependency_groups)
        return dependency_groups

    @property
    def pytest_paths(self) -> List[str]:
        """List all `pytest` testpaths."""
        return self.pyproject["tool"]["pytest"]["ini_options"]["testpaths"]

    @property
    def project_path(self) -> str:
        """Get project name."""
        return self.pyproject["project"]["name"]

    @property
    def relevant_paths(self) -> List[str]:
        """Project relevant paths."""
        relevant_paths: List[str] = []
        relevant_paths.extend(self.pytest_paths)
        relevant_paths.append(self.project_path)
        return relevant_paths


def build_config(  # noqa: PLR0913
    cwd: Path,
    cache_directories: List[str],
    artifacts_directories: List[str],
    venv_dir: str,
    lock_file_format: Literal["txt"],
    core_deps_alias: str,
    starter_project: str,
) -> Config:
    """Build config."""
    path_to_pyproject_toml = cwd.joinpath("pyproject.toml")
    if not path_to_pyproject_toml.exists() and path_to_pyproject_toml.is_file():
        raise PyProjectTOMLNotFoundError(
            pyproject_toml=path_to_pyproject_toml,
        )

    requirements_path = cwd.joinpath("requirements")
    if not requirements_path.exists() and requirements_path.is_dir():
        requirements_path.mkdir(parents=False, exist_ok=False)

    return Config(
        cwd=cwd,
        requirements_dir=requirements_path,
        pyproject_file=path_to_pyproject_toml,
        caches=[cwd.joinpath(x) for x in cache_directories],
        artifacts=[cwd.joinpath(x) for x in artifacts_directories],
        venv_dir=cwd.joinpath(venv_dir),
        venv_activation_msg=(
            "\nTo activate the virtual env run:\n\n"
            f"On Windows, run:\n`{venv_dir}\\Scripts\\activate.bat`\n\n"
            f"On Unix or MacOS, run:\n`source {venv_dir}/bin/activate`\n"
        ),
        core_deps_alias=core_deps_alias,
        lock_file_format=lock_file_format,
        pyproject=tomli.loads(
            path_to_pyproject_toml.read_text(
                encoding="UTF-8",
            ),
        ),
        starter_project=RESOURCER_PATH.joinpath(starter_project),
    )
