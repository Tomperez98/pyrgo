"""check command."""
import click


@click.command()
def check() -> None:
    """Analyze the current package and report errors."""
