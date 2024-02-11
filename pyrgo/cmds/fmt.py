"""Format command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.command_exec import PythonCommandExec
from pyrgo.conf import PyrgoConf
from pyrgo.utils import inform_and_run_program


@click.command("fmt")
def fmt() -> None:
    """Format code with `ruff`."""
    configuration = PyrgoConf()
    fmt_command = PythonCommandExec(
        program="ruff",
    ).add_args(args=["format", "."])
    for command in [fmt_command]:
        command.add_args(args=configuration.relevant_paths)

    program_execution = inform_and_run_program(commands=[fmt_command])
    if not isinstance(program_execution, Ok):
        sys.exit(1)
    sys.exit(0)
