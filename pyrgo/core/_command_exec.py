"""Command execution module."""
from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from typing import TYPE_CHECKING

from result import Err, Ok, Result

if TYPE_CHECKING:
    import pathlib
    from io import TextIOWrapper

    from typing_extensions import Self

    from pyrgo.typing import PyrgoProgram


@dataclass(frozen=False)
class PythonCommandExec:
    """Python command executor."""

    args: list[str]
    output_file: pathlib.Path | None

    @classmethod
    def new(
        cls: type[PythonCommandExec],
        program: PyrgoProgram,
    ) -> PythonCommandExec:
        """Build a new command executor."""
        return cls(args=[sys.executable, "-m", program], output_file=None)

    def add_output_file(self, file: pathlib.Path) -> Self:
        """Add output file to command."""
        self.output_file = file
        return self

    def add_args(self, args: list[str]) -> Self:
        """Add arguments to command."""
        self.args.extend(args)
        return self

    def execute(self) -> Result[None, subprocess.CalledProcessError]:
        """Execute python command."""
        stdout_file: None | TextIOWrapper = None

        if self.output_file is not None:
            stdout_file = self.output_file.open(mode="w")

        try:
            subprocess.run(args=self.args, check=True, stdout=stdout_file)
        except subprocess.CalledProcessError as e:
            return Err(e)
        return Ok(None)
