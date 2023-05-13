"""Root CLI."""

import click

from pyrgo.command.add import add
from pyrgo.command.build import build
from pyrgo.command.check import check
from pyrgo.command.clean import clean
from pyrgo.command.docs import docs
from pyrgo.command.fmt import fmt
from pyrgo.command.init import init
from pyrgo.command.lock import lock
from pyrgo.command.new import new
from pyrgo.command.remove import remove
from pyrgo.command.test import test
from pyrgo.command.venv import venv
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
    ],
)
