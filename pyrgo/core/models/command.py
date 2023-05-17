"""Python command."""
import subprocess
import sys
from dataclasses import dataclass, field
from typing import List

from result import Err, Ok, Result
from typing_extensions import Self


@dataclass(
    eq=False,
    frozen=False,
    repr=True,
)
class PythonExecCommand:
    """Command builder."""

    program: str
    args: List[str] = field(init=False)

    def __post_init__(self) -> None:  # noqa: D105
        self.args = [sys.executable, "-m", self.program]

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
