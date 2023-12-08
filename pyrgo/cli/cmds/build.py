"""Build command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.cli.utils import inform_and_run_program
from pyrgo.core import PyrgoConf, PythonCommandExec


@click.command("build")
def build() -> None:
    """Build project with `build`."""
    program_execution = inform_and_run_program(
        commands=[
            PythonCommandExec.new(
                program="build",
            ).add_args(
                [PyrgoConf.new().cwd.as_posix()],
            ),
        ],
    )
    if not isinstance(program_execution, Ok):
        sys.exit(1)

    sys.exit(0)
