"""lock command."""
import sys
from typing import List, Tuple

import click
from result import Ok

from pyrgo.core import ops
from pyrgo.core.config import app_config
from pyrgo.core.models.pyproject import Pyproject


def dynamic_group_choices() -> List[str]:
    """Dynamic markers for options."""
    pyproject = Pyproject()
    pyproject.read_pyproject_toml(pyproject_path=app_config.pyproject_toml_path)
    return [
        app_config.core_dependecies_name,
        *pyproject.extract_optional_dependencies().keys(),
    ]


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
    executed = ops.lock.execute(groups=groups)
    if not isinstance(executed, Ok):
        click.echo(message=executed.err())
        sys.exit(1)
    sys.exit(0)
