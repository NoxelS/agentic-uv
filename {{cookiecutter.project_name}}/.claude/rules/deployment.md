# Deployment & CI/CD Workflows

## CI/CD Pipeline Overview

Every commit and PR is automatically checked:

1. **Lint & Format Check** (ruff)
2. **Type Checking** ({% if cookiecutter.type_checker == "mypy" %}mypy{% else %}ty{% endif %})
{% if cookiecutter.deptry == 'y' -%}
3. **Dependency Analysis** (deptry)
{%- endif %}
4. **Tests & Coverage** (pytest)
5. **Security Audit** (pip-audit)
6. **Lock File Validation** (uv)

All checks must pass before merging to main.

## GitHub Actions Workflows

### Main Workflow (`main.yml`)

Runs on:
- Every push to main
- Every pull request

Checks:
- ✓ Code quality (ruff)
- ✓ Type safety
- ✓ Test coverage (80%+ required)
{% if cookiecutter.deptry == 'y' -%}
- ✓ Dependency cleanliness
{%- endif %}
- ✓ Security vulnerabilities

### Security Audit (`security-audit.yml`)

Runs:
- **Schedule:** Weekly on Mondays
- **On Demand:** Manually trigger via GitHub UI

Scans for:
- Known vulnerabilities in dependencies
- Outdated packages
- Security advisories

## Local Development Workflow

### Before Committing

```bash
# Full quality check (lint + type + tests)
make check

# Or manually:
uv run pre-commit run -a
uv run {% if cookiecutter.type_checker == "mypy" %}mypy{% else %}ty check{% endif %}
uv run pytest --cov
```

If any check fails, fix the issues and commit again.

### Making Changes

```bash
# Create feature branch
git checkout -b feature/my-feature

# Make code changes
# Write tests
# Keep tests passing
make test

# Before committing, run checks
make check

# Commit and push
git add .
git commit -m "feat: add my feature"
git push origin feature/my-feature

# Create PR on GitHub
```

## Release & Versioning

### Version Numbering

This project uses **Semantic Versioning**: `MAJOR.MINOR.PATCH`

- **MAJOR:** Breaking changes
- **MINOR:** New features (backward-compatible)
- **PATCH:** Bug fixes

Example:
- `0.1.0` → `0.1.1` (patch - bug fix)
- `0.1.1` → `0.2.0` (minor - new feature)
- `0.2.0` → `1.0.0` (major - breaking change)

### Creating a Release

{% if cookiecutter.publish_to_pypi == "y" -%}

1. **Update version in `pyproject.toml`:**
   ```toml
   version = "0.2.0"
   ```

2. **Tag the release:**
   ```bash
   git tag v0.2.0
   git push origin v0.2.0
   ```

3. **GitHub Actions automatically:**
   - Builds the package
   - Publishes to PyPI
   - Creates GitHub release

4. **Verify on PyPI:**
   - Visit https://pypi.org/project/{{cookiecutter.project_name}}/
   - Check new version is available

{%- else -%}

1. **Update version in `pyproject.toml`**
2. **Tag the release:** `git tag v0.2.0`
3. **Push tag:** `git push origin v0.2.0`
4. **GitHub Actions builds the package**

{%- endif %}

### Updating Changelog

Keep `CHANGELOG.md` or document changes in releases:

```markdown
## [0.2.0] - 2026-02-16

### Added
- New feature X for processing data
- Command-line interface for batch operations

### Fixed
- Bug in data validation with empty inputs

### Changed
- Improved performance of main algorithm by 40%
- Updated documentation examples

## [0.1.0] - 2026-01-01

### Added
- Initial release
- Core functionality
```

## Dependency Updates

### Adding Dependencies

```bash
# Add production dependency
uv add requests

# Add development-only dependency
uv add --dev pytest-timeout

# Lock new dependencies
uv lock
```

Commit both `pyproject.toml` and `uv.lock`.

### Removing Dependencies

```bash
# Remove unused dependency
uv remove old-package

# Check what else uses it
make check  # deptry will warn if still referenced
```

{% if cookiecutter.deptry == 'y' -%}
## deptry - Dependency Checker

deptry ensures:
- No unused dependencies declared
- No missing dependencies in code
- Correct categorization (dev vs prod)

```bash
# Run locally
uv run deptry .

# Runs automatically in CI/CD
make check
```

### Fixing deptry Issues

**Unused dependency:**
```bash
uv remove unused_package
```

**Missing dependency:**
```bash
uv add missing_package
```

{%- endif %}

## Lock File Management

`uv.lock` ensures reproducible builds:

```bash
# Update lock file
uv lock

# Verify lock is up to date
uv lock --locked  # Fails if out of sync

# Always commit lock file
git add uv.lock
git commit -m "chore: update lock file"
```

## Troubleshooting CI/CD Failures

### Type Check Failed

```bash
# Check types locally
uv run {% if cookiecutter.type_checker == "mypy" %}mypy{% else %}ty check{% endif %}

# Common fixes:
# - Add type annotations to functions
# - Use correct types: list[str] not List[str]
# - Import types from typing module
```

### Test Failed

```bash
# Run tests locally
make test

# Run specific failing test
uv run pytest tests/test_module.py::test_function -v

# Check coverage
make test-coverage
```

### Ruff Lint Failed

```bash
# Run linting locally
uv run ruff check .

# Auto-fix many issues
uv run ruff check --fix

# Format code
uv run ruff format .
```

### Lock File Out of Sync

```bash
# Update lock file
uv lock

# Commit it
git add uv.lock
git commit -m "chore: regenerate lock file"
```

## Best Practices

1. **Run `make check` before every commit**
2. **Keep main branch stable** - all PR checks must pass
3. **Review test coverage** before sending PR
4. **Update lock file** when adding/removing dependencies
5. **Tag releases properly** - use semantic versioning
6. **Document breaking changes** - update migration guide

## Emergency Overrides

For critical security patches or emergency fixes:

```bash
# Skip pre-commit checks (NOT RECOMMENDED)
git commit --no-verify

# But always run locally before pushing:
make check

# Document why it was necessary
```

Overrides should be approved by maintainers.
