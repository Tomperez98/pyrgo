"""check command."""


import click

from pyrgo.utilities.command import PythonExecCommand, inform_and_run_program


@click.command()
def check() -> None:
    """Analyze the current package with `ruff` and `mypy`."""
    inform_and_run_program(
        command=PythonExecCommand(program="ruff").add_args(
            args=[
                "tests",
                "pyrgo",
            ],
        ),
    )
    inform_and_run_program(
        command=PythonExecCommand(program="mypy").add_args(
            args=[
                "tests",
                "pyrgo",
            ],
        ),
    )
