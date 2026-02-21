# agentic-uv - Modern Python Cookiecutter Template

Welcome to the development environment for **agentic-uv**, a cookiecutter template for creating modern Python projects with agent-based development support, strict code quality standards, and full CI/CD automation.

## Project Overview

**agentic-uv** is a cookiecutter template that generates Python projects with:
- ✅ Agent-based development ready (`.claude/` memory structure for Claude Code)
- ✅ Modern best practices (strict type checking, comprehensive linting, security scanning)
- ✅ High test coverage requirements (80%+ enforced)
- ✅ Automated CI/CD (GitHub Actions with security audits)
- ✅ Fast dependency management (uv)
- ✅ Multiple optional features (MkDocs, Docker, codecov, etc.)

## Repository Structure

```
agentic-uv/
├── {{cookiecutter.project_name}}/    ← Template directory (Jinja2 templated files)
│   ├── {{cookiecutter.project_slug}}/
│   │   └── __init__.py              ← User code starts here (empty)
│   ├── .claude/                     ← Agent development guidelines (NEW)
│   │   ├── CLAUDE.md
│   │   └── rules/
│   │       ├── code-style.md
│   │       ├── testing.md
│   │       ├── best-practices.md
│   │       ├── deployment.md
│   │       └── skills.md            ← Agent-based development guide
│   ├── .github/workflows/           ← CI/CD pipelines
│   ├── tests/
│   ├── docs/                        ← Optional MkDocs documentation
│   ├── pyproject.toml              ← Enhanced with stricter configs
│   ├── Makefile                    ← Better targets for testing/coverage
│   ├── tox.ini                     ← With security audit envs
│   └── README.md                   ← Mentions agent-ready setup
│
├── hooks/
│   ├── pre_gen_project.py          ← Template generation hooks
│   └── post_gen_project.py         ← Removes example foo.py (NEW)
│
├── tests/                          ← Tests for the cookiecutter itself
├── docs/                           ← Root documentation
├── cookiecutter.json              ← Updated with Noel's info
├── mkdocs.yml                     ← Updated nav and author
└── README.md                      ← Template info
```

## Key Improvements Made

### 📦 Modern Best Practices (Phase 1)

1. **Enhanced Static Analysis**
   - Added `PIE` (flake8-pie) rule set to ruff
   - Bandit security checking via pre-commit hooks
   - Updated ruff config with 18+ rule sets
   - Stricter mypy config: `disallow_incomplete_defs`, `warn_unreachable`, etc.

2. **Improved Testing & Coverage**
   - Always include `pytest-cov` and `pytest-xdist`
   - Coverage threshold: 80% (fail_under in config)
   - New Makefile targets: `make test-coverage`, `make test-parallel`
   - HTML coverage reports in `coverage_html_report/`
   - Pytest markers for critical tests: `@pytest.mark.coverage`

3. **Stronger Type Checking**
   - Mypy strict mode enforcement (no `Any` without justification)
   - Added config for: `disallow_incomplete_defs`, `warn_unused_configs`, `warn_redundant_casts`, `warn_unreachable`
   - Pretty error output and context

4. **Security & Supply Chain**
   - Added `bandit[toml]` to dependencies
   - New GitHub Actions workflow: `security-audit.yml` (scheduled + manual trigger)
   - Runs bandit + pip-audit weekly
   - Security job in main.yml

### 🤖 Agent-Based Development (Phase 2)

1. **`.claude/` Directory Structure** (Built into every generated project)
   - `CLAUDE.md` - Project overview and quick reference
   - `.claude/rules/*.md` - Modular, topic-specific guidelines:
     - `code-style.md` - Type hints, formatting, naming
     - `testing.md` - Pytest patterns, coverage, fixtures
     - `best-practices.md` - Security, type safety, quality standards
     - `deployment.md` - CI/CD, releases, workflows
     - `skills.md` - Agent-based development guide

2. **Claude Code Integration**
   - Full context for Claude to understand project conventions
   - Guidelines document how to work with agents
   - No Python framework needed—pure markdown instructions
   - Works with both GitHub Copilot and Claude API

3. **Clean Project Structure**
   - `{{cookiecutter.project_slug}}/` starts completely empty (only `__init__.py`)
   - `foo.py` example file removed by `post_gen_project.py`
   - Users start with a blank canvas

4. **Enhanced Documentation**
   - Template README mentions agent-ready setup prominently
   - New docs for agent development features
   - Links to `.claude/rules/` in Makefile output (`make claude-info`)

## Available OpenCode Skills

The `.claude/skills/` directory contains reusable OpenCode skills for agent-based development:

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

## How to Contribute

### Creating New Generated Projects

1. Test the template by generating a sample project:
   ```bash
   cookiecutter . --no-input
   ```

2. Verify the generated project structure:
   ```bash
   cd example-project
   ls -la                    # Check .claude/ exists
   make claude-info          # Verify Claude integration
   make test                 # Run tests
   make check                # Full quality check
   ```

3. Verify `.claude/` files are properly templated:
   - `CLAUDE.md` has correct project name/slug
   - `rules/*.md` reference correct directories
   - No hardcoded paths or secrets

### Modifying Template Files

When editing template files (in `{{cookiecutter.project_name}}/`):

1. Use Jinja2 syntax for conditionals:
   ```jinja2
   {% if cookiecutter.mkdocs == 'y' %}
   # This is included only if mkdocs is enabled
   {% endif %}
   ```

2. Variable references:
   - `{{cookiecutter.project_name}}` - User's project name
   - `{{cookiecutter.project_slug}}` - Python module name (auto-slugified)
   - `{{cookiecutter.author}}` - Author name (Noel Schwabenland by default)
   - Check `cookiecutter.json` for all available variables

3. Keep `.claude/` files in sync with project conventions
   - Edit rules markdown to match code style guidelines
   - Update example code in `.claude/rules/code-style.md`
   - Ensure paths reference correct directories (src/ vs. flat layout)

### Testing Changes

```bash
# Run root project tests
pytest tests/

# Run linting on template files
ruff check .

# Generate test project with different options
cookiecutter . --no-input layout=src type_checker=ty

# Test with all combinations
pytest tests/test_combinations.py
```

## Key Files to Know

| File | Purpose |
|------|---------|
| `cookiecutter.json` | Template variables and choices (author: Noel Schwabenland) |
| `hooks/post_gen_project.py` | Removes files based on user choices; removes `foo.py` |
| `{{cookiecutter.project_name}}/pyproject.toml` | Has enhanced configs (stricter mypy, coverage thresholds, bandit) |
| `{{cookiecutter.project_name}}/.claude/CLAUDE.md` | Generated project's main instructions |
| `{{cookiecutter.project_name}}/.claude/rules/*.md` | Generated project's modular guidelines |
| `docs/` | Root documentation (MkDocs) |
| `mkdocs.yml` | Updated with agent-development feature + Noel's info |

## Common Tasks

### Add a New Rule File to `.claude/rules/`

1. Create template in `{{cookiecutter.project_name}}/.claude/rules/new-rule.md`
2. Update `{{cookiecutter.project_name}}/.claude/CLAUDE.md` to reference it
3. Document in generated project README if major feature
4. Test with `cookiecutter . --no-input` and verify file exists

### Update Linting/Type Checking Standards

1. Modify `{{cookiecutter.project_name}}/pyproject.toml` (the template file)
2. Check template syntax with ruff: `ruff check .`
3. Generate test project and verify: `make check` passes
4. Document changes in `.claude/rules/best-practices.md`

### Add New GitHub Actions Workflow

1. Create in `{{cookiecutter.project_name}}/.github/workflows/`
2. Use Jinja2 to conditionally include based on `cookiecutter.yml` vars
3. Update `hooks/post_gen_project.py` to remove if not needed
4. Document in `.claude/rules/deployment.md` and root docs

## Version & Metadata

- **Current Version:** 0.1.0
- **Author:** Noel Schwabenland (owner of this fork/update)
- **Original Creator:** Florian Maas (fpgmaas/agentic-uv)
- **Python Support:** 3.10 - 3.14
- **Build Tool:** uv (fast Python package manager)

## Documentation Links

- Root docs: See `docs/` directory
- Generated project docs: `{{cookiecutter.project_name}}/docs/` (if mkdocs=y)
- Agent development guide: @.claude/rules/skills.md (template)
- MkDocs config: @../mkdocs.yml

## Quick Start for Development

```bash
# Clone and set up
git clone <repo>
cd agentic-uv
uv sync
uv run pre-commit install

# Generate a test project
cookiecutter . --no-input

# Test generated project
cd example-project
make install
make check
make test

# Back to template work
cd ..
pytest tests/
```

## Notes for Claude

This template is designed to be both:
1. **Easy to use** - Users just answer questions and get a ready-to-use project
2. **Agent-ready** - Generated projects include `.claude/` so Claude can help with development
3. **Best-practices-first** - Strict linting, type checking, and testing enforced from day one

When helping maintain this template:
- Always test changes by generating a sample project
- Verify `.claude/` files Are properly templated (no hardcoded paths)
- Keep Jinja2 conditionals unbroken (many branches for optional features)
- Document changes in root docs for other maintainers
