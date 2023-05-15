"""docs command."""

import click

from pyrgo.commands.docs.build import build
from pyrgo.commands.docs.new import new
from pyrgo.commands.docs.serve import serve
from pyrgo.utils import add_commands


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
