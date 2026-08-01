#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = app
PYTHON_VERSION = 3.12.3
PYTHON_INTERPRETER = python3

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Sync dependencies
.PHONY: venv
venv:
	uv sync --locked

## Delete compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using ruff
.PHONY: lint
lint:
	uv run ruff format --check
	uv run ruff check

## Lint fix source code with ruff
.PHONY: lint-fix
lint-fix:
	uv run ruff check --fix
	uv run ruff format

# ## Run tests
# .PHONY: test
# test:
# 	uv run pytest tests

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)