"""test command."""

import pathlib
from typing import List, Optional

import click

from pyrgo.utilities.command import PythonExecCommand, inform_and_run_program
from pyrgo.utilities.project import (
    list_pytest_markers,
    read_pyproject,
)


def dynamic_marker_choices() -> List[str]:
    """Dynamic markers for options."""
    cwd = pathlib.Path().cwd()
    content = read_pyproject(cwd=cwd)
    return list_pytest_markers(content=content)


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
@click.option(
    "--no-strict-markers",
    "no_strict_markers",
    type=bool,
    is_flag=True,
    default=False,
    help="Any unknown marks applied with the `@pytest.mark.name_of_mark` decorator will trigger an error.",  # noqa: E501
)
def test(
    *,
    no_strict_markers: bool,
    marker: Optional[str],
) -> None:
    """Execute tests using `pytest`."""
    args_to_add: List[str] = []
    if not no_strict_markers:
        args_to_add.append("--strict-markers")

    if marker:
        args_to_add.extend(["-m", marker])

    inform_and_run_program(
        command=PythonExecCommand(program="pytest").add_args(
            args=args_to_add,
        ),
    )
