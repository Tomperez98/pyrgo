"""Root core CLI."""
from __future__ import annotations

import click

from pyrgo.cli.constants import PACKAGE_NAME
from pyrgo.cli.pyrgo.commands.add import add
from pyrgo.cli.pyrgo.commands.audit import audit
from pyrgo.cli.pyrgo.commands.build import build
from pyrgo.cli.pyrgo.commands.check import check
from pyrgo.cli.pyrgo.commands.clean import clean
from pyrgo.cli.pyrgo.commands.docs import docs
from pyrgo.cli.pyrgo.commands.fmt import fmt
from pyrgo.cli.pyrgo.commands.lock import lock
from pyrgo.cli.pyrgo.commands.remove import remove
from pyrgo.cli.pyrgo.commands.sync import sync
from pyrgo.cli.pyrgo.commands.test import test
from pyrgo.cli.pyrgo.commands.venv import venv
from pyrgo.cli.utils import add_commands


@click.group(
    context_settings={
        "help_option_names": [
            "-h",
            "--help",
        ],
    },
)
@click.version_option(
    None,
    "-v",
    "--version",
    package_name=PACKAGE_NAME,
    prog_name=PACKAGE_NAME,
)
def root() -> None:
    """Pyrgo. Python package manager."""


add_commands(
    cli=root,
    commands=[
        check,
        clean,
        fmt,
        lock,
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
