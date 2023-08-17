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

    def __init__(self, path: pathlib.Path) -> None:  # noqa: D107
        super().__init__(f"`pyproject.toml` not found at {path.as_posix()}")


def _configure_logger(logger: loguru.Logger) -> loguru.Logger:
    logger.remove()
    fmt = "<lvl>[{level}]</lvl> {message} <green>{name}:{function}:{line}</green> @ {time:HH:mm:ss}"  # noqa: E501
    logger.add(sys.stderr, format=fmt)
    return logger


@dataclass(frozen=True)
class PyrgoConf:
    """Pyrgo configuration."""

    cwd: pathlib.Path
    requirements: pathlib.Path
    logger: loguru.Logger
    relevant_paths: list[str]
    optional_deps: set[str] | None

    @classmethod
    def new(cls: type[PyrgoConf]) -> PyrgoConf:
        """Create new configuration instance."""
        logger = _configure_logger(logger=loguru.logger)
        cwd = pathlib.Path().cwd()
        pyproject_path = cwd.joinpath("pyproject.toml")
        if not (pyproject_path.exists() and pyproject_path.is_file()):
            raise PyProjectNotFoundError(path=cwd)

        pyproject_data = tomli.loads(pyproject_path.read_text())
        relevant_paths: list[str] = [
            pyproject_data["project"]["name"].strip().replace("-", "_"),
        ]
        relevant_paths.extend(
            pyproject_data["tool"]["pytest"]["ini_options"]["testpaths"],
        )
        extra_paths = pyproject_data["tool"]["pyrgo"].get("extra-paths", None)
        if extra_paths is not None:
            relevant_paths.extend(extra_paths)

        op_deps: dict[str, Any] | None = pyproject_data["project"].get(
            "optional-dependencies",
            None,
        )

        return cls(
            cwd=cwd,
            requirements=cwd.joinpath("requirements"),
            logger=logger,
            relevant_paths=relevant_paths,
            optional_deps=None if op_deps is None else set(op_deps.keys()),
        )
