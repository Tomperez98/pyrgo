"""init operation."""
from __future__ import annotations

import shutil
import tempfile
from pathlib import Path
from typing import TYPE_CHECKING

from result import Err, Ok, Result

from pyrgo.core.utilities.io import prepare_starter_project

if TYPE_CHECKING:
    from pyrgo.core.models.config import Config


def execute(
    app_config: Config,
    project_name: str,
) -> Result[None, Exception]:
    """Execute init operation."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        template_path = prepare_starter_project(
            app_config=app_config,
            project_name=project_name,
            tmp_dir=tmp_dir,
        )
        if not isinstance(template_path, Ok):
            return Err(template_path.err())

        shutil.move(
            src=str(template_path.unwrap()),
            dst=str(
                app_config.cwd.joinpath(
                    "tmp",
                ),
            ),
        )

    return Ok()
