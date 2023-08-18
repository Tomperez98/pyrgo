"""CLI entrypoint."""
from __future__ import annotations

import click

from pyrgo.cli import cmds


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


cli.add_command(cmd=cmds.lock)
cli.add_command(cmd=cmds.fmt)
cli.add_command(cmd=cmds.check)
cli.add_command(cmd=cmds.sync)
cli.add_command(cmd=cmds.build)
cli.add_command(cmd=cmds.clean)
cli.add_command(cmd=cmds.test)
cli.add_command(cmd=cmds.audit)
cli.add_command(cmd=cmds.new)
