"""Add command."""
from __future__ import annotations

import click
import tomlkit
from tomlkit.items import Item, Table

from pyrgo.core import PyrgoConf


@click.command("add")
@click.option(
    "-e",
    "--env",
    "env",
    type=click.STRING,
    required=True,
    default="core",
    show_default=True,
)
@click.argument("dependency", type=click.STRING)
def add(env: str, dependency: str) -> None:
    """Add dependency to env."""
    conf = PyrgoConf.new()

    pyproject_doc = tomlkit.loads(conf.pyproject_path.read_text())

    project_container = pyproject_doc["project"]
    if not isinstance(project_container, Table):
        msg = "`project` section should be a container"
        raise TypeError(msg)

    if env == "core":
        project_container["dependencies"] = _extend_pyproject_list(
            project_container["dependencies"], new_value=dependency
        )

    else:
        project_optional_deps = project_container["optional-dependencies"]
        if not isinstance(project_optional_deps, Table):
            msg = "`project` section should be a container"
            raise TypeError(msg)

        if env not in conf.env_groups:
            project_optional_deps[env] = []

        project_optional_deps[env] = _extend_pyproject_list(
            pyproject_item=project_optional_deps[env], new_value=dependency
        )

    conf.pyproject_path.write_text(tomlkit.dumps(pyproject_doc, sort_keys=False))


def _extend_pyproject_list(pyproject_item: Item, new_value: str) -> list[str]:
    pyproject_list: list[str] = pyproject_item.unwrap()
    pyproject_list.append(new_value)
    return pyproject_list
