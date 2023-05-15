"""Text utilities."""
import sys

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
import click


def colorize_text(
    *,
    text: str,
    color: Literal[
        "yellow",
        "red",
    ],
) -> str:
    """Colorize text."""
    return click.style(text=text, fg=color)
