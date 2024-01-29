"""Sync command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.cli.utils import ensure_env_exist, inform_and_run_program
from pyrgo.core import PyrgoConf, PythonCommandExec


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
    ensure_env_exist(env=env, config=config, where="lock-files")

    piptools_command = PythonCommandExec.new(
        program="piptools",
    ).add_args(
        args=[
            "sync",
            config.requirements.joinpath(f"{env}.txt")
            .relative_to(config.cwd)
            .as_posix(),
        ],
    )
    pip_command = PythonCommandExec.new(
        program="pip",
    ).add_args(
        args=["install", "--no-deps"],
    )
    if editable:
        pip_command.add_args(args=["-e"])
    pip_command.add_args(args=["."])

    program_execution = inform_and_run_program(
        commands=[
            piptools_command,
            pip_command,
        ]
    )

    if not isinstance(program_execution, Ok):
        sys.exit(1)

    sys.exit(0)
