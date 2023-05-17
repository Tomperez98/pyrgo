"""Application configuration."""
import dataclasses
import pathlib
from typing import List, Optional, Set

import tomlkit
from typing_extensions import Self

from pyrgo.core.errors import (
    PyProjectTOMLNotFoundError,
)
from pyrgo.core.models.pyproject import Pyproject
from pyrgo.logging import logger


@dataclasses.dataclass(frozen=True, repr=False, eq=False)
class Config:
    """Configuration variables."""

    cwd: pathlib.Path
    pyproject_toml_path: pathlib.Path
    requirements_path: pathlib.Path
    caches_paths: List[pathlib.Path]
    artifacts_paths: List[pathlib.Path]
    venv_path: pathlib.Path
    venv_activation_msg: str
    core_dependecies_name: str
    lock_file_format: str
    pyproject_toml: Pyproject

    def available_environments(self) -> List[str]:
        """List available environments in `requirements/`."""
        return [
            x.name.rstrip(f".{self.lock_file_format}")
            for x in self.requirements_path.glob(f"*.{self.lock_file_format}")
            if x.is_file()
        ]


class ConfigBuilder:  # noqa: D101
    def __init__(self) -> None:
        """Build `Config`."""
        self.cwd: Optional[pathlib.Path] = None
        self.pyproject_toml_path: Optional[pathlib.Path] = None
        self.requirements_path: Optional[pathlib.Path] = None
        self.venv_path: Optional[pathlib.Path] = None
        self.caches_paths: Optional[List[pathlib.Path]] = None
        self.artifacts_paths: Optional[List[pathlib.Path]] = None
        self.venv_activation_msg: Optional[str] = None
        self.core_dependecies_name: Optional[str] = None
        self.lock_file_format: Optional[str] = None
        self.pyproject_toml: Optional[Pyproject] = None

    def attach_paths(
        self,
        cwd: pathlib.Path,
        cache_paths: Set[str],
        artifacts_paths: Set[str],
        venv: str,
    ) -> Self:
        """Attach configuration by paths."""
        self.cwd = cwd
        self.pyproject_toml_path = cwd.joinpath("pyproject.toml")
        if not self.pyproject_toml_path.exists() and self.pyproject_toml_path.is_file():
            raise PyProjectTOMLNotFoundError(cwd=self.cwd)

        self.requirements_path = cwd.joinpath("requirements")
        if not self.requirements_path.exists():
            logger.warning(
                "creating `requirements/` directory at {location}",
                location=self.requirements_path,
            )
            self.requirements_path.mkdir(parents=False, exist_ok=False)

        self.caches_paths = [cwd.joinpath(x) for x in cache_paths]
        self.artifacts_paths = [cwd.joinpath(x) for x in artifacts_paths]
        self.venv_path = cwd.joinpath(venv)
        return self

    def attach_other(
        self,
        venv_activation_msg: str,
        core_dependecies_name: str,
        lock_file_format: str,
    ) -> Self:
        """Attach various configurations."""
        self.venv_activation_msg = venv_activation_msg
        self.core_dependecies_name = core_dependecies_name
        self.lock_file_format = lock_file_format
        return self

    def attach_pyproject(self) -> Self:
        """Attach pyproject."""
        if not (self.core_dependecies_name and self.pyproject_toml_path):
            raise RuntimeError

        self.pyproject_toml = Pyproject(
            core_dependency_name=self.core_dependecies_name,
            data=tomlkit.parse(self.pyproject_toml_path.read_bytes()),
        )

        return self

    def build(self) -> Config:
        """Build config."""
        if not (
            self.artifacts_paths
            and self.cwd
            and self.pyproject_toml_path
            and self.requirements_path
            and self.caches_paths
            and self.venv_path
            and self.pyproject_toml
        ):
            raise RuntimeError
        if not (
            self.venv_activation_msg
            and self.core_dependecies_name
            and self.lock_file_format
        ):
            raise RuntimeError

        return Config(
            cwd=self.cwd,
            pyproject_toml_path=self.pyproject_toml_path,
            requirements_path=self.requirements_path,
            caches_paths=self.caches_paths,
            artifacts_paths=self.artifacts_paths,
            venv_activation_msg=self.venv_activation_msg,
            core_dependecies_name=self.core_dependecies_name,
            venv_path=self.venv_path,
            lock_file_format=self.lock_file_format,
            pyproject_toml=self.pyproject_toml,
        )


app_config = (
    ConfigBuilder()
    .attach_other(
        venv_activation_msg=(
            "\nTo activate the virtual env run:\n\n"
            "On Windows, run:\n`.venv\\Scripts\\activate.bat`\n\n"
            "On Unix or MacOS, run:\n`source .venv/bin/activate`\n"
        ),
        core_dependecies_name="core",
        lock_file_format="txt",
    )
    .attach_paths(
        cwd=pathlib.Path().cwd(),
        cache_paths={
            ".mypy_cache",
            ".pytest_cache",
            ".ruff_cache",
        },
        artifacts_paths={
            "dist",
            "site",
        },
        venv=".venv",
    )
    .attach_pyproject()
).build()
