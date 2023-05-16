"""audit command."""

import click

from pyrgo.cli.utils import dynamic_available_environments


@click.command
@click.option(
    "-env",
    "--environment",
    "environment",
    type=click.Choice(choices=dynamic_available_environments()),
    required=True,
    help="Sync to one of available enviroments.",
)
def audit() -> None:
    """Audit dependencies with `pip-audit`."""
