"""io utilities."""
from __future__ import annotations

from typing import TYPE_CHECKING
from zipfile import ZipFile

from result import Ok, Result

from pyrgo.core.resources import RESOURCER_PATH

if TYPE_CHECKING:
    from pathlib import Path

    from pyrgo.core.models.config import Config


def prepare_starter_project(
    app_config: Config,
    project_name: str,
    tmp_dir: Path,
) -> Result[Path, Exception]:
    """Unzip and prepare `starter-project` ready to me moved."""
    with ZipFile(
        file=RESOURCER_PATH.joinpath(
            f"{app_config.starter_project}.zip",
        ),
    ) as starter_zip:
        starter_zip.extractall(tmp_dir)
        template_path = tmp_dir.joinpath(
            app_config.starter_project,
        )
        template_path.joinpath("project_name").rename(
            target=template_path.joinpath(project_name),
        )
        template_path.joinpath("pyproject.toml").write_text(
            template_path.joinpath("pyproject.toml")
            .read_text(encoding="UTF-8")
            .replace("project_name", project_name),
        )

    return Ok(template_path)
