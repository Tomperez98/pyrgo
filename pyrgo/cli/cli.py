"""Root CLI."""

import click

from pyrgo.cli.commands.add import add
from pyrgo.cli.commands.audit import audit
from pyrgo.cli.commands.build import build
from pyrgo.cli.commands.check import check
from pyrgo.cli.commands.clean import clean
from pyrgo.cli.commands.docs import docs
from pyrgo.cli.commands.fmt import fmt
from pyrgo.cli.commands.init import init
from pyrgo.cli.commands.lock import lock
from pyrgo.cli.commands.new import new
from pyrgo.cli.commands.remove import remove
from pyrgo.cli.commands.sync import sync
from pyrgo.cli.commands.test import test
from pyrgo.cli.commands.venv import venv
from pyrgo.cli.utils import add_commands


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=False,
)
@click.version_option(prog_name="Pyrgo")
def root() -> None:
    """Pyrgo. Python package manager."""


add_commands(
    cli=root,
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
        audit,
    ],
)
