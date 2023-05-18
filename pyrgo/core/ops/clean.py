"""clean operation."""
import itertools
import shutil

from result import Ok, Result

from pyrgo.core.models.config import Config


def execute(app_config: Config) -> Result[None, Exception]:
    """Execute clean operation."""
    for to_be_clean in itertools.chain(
        app_config.caches,
        app_config.artifacts,
    ):
        if to_be_clean.exists() and to_be_clean.is_dir():
            shutil.rmtree(to_be_clean)

    for relevant_path in app_config.relevant_paths:
        for pycaches in app_config.cwd.joinpath(relevant_path).rglob(
            pattern="__pycache__",
        ):
            shutil.rmtree(pycaches)

    return Ok()
