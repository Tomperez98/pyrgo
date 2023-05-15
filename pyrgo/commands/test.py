"""test command."""

import pathlib
from typing import List, Optional

import click

from pyrgo.utilities.command import PythonExecCommand, inform_and_run_program
from pyrgo.utilities.project import Pyproject


def dynamic_marker_choices() -> List[str]:
    """Dynamic markers for options."""
    pyproject = Pyproject(cwd=pathlib.Path().cwd())
    pyproject.read_pyproject_toml()
    return pyproject.list_pytest_markers()


@click.command()
@click.option(
    "-m",
    "--marked",
    "marker",
    type=click.Choice(
        choices=dynamic_marker_choices(),
    ),
    default=None,
    help="Run tests based on marks. By default all tests are executed.",
)
def test(
    *,
    marker: Optional[str],
) -> None:
    """Execute tests using `pytest`."""
    args_to_add: List[str] = []

    if marker:
        args_to_add.extend(["-m", marker])

    inform_and_run_program(
        command=PythonExecCommand(program="pytest").add_args(
            args=args_to_add,
        ),
    )
