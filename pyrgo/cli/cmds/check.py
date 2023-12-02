"""Check command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.cli.cmds._utils import inform_and_run_program
from pyrgo.command_exec import PythonCommandExec
from pyrgo.conf import PyrgoConf

VULTURE_WHITELIST = ".whitelist.vulture"


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
    """Check code with `mypy`, `ruff` and `vulture`."""
    configuration = PyrgoConf.new()
    configuration.cwd.joinpath(VULTURE_WHITELIST).touch(exist_ok=True)
    ruff_command = PythonCommandExec.new(
        program="ruff",
    )
    mypy_command = PythonCommandExec.new(
        program="mypy.dmypy",
    ).add_args(
        args=["run", "--timeout", str(timeout), "--"],
    )
    vulture_command = PythonCommandExec.new(
        program="vulture",
    )

    if add_noqa:
        ruff_command.add_args(args=["--add-noqa"])
        vulture_command.add_args(args=["--make-whitelist"]).add_output_file(
            file=configuration.cwd.joinpath(VULTURE_WHITELIST)
        )
    if ignore_noqa:
        ruff_command.add_args(args=["--ignore-noqa"])
    if fix:
        ruff_command.add_args(args=["--unsafe-fixes", "--fix"])

    ruff_command.add_args(configuration.relevant_paths)
    mypy_command.add_args(configuration.relevant_paths)
    vulture_command.add_args(configuration.relevant_paths)
    if not ignore_noqa:
        vulture_command.add_args(args=[VULTURE_WHITELIST])

    program_execution = inform_and_run_program(
        commands=[ruff_command, mypy_command, vulture_command]
    )
    if not isinstance(program_execution, Ok):
        sys.exit(1)

    sys.exit(0)
