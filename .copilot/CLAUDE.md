# agentic-uv - Modern Python Cookiecutter Template

Welcome to the development environment for **agentic-uv**, a cookiecutter template for creating modern Python projects with agent-based development support, strict code quality standards, and full CI/CD automation.

## Project Overview

**agentic-uv** is a cookiecutter template that generates Python projects with:
- ✅ Agent-based development ready (`.copilot/` memory structure for GitHub Copilot Code)
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
│   ├── .copilot/                     ← Agent development guidelines (NEW)
│   │   ├── COPILOT.md
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

1. **`.copilot/` Directory Structure** (Built into every generated project)
   - `COPILOT.md` - Project overview and quick reference
   - `.copilot/rules/*.md` - Modular, topic-specific guidelines:
     - `code-style.md` - Type hints, formatting, naming
     - `testing.md` - Pytest patterns, coverage, fixtures
     - `best-practices.md` - Security, type safety, quality standards
     - `deployment.md` - CI/CD, releases, workflows
     - `skills.md` - Agent-based development guide

2. **GitHub Copilot Code Integration**
   - Full context for GitHub Copilot to understand project conventions
   - Guidelines document how to work with agents
   - No Python framework needed—pure markdown instructions
   - Works with both GitHub Copilot and GitHub Copilot API

3. **Clean Project Structure**
   - `{{cookiecutter.project_slug}}/` starts completely empty (only `__init__.py`)
   - `foo.py` example file removed by `post_gen_project.py`
   - Users start with a blank canvas

4. **Enhanced Documentation**
   - Template README mentions agent-ready setup prominently
   - New docs for agent development features
   - Links to `.copilot/rules/` in Makefile output (`make claude-info`)

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

## Subagent Definitions

The `.copilot/agents/` directory contains prompt definitions for all subagents referenced by the `subagents-orchestration-guide` skill:

### Implementation Support Agents
- **task-executor** - Executes a single implementation task and returns structured JSON
- **quality-fixer** - Runs the full QA pipeline and self-heals until all checks pass
- **task-decomposer** - Breaks a work plan into atomic, ordered implementation tasks
- **integration-test-reviewer** - Reviews integration/E2E tests against skeletons

### Document Creation Agents
- **requirement-analyzer** - Analyzes requirements and determines work scale
- **prd-creator** - Creates or updates Product Requirements Documents
- **technical-designer** - Creates ADRs and Design Docs from approved requirements
- **work-planner** - Creates phased implementation work plans from Design Docs
- **document-reviewer** - Reviews documents for quality and completeness
- **design-sync** - Verifies consistency across all Design Docs for a feature
- **acceptance-test-generator** - Generates integration/E2E test skeletons from Design Doc ACs

Each agent definition specifies its role, input expectations, responsibilities, output JSON format, and prohibited actions. The orchestrator (main Copilot session) coordinates these agents — agents cannot call each other directly.

## How to Contribute

### Creating New Generated Projects

1. Test the template by generating a sample project:
   ```bash
   cookiecutter . --no-input
   ```

2. Verify the generated project structure:
   ```bash
   cd example-project
   ls -la                    # Check .copilot/ exists
   make claude-info          # Verify GitHub Copilot integration
   make test                 # Run tests
   make check                # Full quality check
   ```

3. Verify `.copilot/` files are properly templated:
   - `COPILOT.md` has correct project name/slug
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

3. Keep `.copilot/` files in sync with project conventions
   - Edit rules markdown to match code style guidelines
   - Update example code in `.copilot/rules/code-style.md`
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
| `{{cookiecutter.project_name}}/.copilot/COPILOT.md` | Generated project's main instructions |
| `{{cookiecutter.project_name}}/.copilot/rules/*.md` | Generated project's modular guidelines |
| `docs/` | Root documentation (MkDocs) |
| `mkdocs.yml` | Updated with agent-development feature + Noel's info |

## Common Tasks

### Add a New Rule File to `.copilot/rules/`

1. Create template in `{{cookiecutter.project_name}}/.copilot/rules/new-rule.md`
2. Update `{{cookiecutter.project_name}}/.copilot/COPILOT.md` to reference it
3. Document in generated project README if major feature
4. Test with `cookiecutter . --no-input` and verify file exists

### Update Linting/Type Checking Standards

1. Modify `{{cookiecutter.project_name}}/pyproject.toml` (the template file)
2. Check template syntax with ruff: `ruff check .`
3. Generate test project and verify: `make check` passes
4. Document changes in `.copilot/rules/best-practices.md`

### Add New GitHub Actions Workflow

1. Create in `{{cookiecutter.project_name}}/.github/workflows/`
2. Use Jinja2 to conditionally include based on `cookiecutter.yml` vars
3. Update `hooks/post_gen_project.py` to remove if not needed
4. Document in `.copilot/rules/deployment.md` and root docs

## Version & Metadata

- **Current Version:** 0.1.0
- **Author:** Noel Schwabenland (owner of this fork/update)
- **Original Creator:** Florian Maas (fpgmaas/agentic-uv)
- **Python Support:** 3.10 - 3.14
- **Build Tool:** uv (fast Python package manager)

## Documentation Links

- Root docs: See `docs/` directory
- Generated project docs: `{{cookiecutter.project_name}}/docs/` (if mkdocs=y)
- Agent development guide: @.copilot/rules/skills.md (template)
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

## Notes for GitHub Copilot

This template is designed to be both:
1. **Easy to use** - Users just answer questions and get a ready-to-use project
2. **Agent-ready** - Generated projects include `.copilot/` so GitHub Copilot can help with development
3. **Best-practices-first** - Strict linting, type checking, and testing enforced from day one

### Session Flow Requirements

**Important:** When working on tasks, do NOT complete sessions with a simple closing message. Instead:
- Always end each task with a **question tool call** (using the `askQuestion` tool)
- Questions should be contextual and offer the user clear next steps
- This keeps the conversation interactive and gives users agency over what happens next
- Examples of good closing questions:
  - "Would you like me to run the tests to verify these changes?"
  - "Should I commit these changes or would you like to review them first?"
  - "Do you want me to generate a test project to verify the template works with these changes?"
  - "Would you like me to update the documentation to reflect these changes?"

When helping maintain this template:
- Always test changes by generating a sample project
- Verify `.copilot/` files are properly templated (no hardcoded paths)
- Keep Jinja2 conditionals unbroken (many branches for optional features)
- Document changes in root docs for other maintainers
- **End sessions with a question**, not a statement
