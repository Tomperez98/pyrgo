"""docs command."""

import click

from pyrgo.cli.commands.docs.build import build
from pyrgo.cli.commands.docs.new import new
from pyrgo.cli.commands.docs.serve import serve
from pyrgo.cli.utils import add_commands


@click.group()
def docs() -> None:
    """Document you project."""


add_commands(
    cli=docs,
    commands=[
        serve,
        build,
        new,
    ],
)
