---
name: lint-project
description: Validate code quality by running linting, formatting, and static analysis checks
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: code-quality
---

## What I do

After making code changes, I run the project's linting pipeline to catch quality issues early:

- **Pre-commit checks** - All configured hooks (ruff format, security, etc.)
- **Type checking** - mypy strict mode validation
- **Dependency audit** - deptry for unused/missing dependencies
- **Lock file validation** - Ensures consistency with pyproject.toml

## When to use me

Use this skill **after making code changes**:

1. After implementing a new feature
2. After refactoring existing code
3. After fixing bugs
4. Before committing changes to git
5. When validating pull request changes

## How I work

I execute: `make check`

This Makefile target orchestrates the full linting pipeline defined in your project:

```bash
make check
```

Which runs:
- `uv lock --locked` - Validates lock file
- `uv run pre-commit run -a` - All pre-commit hooks
- `uv run mypy` - Strict type checking
- `uv run deptry .` - Dependency validation

## What I report

I'll show you:
- ✅ **All checks pass** - Your code is ready to commit
- ❌ **Check failures** - Specific linting/type errors with line numbers
- 🔧 **Auto-fix opportunities** - Which issues ruff can fix automatically
- 📋 **Manual fixes needed** - Which issues require your attention

## Common fixes

If `make check` fails:
- **Format errors**: Run `uv run ruff format .` to auto-fix
- **Import issues**: Run `uv run ruff check --fix .` for auto-fixable checks
- **Type errors**: Review the mypy output and add type annotations
- **Unused dependencies**: Remove from pyproject.toml [dependencies]

## Integration tips

After you make changes, ask me to:
- "Load the lint-project skill and check my code"
- "Validate these changes with make check"
- "Run linting on the code I just wrote"

Or I may automatically suggest this skill after you've made code changes.

---

**Related Skills**: `test-project`, `check-project`
