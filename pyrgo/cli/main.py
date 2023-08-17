"""CLI entrypoint."""
from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Literal

import click
from result import Err, Ok, Result

from pyrgo.command_exec import PythonCommandExec
from pyrgo.conf import PyrgoConf

if TYPE_CHECKING:
    import subprocess


def _inform_and_run_program(
    commands: list[PythonCommandExec],
) -> Result[None, list[subprocess.CalledProcessError]]:
    """Inform and execute command."""
    subprocess_errors: list[subprocess.CalledProcessError] = []
    for command in commands:
        command_to_execute = " ".join(command.args)
        click.echo(message=click.style(command_to_execute, fg="yellow"), color=True)
        execution_result = command.execute()
        if not isinstance(execution_result, Ok):
            subprocess_errors.append(execution_result.err())

    if len(subprocess_errors) > 0:
        return Err(subprocess_errors)
    return Ok(None)


@click.group(
    context_settings={
        "help_option_names": [
            "-h",
            "--help",
        ],
        "show_default": True,
    },
)
@click.version_option(None, "-v", "--version")
def cli() -> None:
    """Pyrgo. Python package manager."""


@cli.command("fmt")
def fmt() -> None:
    """Format code with `ruff` and `black`."""
    configuration = PyrgoConf.new()
    ruff_command = PythonCommandExec.new(program="ruff").add_args(args=["--fix-only"])
    black_command = PythonCommandExec.new(program="black")

    for command in [ruff_command, black_command]:
        command.add_args(args=configuration.relevant_paths)

    program_execution = _inform_and_run_program(commands=[ruff_command, black_command])
    if not isinstance(program_execution, Ok):
        sys.exit(1)
    sys.exit(0)


@cli.command("check")
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

    for command in [ruff_command, mypy_command]:
        command.add_args(args=configuration.relevant_paths)

    program_execution = _inform_and_run_program(commands=[ruff_command, mypy_command])
    if not isinstance(program_execution, Ok):
        sys.exit(1)

    sys.exit(0)


@cli.command("lock")
@click.option(
    "-gh",
    "--generate-hashes",
    "generate_hashes",
    is_flag=True,
    default=False,
    show_default=True,
    type=click.BOOL,
)
@click.option(
    "-e",
    "--env",
    "envs",
    multiple=True,
    type=click.STRING,
    required=False,
)
def lock(*, generate_hashes: bool, envs: tuple[str, ...]) -> None:
    """Lock project dependencies with `piptools`."""
    configuration = PyrgoConf.new()
    if not configuration.requirements.exists():
        configuration.requirements.mkdir()

    piptools_cmd = PythonCommandExec.new(program="piptools").add_args(
        args=["compile"],
    )
    if generate_hashes:
        piptools_cmd.add_args(args=["--generate-hashes"])

    piptools_cmd.add_args(
        args=[
            "--resolver=backtracking",
            "-o",
            configuration.requirements.joinpath("core.txt")
            .relative_to(configuration.cwd)
            .as_posix(),
            "pyproject.toml",
        ],
    )

    execution_mode: Literal["all", "specific-group"] = (
        "all" if len(envs) == 0 else "specific-group"
    )

    _ = execution_mode

    raise NotImplementedError
