# {{cookiecutter.project_name}}

[![Release](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![Build status](https://img.shields.io/github/actions/workflow/status/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/main.yml?branch=main)](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/actions/workflows/main.yml?query=branch%3Amain)
{% if cookiecutter.codecov == "y" -%}
[![codecov](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
{%- endif %}
[![Commit activity](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![License](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})

{{cookiecutter.project_description}}

- **Github repository**: <https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/>
{%- if cookiecutter.mkdocs == "y" %}
- **Documentation**: <https://{{cookiecutter.author_github_handle}}.github.io/{{cookiecutter.project_name}}/>
{%- endif %}

## 🚀 Agent-Ready Development

This project is configured for **agent-based development** with Claude. All project guidelines, testing patterns, and code style conventions are documented in `.claude/` for Claude Code:

- **Code Style:** `.claude/rules/code-style.md` - Type hints, formatting, organization
- **Testing Guide:** `.claude/rules/testing.md` - 80%+ coverage requirements, patterns
- **Best Practices:** `.claude/rules/best-practices.md` - Security, type checking, quality
- **Deployment:** `.claude/rules/deployment.md` - CI/CD and release workflows

Open this project in Claude Code to get full context and assistance automatically!

## Getting Started

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}.git
git push -u origin main
```

### 2. Set Up Your Development Environment

Install the environment and pre-commit hooks:

```bash
make install
```

This will also generate your `uv.lock` file.

### 3. Run Pre-Commit Hooks

The CI/CD pipeline might initially fail due to formatting. Fix issues with:

```bash
uv run pre-commit run -a
```

### 4. Commit the Changes

Commit the formatting fixes:

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

**You're ready to start development!** The CI/CD pipeline will run when you open PRs, merge to main, or create releases.

## Available Commands

```bash
make help              # Show all available commands
make install           # Set up development environment
make check             # Run linting, type checking, and tests
make test              # Run tests with coverage
make test-coverage     # Generate HTML coverage report
make test-parallel     # Run tests in parallel
make claude-info       # Show Claude Code integration info
{% if cookiecutter.mkdocs == "y" -%}
make docs              # Build and serve documentation
make docs-test         # Test documentation builds
{%- endif %}
```

## Code Quality Standards

✓ **Type Checking:** {% if cookiecutter.type_checker == "mypy" %}mypy (strict mode){% else %}ty{% endif %} - All code must be fully typed
✓ **Linting:** ruff with 18+ rule sets
✓ **Security:** bandit pre-commit hooks + pip-audit in CI/CD
✓ **Testing:** pytest with 80%+ coverage requirement
{%- if cookiecutter.deptry == "y" %}
✓ **Dependencies:** deptry checks for unused/missing deps
{%- endif %}
✓ **Formatting:** Automatic with ruff

## Releasing a New Version

{% if cookiecutter.publish_to_pypi == "y" -%}

1. Create an API Token on [PyPI](https://pypi.org/)
2. Add it to your project secrets as `PYPI_TOKEN` on GitHub
3. Create a [new release](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/releases/new)
4. Create a tag in the form `v*.*.*`

The CI/CD pipeline will automatically build and publish to PyPI.
{%- else -%}

1. Update the version in `pyproject.toml`
2. Create a [new release](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/releases/new)
3. Create a tag in the form `v*.*.*`

The CI/CD pipeline will build a release package automatically.
{%- endif %}

See `.claude/rules/deployment.md` for detailed release procedures.

---

Repository created with [agentic-uv](https://github.com/noelschwabenland/agentic-uv) by Noel Schwabenland.

