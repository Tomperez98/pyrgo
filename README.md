# pyrgo

[![PyPI downloads](https://img.shields.io/pypi/dm/pyrgo.svg)](https://pypistats.org/packages/pyrgo)

Python project manager inspired in [Cargo](https://doc.rust-lang.org/cargo/).

**`pyrgo` does not reinvent the wheel**. It's just a unified API that leverages popular libraries to improve your development experience.

- Testing:
  - [pytest](https://docs.pytest.org/en/7.3.x/)
- Code formatting:
  - [ruff](https://beta.ruff.rs/docs/)
- Code checking:
  - [ruff](https://beta.ruff.rs/docs/)
  - [mypy](https://mypy.readthedocs.io/en/stable/config_file.html)
  - [vulture](https://github.com/jendrikseipp/vulture)
- Artifacts building:
  - [build](https://pypa-build.readthedocs.io/en/stable/)
- Package management:
  - [pip](https://pip.pypa.io/en/stable/)
  - [pip-tools](https://pip-tools.readthedocs.io/en/latest/)

All behind a unified API.

```zsh
Usage: pyrgo [OPTIONS] COMMAND [ARGS]...

  pyrgo. Python package manager.

Options:
  -v, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  add     Add dependency to env.
  audit   Audit locked dependencies with `pip_audit`.
  build   Build project with `build`.
  check   Check code with `mypy`, `ruff` and `vulture`.
  clean   Clean project repository.
  doc     Build a package's documentation with `pdoc`.
  fix     Automatically fix lint warnings reported by `ruff`.
  fmt     Format code with `ruff`.
  lock    Lock project dependencies with `piptools`.
  new     Create a project.
  remove  Remove dependency from env.
  sync    Sync current python environment to locked deps.
  test    Run tests with `pytest`.
```

The minimal pyrgo project structure, as well as python project structure is this one:

```bash
.
├── README.md
├── pkg
│   └── __init__.py
├── pyproject.toml
└── tests
    └── test_something.py
```


Few extra configurations

```toml
[tool.pyrgo]
extra-paths = ["scripts"]
extra-caches = [".coverage"]
vulture-allowlist = ".allowlist"
```
