"""command utilities."""
import sys
from typing import List

import click
from result import Ok

from pyrgo.core.models.command import PythonExecCommand
from pyrgo.core.utilities.text import colorize_text


def inform_and_run_program(commands: List[PythonExecCommand]) -> None:
    """Inform and run program."""
    execution_failed = False
    for command in commands:
        command_to_be_executed = " ".join(command.args)
        click.echo(
            message=colorize_text(
                text=f"Running {command_to_be_executed}",
                color="yellow",
            ),
        )
        executed = command.run()
        if not isinstance(executed, Ok):
            execution_failed = True

    if execution_failed:
        sys.exit(1)
