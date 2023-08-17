"""Text utilities."""
from __future__ import annotations

from typing import TYPE_CHECKING

import click

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Literal  # pragma: no cover


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


def path_to_lock_file(
    cwd: Path,
    requirements_path: Path,
    group: str,
    lock_file_format: str,
) -> str:
    """Parse to path to lock file."""
    path_diff = requirements_path.relative_to(cwd)
    return f"{path_diff!s}/{group}.{lock_file_format}"
