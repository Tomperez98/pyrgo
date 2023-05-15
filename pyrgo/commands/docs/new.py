"""docs new command."""

import pathlib
import sys

import click

from pyrgo.utilities.command import (
    PythonExecCommand,
    inform_and_run_program,
)
from pyrgo.utilities.text import colorize_text


@click.command()
def new() -> None:
    """Create a new MkDocs project."""
    cwd = pathlib.Path().cwd()
    pyproject = cwd.joinpath("pyproject.toml")
    if not pyproject.exists():
        click.echo(
            message=colorize_text(
                text="pyproject.toml not found.",
                color="red",
            ),
        )
        sys.exit(1)

    inform_and_run_program(
        command=PythonExecCommand(program="mkdocs").add_args(
            [
                "new",
                str(cwd),
            ],
        ),
    )
