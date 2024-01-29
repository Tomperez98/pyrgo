"""Test command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.cli.utils import inform_and_run_program
from pyrgo.core import PythonCommandExec


@click.command("test")
@click.option(
    "-m",
    "marker",
    type=click.STRING,
    default=None,
    show_default=True,
)
def test(marker: str | None) -> None:
    """Run tests with `pytest`."""
    pytest_command = PythonCommandExec.new(
        program="pytest",
    )
    if marker is not None:
        pytest_command.add_args(args=["-m", marker])
    program_execution = inform_and_run_program(commands=[pytest_command])
    if not isinstance(program_execution, Ok):
        sys.exit(1)

    sys.exit(0)
