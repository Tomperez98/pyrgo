"""command utilities."""
import subprocess
import sys
from typing import Literal

import click
from typing_extensions import Self


class PythonExecCommand:
    """Command builder."""

    def __init__(self, program: str) -> None:
        """Python programs to be executed within current python interpreter."""
        self.program = program
        self.args = [sys.executable, "-m", program]

    def add_args(self, args: list[str]) -> Self:
        """Add args to execution."""
        self.args.extend(args)
        return self

    def run(self) -> None:
        """Run command."""
        subprocess.run(args=self.args)


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


def inform_and_run_program(command: PythonExecCommand) -> None:
    """Inform and run program."""
    click.echo(
        message=colorize_text(
            text=f"running {command.program}...",
            color="yellow",
        ),
    )
    command.run()
