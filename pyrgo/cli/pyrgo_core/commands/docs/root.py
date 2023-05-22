"""docs command."""
from __future__ import annotations

import click

from pyrgo.cli.pyrgo_core.commands.docs.build import build
from pyrgo.cli.pyrgo_core.commands.docs.new import new
from pyrgo.cli.pyrgo_core.commands.docs.serve import serve
from pyrgo.cli.utils import add_commands


@click.group()
def docs() -> None:
    """Document you project with `mkdocs-material`."""


add_commands(
    cli=docs,
    commands=[
        serve,
        build,
        new,
    ],
)
