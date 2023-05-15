"""command utilities."""
import subprocess
import sys
from typing import List

import click
from typing_extensions import Self

from pyrgo.utilities.text import colorize_text


class PythonExecCommand:
    """Command builder."""

    def __init__(self, program: str) -> None:
        """Python programs to be executed within current python interpreter."""
        self.program = program
        self.args = [sys.executable, "-m", program]

    def add_args(self, args: List[str]) -> Self:
        """Add args to execution."""
        self.args.extend(args)
        return self

    def run(self) -> None:
        """Run command."""
        subprocess.run(args=self.args)


def inform_and_run_program(command: PythonExecCommand) -> None:
    """Inform and run program."""
    click.echo(
        message=colorize_text(
            text=f"running {command.program}...",
            color="yellow",
        ),
    )
    command.run()
