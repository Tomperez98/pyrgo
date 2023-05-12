"""fmt command."""

import click

from pyrgo.utilities.command import PythonExecCommand, inform_and_run_program


@click.command()
def fmt() -> None:
    """Format all files of the current project using `black` and `ruff`."""
    inform_and_run_program(
        command=PythonExecCommand(program="ruff").add_args(
            args=[
                "--fix-only",
                "tests",
                "pyrgo",
            ],
        ),
    )

    inform_and_run_program(
        command=PythonExecCommand(program="black").add_args(
            args=[
                "tests",
                "pyrgo",
            ],
        ),
    )
