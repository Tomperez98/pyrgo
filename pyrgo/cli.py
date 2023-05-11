"""Root CLI."""
import click

from pyrgo.command.fmt import fmt
from pyrgo.command.lock import lock


@click.group()
@click.version_option()
def cli() -> None:
    """pyrgo. Python package manager."""


cli.add_command(
    cmd=fmt,
    name="fmt",
)

cli.add_command(
    cmd=lock,
    name="lock",
)
