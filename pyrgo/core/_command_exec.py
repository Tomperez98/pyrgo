"""Command execution module."""
from __future__ import annotations

import subprocess
import sys
from typing import TYPE_CHECKING, Optional

from result import Err, Ok, Result

if TYPE_CHECKING:
    import pathlib
    from io import TextIOWrapper
    from pathlib import Path

    from typing_extensions import Self

    from pyrgo.typing import PyrgoProgram


class PythonCommandExec:
    """Python command executor."""

    def __init__(
        self,
        program: PyrgoProgram,
    ) -> None:
        """Build a new command executor."""
        self.args: list[str] = [sys.executable, "-m", program]
        self.output_file: Path | None = None

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
        stdout_file: Optional[TextIOWrapper] = None

        if self.output_file is not None:
            stdout_file = self.output_file.open(mode="w")

        try:
            subprocess.run(args=self.args, check=True, stdout=stdout_file)
        except subprocess.CalledProcessError as e:
            return Err(e)
        return Ok(None)
