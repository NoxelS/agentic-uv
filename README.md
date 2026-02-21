<p align="center">
  <img width="600" src="https://raw.githubusercontent.com/NoxelS/agentic-uv/main/docs/static/cookiecutter.svg">
</p>

---

[![Build status](https://img.shields.io/github/actions/workflow/status/NoxelS/agentic-uv/main.yml?branch=main)](https://github.com/NoxelS/agentic-uv/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/badge/python-3.10_%7C_3.11_%7C_3.12_%7C_3.13_%7C_3.14-blue?labelColor=grey&color=blue)](https://github.com/NoxelS/agentic-uv/blob/main/pyproject.toml)
[![License](https://img.shields.io/github/license/NoxelS/agentic-uv)](https://github.com/NoxelS/agentic-uv/blob/main/LICENSE)

**agentic-uv** is a modern [Cookiecutter](https://cookiecutter.readthedocs.io) template for Python projects — batteries-included from day one, and built for agent-assisted development with [OpenCode](https://opencode.ai) and GitHub Copilot.

---

## Features

### Dependency & Package Management
- [**uv**](https://docs.astral.sh/uv/) — fast, modern Python package and project manager
- Supports both [**src layout** and **flat layout**](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- Optional publishing to [**PyPI**](https://pypi.org) via GitHub release automation

### Code Quality
- [**ruff**](https://github.com/astral-sh/ruff) — extremely fast linter and formatter with 18+ rule sets enabled
- [**mypy**](https://mypy.readthedocs.io/en/stable/) or [**ty**](https://docs.astral.sh/ty/) — strict static type checking (your choice)
- [**deptry**](https://github.com/fpgmaas/deptry/) — detects unused, missing, and transitive dependencies
- [**bandit**](https://bandit.readthedocs.io/) — security scanning via pre-commit hooks
- [**pre-commit**](https://pre-commit.com/) — automated hooks run on every commit

### Testing & Coverage
- [**pytest**](https://docs.pytest.org/) with [**pytest-cov**](https://pytest-cov.readthedocs.io/) and [**pytest-xdist**](https://pytest-xdist.readthedocs.io/)
- **80%+ coverage threshold** enforced (`fail_under=80` in config)
- HTML and XML coverage reports generated automatically
- Parallel test execution via `make test-parallel`
- `@pytest.mark.coverage` marker for critical test paths

### CI/CD
- [**GitHub Actions**](https://github.com/features/actions) — full CI pipeline on every push and PR
- **Security audit workflow** — weekly bandit + pip-audit scans (scheduled and manual trigger)
- Multi-Python-version testing with [**tox-uv**](https://github.com/tox-dev/tox-uv) (3.10–3.14)
- Optional [**Codecov**](https://about.codecov.io/) integration for coverage tracking

### Documentation
- Optional [**MkDocs**](https://www.mkdocs.org/) setup with Material theme
- Auto-deploy to GitHub Pages

### Containerization
- Optional [**Docker**](https://www.docker.com/) or [**Podman**](https://podman.io/) support

### Agent-Based Development
Every generated project ships with a pre-configured `.claude/` and `.copilot/` directory structure, giving AI coding agents full project context out of the box:

- **`CLAUDE.md` / `COPILOT.md`** — project overview, conventions, and quick-start guide for the agent
- **`.claude/rules/`** — modular, topic-specific guidelines:
  - `code-style.md` — type hints, naming, formatting standards
  - `testing.md` — pytest patterns, coverage requirements, fixture design
  - `best-practices.md` — security, type safety, error handling
  - `deployment.md` — CI/CD, release workflows, GitHub Actions
  - `skills.md` — agent-based development guide

**Available OpenCode skills** (`.claude/skills/`):

| Skill | Purpose |
|-------|---------|
| `lint-project` | Run `make check` — ruff, mypy, deptry, pre-commit |
| `test-project` | Run `make test` — pytest with coverage |
| `check-project` | Full pipeline — lint + test |
| `post-change-validation` | Smart skill recommendation after code changes |
| `coding-standards` | Detect anti-patterns, code smells, readability issues |
| `implementation-approach` | Select vertical/horizontal/hybrid implementation strategy |
| `subagents-orchestration-guide` | Orchestrate multi-agent task distribution |

---

## Quickstart

Navigate to the directory where you want to create your project, then run:

```bash
uvx cookiecutter https://github.com/NoxelS/agentic-uv.git
```

Or, if you don't have `uv` installed:

```bash
pip install cookiecutter
cookiecutter https://github.com/NoxelS/agentic-uv.git
```

Follow the prompts to configure your project. Once complete, a new directory is created with your fully configured project. Navigate into it and follow the `README.md` instructions to finish setup.

---

## Template Options

| Option | Choices | Description |
|--------|---------|-------------|
| `author` | string | Your name |
| `email` | string | Your email address |
| `author_github_handle` | string | Your GitHub username |
| `project_name` | string | Project directory name |
| `project_slug` | auto | Python module name (slugified from project name) |
| `project_description` | string | Short project description |
| `layout` | `flat`, `src` | Package layout style |
| `include_github_actions` | `y`, `n` | Generate CI/CD workflows |
| `publish_to_pypi` | `y`, `n` | Add PyPI publish workflow |
| `deptry` | `y`, `n` | Enable dependency audit |
| `mkdocs` | `y`, `n` | Add MkDocs documentation |
| `codecov` | `y`, `n` | Enable Codecov coverage tracking |
| `dockerfile` | `y`, `n` | Add Dockerfile / Containerfile |
| `type_checker` | `mypy`, `ty` | Static type checker |
| `open_source_license` | MIT, BSD, ISC, Apache 2.0, GPL v3, None | License type |

---

## Generated Project Structure

```
your-project/
├── your_project/          ← Your code goes here (starts empty)
│   └── __init__.py
├── tests/
│   └── __init__.py
├── .claude/               ← OpenCode agent context
│   ├── CLAUDE.md
│   └── rules/
│       ├── code-style.md
│       ├── testing.md
│       ├── best-practices.md
│       ├── deployment.md
│       └── skills.md
├── .copilot/              ← GitHub Copilot agent context
│   ├── COPILOT.md
│   └── rules/             ← (same structure as .claude/rules/)
├── .github/workflows/     ← CI/CD pipelines (if enabled)
├── docs/                  ← MkDocs documentation (if enabled)
├── Dockerfile             ← Container setup (if enabled)
├── pyproject.toml         ← Enhanced configuration
├── Makefile               ← Developer convenience targets
├── tox.ini                ← Multi-version test matrix
└── README.md
```

---

## Development Workflow

After generating a project, the typical workflow is:

```bash
# Install dependencies
make install

# Run linting and type checking
make check

# Run tests with coverage
make test

# Full validation (lint + test)
make check && make test
```

If you have OpenCode configured, you can load skills to guide validation:
- `load lint-project` — run code quality checks
- `load test-project` — run the test suite
- `load check-project` — run everything before a PR

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and contribution guidelines.

To test the template locally:

```bash
# Generate a test project
cookiecutter . --no-input

# Test the generated project
cd example-project
make install
make check
make test
```

---

## Acknowledgements

This project is based on [**cookiecutter-uv**](https://github.com/fpgmaas/cookiecutter-uv) by [Florian Maas](https://github.com/fpgmaas), which itself drew inspiration from [Audrey Feldroy's](https://github.com/audreyfeldroy) [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).

**agentic-uv** extends the original with agent-based development support, stricter quality tooling, enhanced security scanning, and a dual `.claude/` / `.copilot/` configuration for AI-assisted workflows.

---

## License

MIT License — see [LICENSE](LICENSE) for details.
