"""command utilities."""
from __future__ import annotations

from typing import TYPE_CHECKING

import click
from result import Err, Ok, Result

if TYPE_CHECKING:
    import subprocess

    from pyrgo.core.models.command import PythonExecCommand
from pyrgo.core.utilities.text import colorize_text


def inform_and_run_program(
    commands: list[PythonExecCommand],
) -> Result[None, list[subprocess.CalledProcessError]]:
    """Inform and run program."""
    execution_failed = False
    subprocess_errors: list[subprocess.CalledProcessError] = []
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
            subprocess_errors.append(executed.err())

    if execution_failed:
        return Err(subprocess_errors)

    return Ok()
