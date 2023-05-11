"""Root CLI."""
import click

from pyrgo.command.check import check
from pyrgo.command.clean import clean
from pyrgo.command.fmt import fmt
from pyrgo.command.lock import lock
from pyrgo.command.venv import venv


@click.group()
@click.version_option()
def cli() -> None:
    """pyrgo. Python package manager."""


cli.add_command(cmd=fmt, name="fmt")
cli.add_command(cmd=lock, name="lock")
cli.add_command(cmd=check, name="check")
cli.add_command(cmd=venv, name="venv")
cli.add_command(cmd=clean, name="clean")
