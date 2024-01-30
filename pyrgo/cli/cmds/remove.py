"""Remove command."""
from __future__ import annotations

import click
import tomlkit
from packaging.requirements import Requirement
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

        new_deps = _remove_from_pyproject_list(
            pyproject_item=project_optional_deps[env], value_to_remove=dependency
        )
        if len(new_deps) > 0:
            project_optional_deps[env] = new_deps
        else:
            project_optional_deps.pop(env)

    conf.pyproject_path.write_text(tomlkit.dumps(pyproject_doc, sort_keys=False))


def _remove_from_pyproject_list(
    pyproject_item: Item, value_to_remove: str
) -> list[str]:
    pyproject_dependencies: dict[str, str] = {
        Requirement(x).name: x for x in pyproject_item.unwrap()
    }
    if value_to_remove in pyproject_dependencies:
        pyproject_dependencies.pop(value_to_remove)

    return list(pyproject_dependencies.values())
