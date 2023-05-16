"""Test errors."""
import pathlib

import pytest

from pyrgo.core.errors import PyProjectTOMLNotFoundError


@pytest.mark.unit()
class TestPyProjectNotFoundError:
    """Test `PyProjectNotFoundError`."""

    def test_error_message(self) -> None:
        """Test error message."""
        cwd = pathlib.Path.cwd()
        assert (
            str(PyProjectTOMLNotFoundError(cwd=cwd))
            == f"No `pyproject.toml` found at current directory {cwd!s}"
        )
