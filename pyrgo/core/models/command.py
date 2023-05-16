"""Python command."""
import subprocess
import sys
from typing import List

from result import Err, Ok, Result
from typing_extensions import Self


class PythonExecCommand:
    """Command builder."""

    def __init__(self, program: str) -> None:
        """Python programs to be executed within current python interpreter."""
        self.args = [sys.executable, "-m", program]

    def add_args(self, args: List[str]) -> Self:
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
