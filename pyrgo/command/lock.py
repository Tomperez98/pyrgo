"""lock command."""
import click

from pyrgo import _pyrgo


@click.command()
def lock() -> None:
    """Lock dependencies."""
    print(dir(_pyrgo))

    print(_pyrgo.read_pyproject())
