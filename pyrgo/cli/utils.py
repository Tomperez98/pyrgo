"""CLI utilities."""
from __future__ import annotations

import sys
from typing import TYPE_CHECKING

import click
from result import Err, Ok, Result

if TYPE_CHECKING:
    import subprocess

    from pyrgo.core import PyrgoConf, PythonCommandExec


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


def ensure_env_exist_in_lock_file(env: str, config: PyrgoConf) -> None:
    """Ensure selected env exists in `requirements` folder."""
    if not config.requirements.exists():
        click.echo(
            message=click.style(
                "No `requirements` folder found. Try locking your deps first",
                fg="red",
            ),
        )
        sys.exit(1)

    locked_envs = config.locked_envs()
    if env not in locked_envs:
        click.echo(
            click.style(
                f"`{env}` not found in available envs.\nAvailable envs: {locked_envs}",
                fg="red",
            ),
        )

        sys.exit(1)
