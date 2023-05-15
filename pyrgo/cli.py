"""Root CLI."""

import click

from pyrgo.commands.add import add
from pyrgo.commands.build import build
from pyrgo.commands.check import check
from pyrgo.commands.clean import clean
from pyrgo.commands.docs import docs
from pyrgo.commands.fmt import fmt
from pyrgo.commands.init import init
from pyrgo.commands.lock import lock
from pyrgo.commands.new import new
from pyrgo.commands.remove import remove
from pyrgo.commands.sync import sync
from pyrgo.commands.test import test
from pyrgo.commands.venv import venv
from pyrgo.utils import add_commands


@click.group()
@click.version_option()
def cli() -> None:
    """pyrgo. Python package manager."""


add_commands(
    cli=cli,
    commands=[
        check,
        clean,
        fmt,
        init,
        lock,
        new,
        venv,
        add,
        test,
        docs,
        remove,
        build,
        sync,
    ],
)
