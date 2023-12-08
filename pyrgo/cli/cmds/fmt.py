"""Format command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.cli.utils import inform_and_run_program
from pyrgo.core import PyrgoConf, PythonCommandExec


@click.command("fmt")
def fmt() -> None:
    """Format code with `ruff`."""
    configuration = PyrgoConf.new()
    fmt_command = PythonCommandExec.new(
        program="ruff",
    ).add_args(args=["format", "."])
    for command in [fmt_command]:
        command.add_args(args=configuration.relevant_paths)

    program_execution = inform_and_run_program(commands=[fmt_command])
    if not isinstance(program_execution, Ok):
        sys.exit(1)
    sys.exit(0)
