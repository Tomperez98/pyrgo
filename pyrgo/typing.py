"""Typing module."""
from __future__ import annotations

from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from typing_extensions import TypeAlias

PyrgoProgram: TypeAlias = Literal[
    "ruff",
    "mypy.dmypy",
    "piptools",
    "pip",
    "build",
    "pytest",
    "pip_audit",
    "vulture",
    "pdoc",
]
