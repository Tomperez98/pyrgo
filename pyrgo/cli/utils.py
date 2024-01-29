"""CLI utilities."""
from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Literal

import click
from result import Err, Ok, Result
from typing_extensions import assert_never

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


def ensure_env_exist(
    env: str, config: PyrgoConf, where: Literal["lock-files", "pyproject"]
) -> None:
    """Ensure selected env exists in `requirements` folder."""
    if where == "lock-files":
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
    elif where == "pyproject":
        if env not in config.env_groups:
            click.echo(
                message=click.style(
                    f"Environment `{env}` not present in `pyproject.toml`",
                    fg="red",
                )
            )
    else:
        assert_never(where)
