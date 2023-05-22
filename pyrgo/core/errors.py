"""Application errors."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


class PyProjectTOMLNotFoundError(Exception):
    """Raised when no `pyproject.toml` found."""

    def __init__(self, pyproject_toml: Path) -> None:
        """No `pyproject.toml` found in current directory."""
        super().__init__(
            f"No `pyproject.toml` found at current directory {pyproject_toml!s}",
        )
