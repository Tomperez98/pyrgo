"""test command utilitites."""
from __future__ import annotations

import pathlib
from typing import TYPE_CHECKING

import pytest

from pyrgo.core.utilities.text import colorize_text, path_to_lock_file

if TYPE_CHECKING:
    import sys

    if sys.version_info >= (3, 9):
        from typing import Literal
    else:
        from typing_extensions import Literal


@pytest.mark.unit()
@pytest.mark.parametrize(
    argnames=["color", "expected_text"],
    argvalues=[
        (
            "yellow",
            "\x1b[33mhi\x1b[0m",
        ),
        (
            "red",
            "\x1b[31mhi\x1b[0m",
        ),
    ],
)
def test_colorize_text(color: Literal["yellow", "red"], expected_text: str) -> None:
    """Test colorize text works as expected."""
    colorized_text = colorize_text(text="hi", color=color)
    assert colorized_text == expected_text


@pytest.mark.unit()
@pytest.mark.parametrize(
    argnames=[
        "base_path",
        "extra_path",
        "group",
        "lock_file_format",
        "expected_path",
    ],
    argvalues=[
        (
            pathlib.Path().cwd().joinpath("abc"),
            "xyz",
            "core",
            "txt",
            "xyz/core.txt",
        ),
    ],
)
def test_path_to_lock_file(
    base_path: pathlib.Path,
    extra_path: str,
    group: str,
    lock_file_format: str,
    expected_path: str,
) -> None:
    """Test path to lock file."""
    total_path = base_path.joinpath(extra_path)
    generated_path = path_to_lock_file(
        cwd=base_path,
        requirements_path=total_path,
        group=group,
        lock_file_format=lock_file_format,
    )
    assert generated_path == expected_path
