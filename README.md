# engg-math-template

Template for packages in the Engineering Mathematics ecosystem. Use **"Use this template"** on GitHub, then follow the checklist below.

## New-package checklist

1. Rename: repo `<name>` (kebab-case) → distribution `engg-math-<name>` → import `engg_math.<name_snake>`.
   Rename `src/engg_math/template/`, and update `pyproject.toml` (`name`, `importlinter`), `__init__.py`, `tests/`.
2. Never add `src/engg_math/__init__.py`. The `engg_math` namespace is shared between distributions.
3. Declare the public API in `__all__`; keep implementation in `_private.py` modules.
4. Keep `[project].dependencies` minimal; put optional features behind extras.
5. Set `CODEOWNERS`, branch protection (see `Meta/GOVERNANCE.md`), and register a PyPI Trusted Publisher.
6. `uv sync` → `uv run pytest` must pass on a fresh clone.

## Development

```bash
uv sync                          # create .venv from uv.lock
uv run ruff check . && uv run ruff format --check .
uv run mypy
uv run lint-imports
uv run pytest
```

CI runs these plus a lowest-dependency run, a 3-OS matrix, a dependency audit, CodeQL and a commit-policy check.

Licence: Apache-2.0.
