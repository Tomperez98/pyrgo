"""Fix command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.cli.utils import inform_and_run_program
from pyrgo.command_exec import PythonCommandExec
from pyrgo.conf import PyrgoConf


@click.command("fix")
def fix() -> None:
    """Automatically fix lint warnings reported by `ruff`."""
    configuration = PyrgoConf()
    ruff_command = (
        PythonCommandExec(
            program="ruff",
        )
        .add_args(args=["--unsafe-fixes", "--fix"])
        .add_args(configuration.relevant_paths)
    )

    program_execution = inform_and_run_program(
        commands=[
            ruff_command,
        ]
    )
    if not isinstance(program_execution, Ok):
        sys.exit(1)

    sys.exit(0)
