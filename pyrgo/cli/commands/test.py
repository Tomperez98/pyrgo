"""test command."""

import pathlib
import sys
from typing import List, Optional

import click
from result import Ok

from pyrgo.core import ops
from pyrgo.core.models.pyproject import Pyproject


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
    executed = ops.test.execute(marker=marker)

    if not isinstance(executed, Ok):
        click.echo(message=executed.err())
        sys.exit(1)

    sys.exit(0)
