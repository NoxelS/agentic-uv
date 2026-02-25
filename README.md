# agentic-uv

[![Build status](https://img.shields.io/github/actions/workflow/status/NoxelS/agentic-uv/main.yml?branch=main)](https://github.com/NoxelS/agentic-uv/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/badge/python-3.10_%7C_3.11_%7C_3.12_%7C_3.13_%7C_3.14-blue?labelColor=grey&color=blue)](https://github.com/NoxelS/agentic-uv/blob/main/pyproject.toml)
[![License](https://img.shields.io/github/license/NoxelS/agentic-uv)](https://github.com/NoxelS/agentic-uv/blob/main/LICENSE)

A [Cookiecutter](https://cookiecutter.readthedocs.io) template for Python projects that enforces best practices from the first commit — and ships AI coding agents that already know and follow every one of them.

## Quickstart 🚀

Navigate to the directory where you want to create your project, then run:

```bash
uvx cookiecutter https://github.com/NoxelS/agentic-uv.git
```

## What this is

**agentic-uv** generates a production-ready Python project with:

- Strict linting, type checking, security scanning, and coverage enforcement wired up and passing before you write a single line of business logic
- A full CI/CD pipeline covering quality, security, and multi-version testing out of the box
- Pre-configured `.claude/` and `.copilot/` directories that give AI coding agents (OpenCode, GitHub Copilot) complete, structured knowledge of every quality rule, testing convention, and deployment workflow in the project

The key idea: the agents don't just have access to your code — they ship with explicit, up-to-date instructions on how this specific project is built, tested, and maintained. They enforce the same standards a senior engineer would.

---

## Best-Practice Enforcement — Baked In

Every generated project starts with the full quality stack already configured and passing:

### Code Quality
- [**ruff**](https://github.com/astral-sh/ruff) — linter and formatter with 18+ rule sets (security, complexity, performance, style, imports)
- [**mypy**](https://mypy.readthedocs.io/en/stable/) or [**ty**](https://docs.astral.sh/ty/) — strict static type checking, no implicit `Any`
- [**bandit**](https://bandit.readthedocs.io/) — security scanning on every commit via pre-commit
- [**vulture**](https://github.com/jendrikseipp/vulture) — dead code detection on every commit
- [**deptry**](https://github.com/fpgmaas/deptry/) — unused, missing, and transitive dependency detection (optional)
- [**pre-commit**](https://pre-commit.com/) — all checks run automatically before any commit lands

### Testing & Coverage
- [**pytest**](https://docs.pytest.org/) with [**pytest-cov**](https://pytest-cov.readthedocs.io/) and [**pytest-xdist**](https://pytest-xdist.readthedocs.io/)
- **80% coverage threshold enforced** — CI fails if coverage drops below 80%
- [**hypothesis**](https://hypothesis.readthedocs.io/) — property-based testing with starter examples included
- [**mutmut**](https://mutmut.readthedocs.io/) — mutation testing to verify test quality
- Integration test scaffold under `tests/integration/`

### Security Auditing
- [**pip-audit**](https://pypi.org/project/pip-audit/) — dependency vulnerability scanning
- Weekly scheduled security audit in CI (bandit + pip-audit)
- `make audit` runs the full security check locally

### CI/CD
- [**GitHub Actions**](https://github.com/features/actions) — quality, security, and test jobs on every push and PR
- Multi-Python-version matrix: 3.10, 3.11, 3.12, 3.13, 3.14
- Optional [**Codecov**](https://about.codecov.io/) integration

### Documentation
- Optional [**MkDocs**](https://www.mkdocs.org/) with Material theme, auto-deployed to GitHub Pages

### Containerization
- Optional [**Docker**](https://www.docker.com/) / [**Podman**](https://podman.io/) support

---

## Agent-Based Development

Every generated project ships with fully pre-configured agent context in `.claude/` (OpenCode) and `.copilot/` (GitHub Copilot). The agents don't need to discover the project conventions — they are given them explicitly.

### What agents know from day one

Each agent loads a structured set of rules covering every aspect of the project:

| Rule file | What the agent learns |
|-----------|----------------------|
| `code-style.md` | Type hints, naming conventions, formatting standards |
| `testing.md` | pytest patterns, coverage requirements, fixture design |
| `best-practices.md` | Security standards, type safety, error handling |
| `deployment.md` | CI/CD workflows, release process, GitHub Actions |
| `commit-guidelines.md` | Conventional commit format enforced on every commit |
| `agent-interaction.md` | How to work iteratively — no premature session termination |
| `implementation-strategy.md` | Risk assessment and implementation planning approach |
| `error-handling.md` | Error propagation, exception design, logging standards |

### OpenCode skills included

Agents can load specialised skills for common workflows:

| Skill | What it does |
|-------|-------------|
| `lint-project` | Runs `make check` — ruff, mypy, pre-commit, deptry |
| `test-project` | Runs `make test` — pytest with coverage reporting |
| `check-project` | Full pipeline — lint then test |
| `post-change-validation` | Recommends the right validation skill after any code change |
| `coding-standards` | Detects anti-patterns, code smells, readability issues |
| `implementation-approach` | Selects vertical/horizontal/hybrid strategy with risk assessment |
| `subagents-orchestration-guide` | Orchestrates multi-agent task distribution for large features |

### Subagent definitions included

For complex features, a full set of specialised subagents is pre-defined:

| Agent | Role |
|-------|------|
| `requirement-analyzer` | Analyses scope and determines implementation scale |
| `prd-creator` | Produces structured Product Requirements Documents |
| `technical-designer` | Creates Architecture Decision Records and Design Docs |
| `work-planner` | Breaks Design Docs into phased, ordered work plans |
| `task-decomposer` | Decomposes work plans into atomic implementation tasks |
| `task-executor` | Executes a single task and returns structured output |
| `quality-fixer` | Runs the full QA pipeline and self-heals until all checks pass |
| `document-reviewer` | Reviews any document for completeness and consistency |
| `design-sync` | Verifies consistency across multiple Design Docs |
| `acceptance-test-generator` | Generates integration test skeletons from acceptance criteria |
| `integration-test-reviewer` | Reviews integration and E2E tests against skeletons |

---

## Quickstart

Navigate to the directory where you want to create your project, then run:

```bash
uvx cookiecutter https://github.com/NoxelS/agentic-uv.git
```

Or without `uv`:

```bash
pip install cookiecutter
cookiecutter https://github.com/NoxelS/agentic-uv.git
```

Follow the prompts. Once complete, navigate into the generated directory and run:

```bash
make install   # set up virtualenv and pre-commit hooks
make check     # linting, type checking, security scanning
make test      # pytest with coverage
```

Everything passes on a fresh project. Start writing code in `your_project/`.

---

## Template Options

| Option | Choices | Description |
|--------|---------|-------------|
| `author` | string | Your name |
| `email` | string | Your email address |
| `author_github_handle` | string | Your GitHub username |
| `project_name` | string | Project directory name |
| `project_slug` | auto | Python module name (slugified) |
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
├── your_project/              ← Your code goes here (starts empty)
│   └── __init__.py
├── tests/
│   ├── test_foo.py            ← Example test (replace with your own)
│   ├── test_properties.py     ← Hypothesis property-based tests (starter examples)
│   └── integration/
│       └── test_integration.py
├── .claude/                   ← OpenCode agent context
│   ├── CLAUDE.md              ← Project overview and quick-start for the agent
│   ├── rules/                 ← Best-practice rules loaded by the agent
│   │   ├── code-style.md
│   │   ├── testing.md
│   │   ├── best-practices.md
│   │   ├── deployment.md
│   │   ├── commit-guidelines.md
│   │   ├── agent-interaction.md
│   │   ├── implementation-strategy.md
│   │   └── error-handling.md
│   └── skills/                ← Reusable workflow skills
│       ├── lint-project/
│       ├── test-project/
│       ├── check-project/
│       ├── post-change-validation/
│       ├── coding-standards/
│       ├── implementation-approach/
│       └── subagents-orchestration-guide/
├── .copilot/                  ← GitHub Copilot agent context (mirrors .claude/)
├── .github/workflows/         ← CI/CD pipelines (if enabled)
│   ├── main.yml               ← Quality, security, and test jobs
│   ├── on-release-main.yml    ← PyPI publish on release (if enabled)
│   └── security-audit.yml     ← Weekly bandit + pip-audit scan
├── docs/                      ← MkDocs documentation (if enabled)
├── Dockerfile                 ← Container setup (if enabled)
├── pyproject.toml             ← Full quality stack configured
├── Makefile                   ← Developer convenience targets
├── tox.ini                    ← Multi-version test matrix
└── README.md
```

---

## Makefile Targets

| Target | What it runs |
|--------|-------------|
| `make install` | Create virtualenv, install deps, install pre-commit hooks |
| `make check` | Ruff, type checker, pre-commit, deptry (if enabled) |
| `make test` | pytest with coverage |
| `make test-coverage` | pytest with HTML coverage report |
| `make test-parallel` | pytest with `-n auto` (parallel) |
| `make test-integration` | Integration tests only (`tests/integration/`) |
| `make test-property` | Hypothesis property-based tests only |
| `make test-mutation` | Mutation tests with mutmut |
| `make audit` | bandit + pip-audit security scan |
| `make build` | Build wheel |
| `make docs` | Serve MkDocs locally (if enabled) |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and contribution guidelines.

To test the template locally:

```bash
cookiecutter . --no-input
cd example-project
make install && make check && make test
```

---

## Acknowledgements

This project is based on [**cookiecutter-uv**](https://github.com/fpgmaas/cookiecutter-uv) by [Florian Maas](https://github.com/fpgmaas), which itself drew inspiration from [Audrey Feldroy's](https://github.com/audreyfeldroy) [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).

**agentic-uv** extends the original with agent-based development support, stricter quality tooling, enhanced security scanning, property-based and mutation testing, and a dual `.claude/` / `.copilot/` configuration for AI-assisted workflows.

---

## License

MIT License — see [LICENSE](LICENSE) for details.
