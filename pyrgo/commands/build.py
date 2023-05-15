"""build command."""

import click

from pyrgo.utilities.command import PythonExecCommand, inform_and_run_program


@click.command
def build() -> None:
    """Build project."""
    inform_and_run_program(
        command=PythonExecCommand(program="hatch").add_args(
            args=[
                "build",
            ],
        ),
    )
