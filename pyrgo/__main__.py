"""CLI entrypoint."""
from __future__ import annotations

import click

from pyrgo.cmds.add import add
from pyrgo.cmds.audit import audit
from pyrgo.cmds.build import build
from pyrgo.cmds.check import check
from pyrgo.cmds.clean import clean
from pyrgo.cmds.doc import doc
from pyrgo.cmds.fix import fix
from pyrgo.cmds.fmt import fmt
from pyrgo.cmds.lock import lock
from pyrgo.cmds.new import new
from pyrgo.cmds.remove import remove
from pyrgo.cmds.sync import sync
from pyrgo.cmds.test import test


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
