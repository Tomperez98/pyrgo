"""io utilities."""
from __future__ import annotations

from typing import TYPE_CHECKING
from zipfile import ZipFile

from result import Ok, Result

from pyrgo.core.resources import RESOURCER_PATH

if TYPE_CHECKING:
    from pathlib import Path


def prepare_starter_project(
    project_name: str,
    tmp_dir: Path,
) -> Result[Path, Exception]:
    """Unzip and prepare `starter-project` ready to me moved."""
    starter_project = "starter-project"
    with ZipFile(
        file=RESOURCER_PATH.joinpath(
            f"{starter_project}.zip",
        ),
    ) as starter_zip:
        starter_zip.extractall(tmp_dir)
        template_path = tmp_dir.joinpath(
            starter_project,
        )
        formatted_project_name = project_name.lower().replace("-", "_")
        template_path.joinpath("project_name").rename(
            target=template_path.joinpath(formatted_project_name),
        )
        template_path.joinpath("pyproject.toml").write_text(
            template_path.joinpath("pyproject.toml")
            .read_text(encoding="UTF-8")
            .replace("project_name", formatted_project_name),
        )

    return Ok(template_path)
