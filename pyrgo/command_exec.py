"""Command execution module."""
from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from result import Err, Ok, Result

if TYPE_CHECKING:
    from typing_extensions import Self, TypeAlias


PyrgoProgram: TypeAlias = Literal[
    "ruff",
    "black",
    "mypy.dmypy",
    "piptools",
    "pip",
    "build",
    "pytest",
    "pip_audit",
]


@dataclass(frozen=False)
class PythonCommandExec:
    """Python command executor."""

    args: list[str]

    @classmethod
    def new(cls: type[PythonCommandExec], program: PyrgoProgram) -> PythonCommandExec:
        """Build a new command executor."""
        return cls(args=[sys.executable, "-m", program])

    def add_args(self, args: list[str]) -> Self:
        """Add arguments to command."""
        self.args.extend(args)
        return self

    def execute(self) -> Result[None, subprocess.CalledProcessError]:
        """Execute python command."""
        try:
            subprocess.run(args=self.args, check=True)
        except subprocess.CalledProcessError as e:
            return Err(e)
        return Ok(None)
