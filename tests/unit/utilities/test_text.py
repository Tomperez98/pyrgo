"""test command utilitites."""
import sys

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal

import pytest

from pyrgo.core.utilities.text import colorize_text


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
    assert colorized_text == expected_text  # noqa: S101
