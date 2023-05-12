"""test command."""

from typing import Optional

import click

from pyrgo.utilities.command import PythonExecCommand, inform_and_run_program


@click.command()
@click.option(
    "-m",
    "--marked",
    "marker",
    type=click.Choice(
        choices=[
            "unit",
            "integration",
        ],
    ),
    default=None,
    help="Run tests based on marks. By default all tests are executed.",
)
def test(marker: Optional[str] = None) -> None:
    """Execute tests using `pytest`."""
    args_to_add = ["tests"]
    if marker:
        args_to_add.extend(["-m", marker])

    inform_and_run_program(
        command=PythonExecCommand(program="pytest").add_args(
            args=args_to_add,
        ),
    )
