"""Root init CLI."""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

import click
from result import Ok

from pyrgo.core.utilities.io import prepare_starter_project


@click.command(
    context_settings={
        "help_option_names": [
            "-h",
            "--help",
        ],
    },
)
@click.argument("path", type=click.Path())
@click.option(
    "-n",
    "--name",
    "name",
    type=click.STRING,
    required=True,
    help="New project name.",
)
def new(path: str, name: str) -> None:
    """Initialize a new Pyrgo project."""
    path_as_path = Path(path)
    with tempfile.TemporaryDirectory() as tmp:
        template_path = prepare_starter_project(
            project_name=name,
            tmp_dir=Path(tmp),
        )
        if not isinstance(template_path, Ok):
            click.echo(template_path.err())
            sys.exit(1)

        if not path_as_path.exists():
            path_as_path.mkdir()

        template_path.unwrap().rename(path_as_path.absolute())
