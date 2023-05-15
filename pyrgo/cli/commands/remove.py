"""remove command."""
import click


@click.command()
def remove() -> None:
    """Remove dependencies from the manifest file."""
