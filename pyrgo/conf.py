"""Pyrgo configuration."""
from __future__ import annotations

import pathlib
import sys
from dataclasses import dataclass, field
from typing import Any

import click
from mashumaro import field_options
from mashumaro.mixins.toml import DataClassTOMLMixin


@dataclass(frozen=True)
class _Project:
    name: str
    optional_dependencies: dict[str, Any] = field(
        metadata=field_options(alias="optional-dependencies"), default_factory=dict
    )


@dataclass(frozen=True)
class _Pyrgo:
    extra_paths: list[str] = field(
        metadata=field_options(alias="extra-paths"), default_factory=list
    )
    extra_caches: list[str] = field(
        metadata=field_options(alias="extra-caches"), default_factory=list
    )
    vulture_allowlist: str = field(
        metadata=field_options(alias="vulture-allowlist"), default=".whitelist.vulture"
    )


@dataclass(frozen=True)
class _Tooling:
    pytest: dict[str, Any]
    pyrgo: _Pyrgo = field(default=_Pyrgo())


@dataclass(frozen=True)
class _PyProjectToml(DataClassTOMLMixin):
    project: _Project
    tool: _Tooling


class PyProjectNotFoundError(Exception):
    """Raised when `pyproject.toml` not found."""

    def __init__(self, path: pathlib.Path) -> None:  # noqa: D107
        super().__init__(f"`pyproject.toml` not found at {path.as_posix()}")


class PyrgoConf:
    """Pyrgo configuration."""

    def __init__(self) -> None:
        """Create new configuration instance."""
        cwd = pathlib.Path().cwd()
        pyproject_path = cwd.joinpath("pyproject.toml")
        if not (pyproject_path.exists() and pyproject_path.is_file()):
            raise PyProjectNotFoundError(path=cwd)

        pyproject_data = _PyProjectToml.from_toml(pyproject_path.read_text())

        project_name = pyproject_data.project.name.strip().replace("-", "_")
        relevant_paths: list[str] = [
            project_name,
        ]
        try:
            test_paths = pyproject_data.tool.pytest["ini_options"]["testpaths"]

        except KeyError:
            click.echo(
                message=click.style(
                    "`tool.pytest.ini_options.testpaths` is required.", fg="red"
                ),
                color=True,
            )
            sys.exit(1)

        caches = [
            cwd.joinpath(".pytest_cache"),
            cwd.joinpath(".ruff_cache"),
            cwd.joinpath(".mypy_cache"),
            *(cwd.joinpath(extra) for extra in pyproject_data.tool.pyrgo.extra_caches),
        ]

        relevant_paths.extend(
            test_paths,
        )
        relevant_paths.extend(pyproject_data.tool.pyrgo.extra_paths)

        self.cwd: pathlib.Path = cwd
        self.requirements: pathlib.Path = cwd.joinpath("requirements")
        self.relevant_paths: list[str] = relevant_paths
        self.artifacts: list[pathlib.Path] = [cwd.joinpath("dist")]
        self.caches: list[pathlib.Path] = caches
        self.env_groups: list[str] = [
            "core",
            *pyproject_data.project.optional_dependencies.keys(),
        ]
        self.project_name: str = project_name
        self.pyproject_path: pathlib.Path = pyproject_path
        self.vulture_allowlist: pathlib.Path = cwd.joinpath(
            pyproject_data.tool.pyrgo.vulture_allowlist
        ).relative_to(cwd)

    def locked_envs(self) -> set[str]:
        """Get a set of available locked envs."""
        locked_envs: set[str] = set()
        for env in self.requirements.glob(pattern="*.txt"):
            locked_envs.add(
                env.relative_to(self.requirements).as_posix().removesuffix(".txt"),
            )

        return locked_envs
