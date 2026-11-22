PYTHON ?= python

.PHONY: test format format-check lint lint-fix typecheck check docker-build

test:
	$(PYTHON) -m pytest -q

format:
	$(PYTHON) -m ruff format bot tests

format-check:
	$(PYTHON) -m ruff format --check bot tests

lint:
	$(PYTHON) -m ruff check bot tests

lint-fix:
	$(PYTHON) -m ruff check --fix bot tests

typecheck:
	$(PYTHON) -m mypy bot

check: format-check lint typecheck test

docker-build:
	docker build -t unn-2026-mityaeva .