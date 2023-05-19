"""audit command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.core import ops
from pyrgo.core.constants import app_config


@click.command
@click.option(
    "-e",
    "--env",
    "environment",
    type=click.Choice(choices=app_config.available_envs),
    required=True,
    help="Audit to one of available enviroments.",
)
@click.option(
    "--fix",
    "fix",
    is_flag=True,
    show_default=True,
    default=False,
    help="Automatically upgrade dependencies with known vulnerabilities",
)
def audit(*, environment: str, fix: bool) -> None:
    """
    Scan project requirements for packages with known vulnerabilities.

    It uses the Python Packaging Advisory Database (https://github.com/pypa/advisory-database)
    """
    executed = ops.audit.execute(
        environment=environment,
        app_config=app_config,
        fix=fix,
    )
    if not isinstance(executed, Ok):
        sys.exit(1)

    sys.exit(0)
