"""Application contants."""
from __future__ import annotations

from pathlib import Path

from pyrgo.core.models.config import build_config

app_config = build_config(
    cwd=Path().cwd(),
    cache_directories=[
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
    ],
    artifacts_directories=[
        "dist",
        "site",
    ],
    venv_dir=".venv",
    lock_file_format="txt",
    core_deps_alias="core",
)
