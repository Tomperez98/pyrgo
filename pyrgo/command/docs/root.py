"""docs command."""

import click

from pyrgo.command.docs.build import build
from pyrgo.command.docs.new import new
from pyrgo.command.docs.serve import serve
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
