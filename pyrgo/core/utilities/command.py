"""command utilities."""
import subprocess
import sys
from typing import List

import click
from result import Err, Ok, Result
from typing_extensions import Self

from pyrgo.core.utilities.text import colorize_text


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

    def run(self) -> Result[None, subprocess.CalledProcessError]:
        """Run command."""
        command_to_be_executed = " ".join(self.args)
        click.echo(
            message=colorize_text(
                text=f"Running {command_to_be_executed}",
                color="yellow",
            ),
        )
        try:
            subprocess.run(args=self.args, check=True)
        except subprocess.CalledProcessError as e:
            return Err(e)

        return Ok()


def inform_and_run_program(commands: List[PythonExecCommand]) -> None:
    """Inform and run program."""
    execution_failed = False
    for command in commands:
        executed = command.run()
        if not isinstance(executed, Ok):
            execution_failed = True

    if execution_failed:
        sys.exit(1)
