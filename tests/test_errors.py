"""Test errors."""
from __future__ import annotations

import pathlib

import pytest

from pyrgo.core.errors import PyProjectTOMLNotFoundError


@pytest.mark.unit()
class TestPyProjectNotFoundError:
    """Test `PyProjectNotFoundError`."""

    def test_error_message(self) -> None:
        """Test error message."""
        path_to_toml = pathlib.Path.cwd().joinpath("pyproject_toml")
        assert (
            str(PyProjectTOMLNotFoundError(pyproject_toml=path_to_toml))
            == f"No `pyproject.toml` found at current directory {path_to_toml!s}"
        )
