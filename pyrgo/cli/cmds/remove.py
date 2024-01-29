"""Remove command."""
from __future__ import annotations

import click
import tomlkit
from tomlkit.items import Item, Table

from pyrgo.cli.utils import ensure_env_exist
from pyrgo.core import PyrgoConf


@click.command("remove")
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
def remove(env: str, dependency: str) -> None:
    """Remove dependency from env."""
    conf = PyrgoConf.new()
    ensure_env_exist(env=env, config=conf, where="pyproject")
    pyproject_doc = tomlkit.loads(conf.pyproject_path.read_text())

    project_container = pyproject_doc["project"]
    if not isinstance(project_container, Table):
        msg = "`project` section should be a container"
        raise TypeError(msg)

    if env == "core":
        project_container["dependencies"] = _remove_from_pyproject_list(
            project_container["dependencies"], value_to_remove=dependency
        )

    else:
        project_optional_deps = project_container["optional-dependencies"]
        if not isinstance(project_optional_deps, Table):
            msg = "`project` section should be a container"
            raise TypeError(msg)

        project_optional_deps[env] = _remove_from_pyproject_list(
            pyproject_item=project_optional_deps[env], value_to_remove=dependency
        )

    conf.pyproject_path.write_text(tomlkit.dumps(pyproject_doc, sort_keys=False))


def _remove_from_pyproject_list(
    pyproject_item: Item, value_to_remove: str
) -> list[str]:
    pyproject_list: list[str] = pyproject_item.unwrap()
    pyproject_list.remove(value_to_remove)
    return pyproject_list
