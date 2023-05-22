"""Python command."""
from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from result import Err, Ok, Result

if TYPE_CHECKING:
    from typing_extensions import Self


@dataclass(
    eq=False,
    frozen=False,
    repr=True,
)
class PythonExecCommand:
    """Command builder."""

    program: str
    args: list[str] = field(init=False)

    def __post_init__(self) -> None:  # noqa: D105
        self.args = [sys.executable, "-m", self.program]

    def add_args(self, args: list[str]) -> Self:
        """Add args to execution."""
        self.args.extend(args)
        return self

    def run(self) -> Result[None, subprocess.CalledProcessError]:
        """Run command."""
        try:
            subprocess.run(args=self.args, check=True)
        except subprocess.CalledProcessError as e:
            return Err(e)

        return Ok()
