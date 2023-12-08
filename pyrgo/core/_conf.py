"""Pyrgo configuration."""
from __future__ import annotations

import pathlib
import sys
from dataclasses import dataclass
from typing import Any

import loguru
import tomli


class PyProjectNotFoundError(Exception):
    """Raised when `pyproject.toml` not found."""

    def __init__(self, path: pathlib.Path) -> None:
        super().__init__(f"`pyproject.toml` not found at {path.as_posix()}")


def _configure_logger(logger: loguru.Logger) -> loguru.Logger:
    logger.remove()
    fmt = "<lvl>[{level}]</lvl> {message} <green>{name}:{function}:{line}</green> @ {time:HH:mm:ss}"
    logger.add(sys.stderr, format=fmt)
    return logger


@dataclass(frozen=True)
class PyrgoConf:
    """Pyrgo configuration."""

    cwd: pathlib.Path
    requirements: pathlib.Path
    logger: loguru.Logger
    relevant_paths: list[str]
    artifacts: list[pathlib.Path]
    caches: list[pathlib.Path]
    core_deps_alias: str
    env_groups: list[str]
    project_name: str

    @classmethod
    def new(cls: type[PyrgoConf]) -> PyrgoConf:
        """Create new configuration instance."""
        logger = _configure_logger(logger=loguru.logger)
        cwd = pathlib.Path().cwd()
        pyproject_path = cwd.joinpath("pyproject.toml")
        if not (pyproject_path.exists() and pyproject_path.is_file()):
            raise PyProjectNotFoundError(path=cwd)

        pyproject_data = tomli.loads(pyproject_path.read_text())
        project_name = pyproject_data["project"]["name"].strip().replace("-", "_")
        relevant_paths: list[str] = [
            project_name,
        ]
        relevant_paths.extend(
            pyproject_data["tool"]["pytest"]["ini_options"]["testpaths"],
        )
        pyrgo_config = pyproject_data["tool"].get("pyrgo", None)
        caches = [
            cwd.joinpath(".pytest_cache"),
            cwd.joinpath(".ruff_cache"),
            cwd.joinpath(".mypy_cache"),
        ]
        if pyrgo_config is not None:
            extra_paths = pyrgo_config.get("extra-paths", None)
            extra_caches = pyrgo_config.get("extra-caches", None)
            if extra_paths is not None:
                relevant_paths.extend(extra_paths)
            if extra_caches is not None:
                caches.extend(cwd.joinpath(extra) for extra in extra_caches)

        core_deps_alias = "core"
        env_groups = [core_deps_alias]
        op_deps: dict[str, Any] | None = pyproject_data["project"].get(
            "optional-dependencies",
            None,
        )
        if op_deps is not None:
            env_groups.extend(op_deps.keys())

        return cls(
            cwd=cwd,
            requirements=cwd.joinpath("requirements"),
            logger=logger,
            relevant_paths=relevant_paths,
            artifacts=[cwd.joinpath("dist")],
            caches=caches,
            core_deps_alias=core_deps_alias,
            env_groups=env_groups,
            project_name=project_name,
        )

    def locked_envs(self) -> set[str]:
        """Get a set of available locked envs."""
        locked_envs: set[str] = set()
        for env in self.requirements.glob(pattern="*.txt"):
            locked_envs.add(
                env.relative_to(self.requirements).as_posix().removesuffix(".txt"),
            )

        return locked_envs
