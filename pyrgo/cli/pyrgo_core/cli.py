"""Root core CLI."""
from __future__ import annotations

import click

from pyrgo.cli.constants import PACKAGE_NAME
from pyrgo.cli.pyrgo_core.commands.add import add
from pyrgo.cli.pyrgo_core.commands.audit import audit
from pyrgo.cli.pyrgo_core.commands.build import build
from pyrgo.cli.pyrgo_core.commands.check import check
from pyrgo.cli.pyrgo_core.commands.clean import clean
from pyrgo.cli.pyrgo_core.commands.docs import docs
from pyrgo.cli.pyrgo_core.commands.fmt import fmt
from pyrgo.cli.pyrgo_core.commands.lock import lock
from pyrgo.cli.pyrgo_core.commands.remove import remove
from pyrgo.cli.pyrgo_core.commands.sync import sync
from pyrgo.cli.pyrgo_core.commands.test import test
from pyrgo.cli.pyrgo_core.commands.venv import venv
from pyrgo.cli.utils import add_commands


@click.group(
    context_settings={
        "help_option_names": [
            "-h",
            "--help",
        ],
        "show_default": True,
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
