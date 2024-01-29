"""CLI entrypoint."""
from __future__ import annotations

import click

from pyrgo.cli.cmds.add import add
from pyrgo.cli.cmds.audit import audit
from pyrgo.cli.cmds.build import build
from pyrgo.cli.cmds.check import check
from pyrgo.cli.cmds.clean import clean
from pyrgo.cli.cmds.doc import doc
from pyrgo.cli.cmds.fix import fix
from pyrgo.cli.cmds.fmt import fmt
from pyrgo.cli.cmds.lock import lock
from pyrgo.cli.cmds.new import new
from pyrgo.cli.cmds.remove import remove
from pyrgo.cli.cmds.sync import sync
from pyrgo.cli.cmds.test import test


@click.group(
    context_settings={
        "help_option_names": [
            "-h",
            "--help",
        ],
        "show_default": True,
    },
)
@click.version_option(None, "-v", "--version")
def cli() -> None:
    """pyrgo. Python package manager."""


cli.add_command(cmd=lock)
cli.add_command(cmd=fmt)
cli.add_command(cmd=check)
cli.add_command(cmd=sync)
cli.add_command(cmd=build)
cli.add_command(cmd=clean)
cli.add_command(cmd=test)
cli.add_command(cmd=audit)
cli.add_command(cmd=new)
cli.add_command(cmd=doc)
cli.add_command(cmd=fix)
cli.add_command(cmd=add)
cli.add_command(cmd=remove)
