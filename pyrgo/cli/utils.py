"""CLI utilities."""
from __future__ import annotations

from typing import TYPE_CHECKING

import click
from result import Err, Ok, Result

if TYPE_CHECKING:
    import subprocess

    from pyrgo.command_exec import PythonCommandExec


def inform_and_run_program(
    commands: list[PythonCommandExec],
) -> Result[None, list[subprocess.CalledProcessError]]:
    """Inform and execute command."""
    subprocess_errors: list[subprocess.CalledProcessError] = []
    for command in commands:
        command_to_execute = " ".join(command.args)
        click.echo(message=click.style(command_to_execute, fg="yellow"), color=True)
        execution_result = command.execute()
        if not isinstance(execution_result, Ok):
            subprocess_errors.append(execution_result.err())

    if len(subprocess_errors) > 0:
        return Err(subprocess_errors)
    return Ok(None)
