"""Application errors."""
import pathlib


class PyProjectTOMLNotFoundError(Exception):
    """Raised when no `pyproject.toml` found."""

    def __init__(self, cwd: pathlib.Path) -> None:
        """No `pyproject.toml` found in current directory."""
        super().__init__(f"No `pyproject.toml` found at current directory {cwd!s}")
