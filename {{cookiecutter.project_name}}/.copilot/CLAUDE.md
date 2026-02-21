# {{cookiecutter.project_name}} - GitHub Copilot Project Context

Welcome! This is a modern Python project scaffolded with agent-based development best practices.

## Project Overview

**Name:** {{cookiecutter.project_name}}  
**Description:** {{cookiecutter.project_description}}  
**Author:** {{cookiecutter.author}} <{{cookiecutter.email}}>  
**Repository:** https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}

## Where to Start Writing Code

All user-facing code goes in `{{cookiecutter.project_slug}}/` directory. It's completely empty and ready for your implementation.

## Key Project Information

- **Python Version:** 3.10 - 3.14
- **Dependency Manager:** uv (fast Python package installer)
- **Code Quality:** Strict linting (ruff), type checking ({% if cookiecutter.type_checker == "mypy" %}mypy strict mode{% else %}ty{% endif %}), security scanning (bandit)
- **Testing:** pytest with 80%+ coverage requirement
- **Layout:** {% if cookiecutter.layout == "src" %}src layout{% else %}flat layout{% endif %}

## Important Guidelines

Please review these before starting development:

- @.copilot/rules/agent-interaction.md — Required protocol for agent interaction (continuous engagement, no premature session termination)
- @.copilot/rules/commit-guidelines.md — Conventional commits standards for all commits
- @.copilot/rules/code-style.md — Code organization and naming conventions
- @.copilot/rules/testing.md — Testing patterns and coverage expectations
- @.copilot/rules/best-practices.md — Security and quality standards
- @.copilot/rules/deployment.md — CI/CD workflows and release process

## Available OpenCode Skills

The `.copilot/skills/` directory contains reusable OpenCode skills for agent-based development:

### Core Validation Skills
- **lint-project** - Run code quality checks (ruff, mypy, pre-commit)
- **test-project** - Execute test suite with coverage reporting
- **check-project** - Full validation pipeline (lint + test)
- **post-change-validation** - Smart skill recommendation engine

### Development Strategy Skills
- **coding-standards** - Detect code smells, anti-patterns, and readability issues
- **implementation-approach** - Select implementation strategy with risk assessment
- **subagents-orchestration-guide** - Coordinate subagent task distribution

These skills are discoverable by OpenCode and can be loaded dynamically to guide development workflows.

## Quick Commands

- `make install` — Set up development environment
- `make check` — Run all linting and type checking
- `make test` — Run tests with coverage
- `make docs` — Build and serve documentation (if enabled)
- `make help` — See all available commands

## Project Structure

```
{{cookiecutter.project_name}}/
├── {{cookiecutter.project_slug}}/         # ← Your code goes here (empty to start)
├── tests/                         # Test files
├── .copilot/                       # GitHub Copilot Code memory (this directory)
├── docs/                          # Documentation
├── .github/workflows/             # CI/CD pipelines
├── pyproject.toml                 # Project config
├── Makefile                       # Convenient commands
└── README.md                      # Project README
```

## Getting Started

1. Review the code style guide: @.copilot/rules/code-style.md
2. Understand testing conventions: @.copilot/rules/testing.md
3. Read security & best practices: @.copilot/rules/best-practices.md
4. Start writing code in `{{cookiecutter.project_slug}}/`
5. Use `make test` and `make check` during development

## Available Tools

{% if cookiecutter.type_checker == "mypy" -%}
- **Type Checking:** mypy (strict mode) - enforces type hints on all functions and variables
{%- else -%}
- **Type Checking:** ty (Astral's modern type checker) - fast type checking
{%- endif %}
- **Linting & Formatting:** ruff with 17+ rule sets (security, complexity, performance, etc.)
- **Security:** bandit pre-commit hooks
- **Testing:** pytest with coverage reporting
{%- if cookiecutter.deptry == 'y' %}
- **Dependency Management:** deptry checks for unused/missing dependencies
{%- endif %}
{%- if cookiecutter.codecov == 'y' %}
- **Coverage Tracking:** codecov integration in CI/CD
{%- endif %}

## Need Help?

- `make help` — See all make targets
- `README.md` — Quick start and setup instructions
- `.copilot/rules/` — Specific guidelines for different aspects of the project
