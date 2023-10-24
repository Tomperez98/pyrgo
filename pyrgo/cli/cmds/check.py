"""Check command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.cli.cmds._utils import inform_and_run_program
from pyrgo.command_exec import PythonCommandExec
from pyrgo.conf import PyrgoConf


@click.command("check")
@click.option(
    "-t",
    "--timeout",
    "timeout",
    default=360,
    type=click.IntRange(min=60),
)
@click.option(
    "--add-noqa",
    "add_noqa",
    is_flag=True,
    default=False,
    show_default=True,
    type=click.BOOL,
)
@click.option(
    "--ignore-noqa",
    "ignore_noqa",
    is_flag=True,
    default=False,
    show_default=True,
    type=click.BOOL,
)
@click.option(
    "--fix/--no-fix",
    "fix",
    default=False,
    show_default=True,
    type=click.BOOL,
)
def check(*, timeout: int, add_noqa: bool, ignore_noqa: bool, fix: bool) -> None:
    """Check code with `mypy` and `ruff`."""
    configuration = PyrgoConf.new()
    ruff_command = PythonCommandExec.new(program="ruff")
    mypy_command = PythonCommandExec.new(program="mypy.dmypy").add_args(
        args=["run", "--timeout", str(timeout), "--"],
    )

    if add_noqa:
        ruff_command.add_args(args=["--add-noqa"])
    if ignore_noqa:
        ruff_command.add_args(args=["--ignore-noqa"])
    if fix:
        ruff_command.add_args(args=["--unsafe-fixes", "--fix"])

    for command in [ruff_command, mypy_command]:
        command.add_args(args=configuration.relevant_paths)

    program_execution = inform_and_run_program(commands=[ruff_command, mypy_command])
    if not isinstance(program_execution, Ok):
        sys.exit(1)

    sys.exit(0)
