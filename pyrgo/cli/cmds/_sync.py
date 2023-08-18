"""Sync command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.cli.cmds._utils import inform_and_run_program
from pyrgo.command_exec import PythonCommandExec
from pyrgo.conf import PyrgoConf


@click.command("sync")
@click.option(
    "-e",
    "--env",
    "env",
    type=click.STRING,
    required=True,
)
@click.option(
    "--editable/--no-editable",
    "editable",
    type=click.BOOL,
    default=True,
    show_default=True,
)
def sync(env: str, *, editable: bool) -> None:
    """Sync current python environment to locked deps."""
    config = PyrgoConf.new()
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
                f"`{env}` not found in available envs.\nAvailable envs: {locked_envs}",  # noqa: E501
                fg="red",
            ),
        )

        sys.exit(1)

    piptools_command = PythonCommandExec.new(program="piptools").add_args(
        args=["sync", config.requirements.joinpath(f"{env}.txt").as_posix()],
    )
    pip_command = PythonCommandExec.new(program="pip").add_args(
        args=["install", "--no-deps"],
    )
    if editable:
        pip_command.add_args(args=["-e"])
    pip_command.add_args(args=["."])

    program_execution = inform_and_run_program(commands=[piptools_command, pip_command])

    if not isinstance(program_execution, Ok):
        sys.exit(1)

    sys.exit(0)
