"""lock command."""
import pathlib
import sys
from typing import List, Tuple

import click
from result import Ok

from pyrgo.core import ops
from pyrgo.core.contants import CORE_DEPENDENCIES_NAME
from pyrgo.core.models.pyproject import Pyproject


def dynamic_group_choices() -> List[str]:
    """Dynamic markers for options."""
    pyproject = Pyproject(cwd=pathlib.Path().cwd())
    pyproject.read_pyproject_toml()
    return [CORE_DEPENDENCIES_NAME, *pyproject.extract_optional_dependencies().keys()]


@click.command()
@click.option(
    "-g",
    "--group",
    "groups",
    type=click.Choice(choices=dynamic_group_choices()),
    multiple=True,
    required=True,
    help="Name of an extras_require group to install; may be used more than once",
)
def lock(groups: Tuple[str]) -> None:
    """Lock dependencies using `piptools`."""
    cwd = pathlib.Path().cwd()
    executed = ops.lock.execute(cwd=cwd, groups=groups)
    if not isinstance(executed, Ok):
        click.echo(message=executed.err())
        sys.exit(1)
    sys.exit(0)
