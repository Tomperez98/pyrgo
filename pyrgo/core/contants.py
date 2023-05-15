"""Application constants."""
CORE_DEPENDENCIES_NAME = "core"

FOLDERS_TO_BE_CLEANED = [
    ".ruff_cache",
    ".mypy_cache",
    ".pytest_cache",
    "site",
    "dist",
]

VENV_ACTIVATION_MSG = (
    "\nTo activate the virtual env run:\n\n"
    "On Windows, run:\n`.venv\\Scripts\\activate.bat`\n\n"
    "On Unix or MacOS, run:\n`source .venv/bin/activate`\n"
)
