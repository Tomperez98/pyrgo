"""lock command."""
import click
import pyrgo


@click.command()
def lock() -> None:
    """Lock dependencies."""
    print(pyrgo.read_pyproject())
