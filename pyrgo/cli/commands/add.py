"""add command."""

import pathlib

import click

from pyrgo.core import ops
from pyrgo.core.contants import CORE_DEPENDENCIES_NAME


@click.command
@click.argument("lib_name", type=str, metavar="<lib_name>")
@click.option(
    "-g",
    "--group",
    "group",
    type=str,
    required=False,
    default=CORE_DEPENDENCIES_NAME,
    help="Group to add new dependency to.",
)
def add(lib_name: str, group: str) -> None:
    """
    Add dependencies to a pyproject.toml manifest file and install.

    \b
    Install packages from:
    - PyPI (and other indexes) using requirement specifiers.
    - VCS project urls.
    - Local project directories.
    - Local or remote source archives.
    """  # noqa: D301
    cwd = pathlib.Path().cwd()
    ops.add.execute(cwd=cwd, new_dependency=lib_name, group=group)
