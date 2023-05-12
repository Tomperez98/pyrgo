"""lock command."""
import click


@click.command()
def lock() -> None:
    """Lock dependencies."""
