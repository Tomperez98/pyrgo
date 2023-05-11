"""activate command."""

import pathlib
import sys
from venv import create

import click


def _create_virtual_env(venv_dir: pathlib.Path) -> None:
    create(env_dir=venv_dir)
    click.echo(message=".venv has been created.")


ACTIVATION_MSG: str = (
    "\n```\nTo activate the virtual env run:\n\n"
    "On Windows, run:\n`.venv\\Scripts\\activate.bat`\n\n"
    "On Unix or MacOS, run:\n`source .venv/bin/activate`\n```\n"
)


@click.command
def venv() -> None:
    """Create project virtual environment."""
    cwd = pathlib.Path().cwd()
    venv_dir = cwd.joinpath(".venv")
    if venv_dir.exists():
        if venv_dir.is_dir():
            click.echo(message=".venv already exists.")
            click.echo(ACTIVATION_MSG)

        elif venv_dir.is_file():
            pathlib.Path.unlink(venv_dir)
            _create_virtual_env(venv_dir)
            click.echo(ACTIVATION_MSG)

        else:
            click.echo(".venv for is neither a directory nor a file.")
            sys.exit(1)

    else:
        _create_virtual_env(venv_dir=venv_dir)
        click.echo(ACTIVATION_MSG)
