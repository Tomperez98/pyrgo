"""clean operation."""
import pathlib
import shutil

from result import Err, Ok, Result

from pyrgo.core.contants import FOLDERS_TO_BE_CLEANED
from pyrgo.core.errors import PyProjectTOMLNotFoundError
from pyrgo.core.models.pyproject import Pyproject


def execute(cwd: pathlib.Path) -> Result[None, PyProjectTOMLNotFoundError]:
    """Execute clean operation."""
    pyproject = Pyproject(cwd=cwd)
    read_pyproject = pyproject.read_pyproject_toml()

    if not isinstance(read_pyproject, Ok):
        return Err(read_pyproject.err())

    for folder in FOLDERS_TO_BE_CLEANED:
        path_to_cache = pyproject.cwd.joinpath(folder)
        if path_to_cache.exists() and path_to_cache.is_dir():
            shutil.rmtree(path_to_cache)
        else:
            continue

    relevant_paths = pyproject.extract_relevant_paths(
        paths_type="all",
    )

    for relevant_path in relevant_paths:
        for pycaches in pyproject.cwd.joinpath(relevant_path).rglob(
            pattern="__pycache__",
        ):
            if pycaches.is_file():
                raise RuntimeError
            shutil.rmtree(pycaches)
    return Ok()
