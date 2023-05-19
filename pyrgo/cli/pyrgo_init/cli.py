"""Root init CLI."""
from __future__ import annotations

import click

from pyrgo.cli.constants import PACKAGE_NAME
from pyrgo.cli.pyrgo_init.commands.new import new
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
        new,
    ],
)
