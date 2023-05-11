"""lock command."""
import click

from pyrgo import _pyrgo


@click.command()
def lock() -> None:
    """Lock dependencies."""
    pyproject_content = _pyrgo.read_pyproject()
    click.echo(pyproject_content)
