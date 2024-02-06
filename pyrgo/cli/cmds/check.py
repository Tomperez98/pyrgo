"""Check command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.cli.utils import inform_and_run_program
from pyrgo.core import PyrgoConf, PythonCommandExec


def _build_vulture_cmd(
    *,
    add_noqa: bool,
    ignore_noqa: bool,
    configuration: PyrgoConf,
    vulture_allowlist: str,
) -> PythonCommandExec:
    configuration.cwd.joinpath(vulture_allowlist).touch(exist_ok=True)
    vulture_command = PythonCommandExec.new(
        program="vulture",
    )
    if add_noqa:
        vulture_command.add_args(args=["--make-whitelist"]).add_output_file(
            file=configuration.cwd.joinpath(vulture_allowlist)
        )

    vulture_command.add_args(configuration.relevant_paths)
    if not ignore_noqa:
        vulture_command.add_args(args=[vulture_allowlist])

    return vulture_command


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
def check(*, timeout: int, add_noqa: bool, ignore_noqa: bool) -> None:
    """Check code with `mypy`, `ruff` and `vulture`."""
    configuration = PyrgoConf.new()
    ruff_command = PythonCommandExec.new(
        program="ruff",
    )
    mypy_command = PythonCommandExec.new(
        program="mypy.dmypy",
    ).add_args(
        args=["run", "--timeout", str(timeout), "--"],
    )

    if add_noqa:
        ruff_command.add_args(args=["--add-noqa"])
    if ignore_noqa:
        ruff_command.add_args(args=["--ignore-noqa"])

    ruff_command.add_args(configuration.relevant_paths)
    mypy_command.add_args(configuration.relevant_paths)

    program_execution = inform_and_run_program(
        commands=[
            ruff_command,
            mypy_command,
            _build_vulture_cmd(
                add_noqa=add_noqa,
                ignore_noqa=ignore_noqa,
                configuration=configuration,
                vulture_allowlist=configuration.vulture_allowlist.as_posix(),
            ),
        ]
    )
    if not isinstance(program_execution, Ok):
        sys.exit(1)

    sys.exit(0)
