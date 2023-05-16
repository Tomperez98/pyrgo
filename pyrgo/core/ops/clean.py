"""clean operation."""
import shutil

from result import Ok, Result

from pyrgo.core.config import app_config


def execute() -> Result[None, Exception]:
    """Execute clean operation."""
    for cache in app_config.caches_paths:
        if cache.exists() and cache.is_dir():
            shutil.rmtree(cache)
        else:
            continue

    for artifact in app_config.artifacts_paths:
        if artifact.exists() and artifact.is_dir():
            shutil.rmtree(artifact)
        else:
            continue

    relevant_paths = app_config.pyproject_toml.extract_relevant_paths(
        paths_type="all",
    )

    for relevant_path in relevant_paths:
        for pycaches in app_config.cwd.joinpath(relevant_path).rglob(
            pattern="__pycache__",
        ):
            if pycaches.is_file():
                raise RuntimeError
            shutil.rmtree(pycaches)
    return Ok()
