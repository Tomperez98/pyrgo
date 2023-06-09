.DEFAULT_GOAL := help
SHELL:=/usr/bin/env bash
OS = $(shell uname | tr A-Z a-z)
sources = pyrgo tests scripts

.PHONY: new-release
new-release: ## Prepare new release for github.
	python scripts/release_github.py

.PHONY: unit
unit: ## Run code unittest.
	python -m pytest -m unit

.PHONY: integration
integration: ## Run code integration tests.
	python -m pytest -m integration

.PHONY: clean
clean: ## Cleans project folder mainly cache
	@rm -rf `find . -name __pycache__`
	@rm -f `find . -type f -name '*.py[co]' `
	@rm -f `find . -type f -name '*~' `
	@rm -f `find . -type f -name '.*~' `
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .ruff_cache
	@rm -rf .mypy_cache
	@rm -rf htmlcov
	@rm -rf *.egg-info
	@rm -f .coverage
	@rm -f .coverage.*
	@rm -f coverage.xml
	@rm -rf build
	@find $(sources) -empty -type d -delete

.PHONY: serve-docs
serve-docs: ## Serve project documentation
	@mkdocs serve

.PHONY: build-docs
build-docs:
	@mkdocs build

.PHONY: lock-dependencies
lock-dependencies: ## Lock dependencies specified in pyproject.toml
	@mkdir -p requirements
	@pip-compile --resolver=backtracking -o requirements/core.txt pyproject.toml
	@pip-compile --extra dev --resolver=backtracking -o requirements/dev.txt pyproject.toml

.PHONY: reload-settings
reload-settings: ## Reload settings from pyproject.toml
	@touch pyproject.toml

.PHONY: help
help:
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'