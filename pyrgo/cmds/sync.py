"""Sync command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.command_exec import PythonCommandExec
from pyrgo.conf import PyrgoConf
from pyrgo.utils import ensure_env_exist, inform_and_run_program


@click.command("sync")
@click.option(
    "-e",
    "--env",
    "env",
    type=click.STRING,
    required=True,
)
def sync(env: str) -> None:
    """Sync current python environment to locked deps using `uv`."""
    config = PyrgoConf()
    ensure_env_exist(env=env, config=config, where="lock-files")

    sync_command = PythonCommandExec(
        program="uv",
    ).add_args(
        args=[
            "pip",
            "sync",
            config.requirements.joinpath(f"{env}.txt")
            .relative_to(config.cwd)
            .as_posix(),
        ],
    )
    pip_command = PythonCommandExec(
        program="uv",
    ).add_args(
        args=["pip", "install"],
    )

    pip_command.add_args(args=["-e", "."])

    program_execution = inform_and_run_program(
        commands=[
            sync_command,
            pip_command,
        ]
    )

    if not isinstance(program_execution, Ok):
        sys.exit(1)

    sys.exit(0)
