"""sync command."""
import click


@click.command
def sync() -> None:
    """Synchronize virtual environment with requirements.txt."""
