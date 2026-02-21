---
name: test-project
description: Execute comprehensive test suite with coverage reporting
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: testing
---

## What I do

After implementing features or fixing bugs, I run the complete test suite:

- **Unit tests** - All pytest tests in the project
- **Coverage analysis** - Verify 80%+ code coverage
- **Coverage reports** - Generate HTML and XML reports
- **Test parallelization** - Run tests efficiently across CPU cores
- **Failure reporting** - Detailed output for debugging failures

## When to use me

Use this skill **after implementing features or fixing bugs**:

1. After writing new code features
2. After refactoring components
3. After fixing bugs
4. Before submitting pull requests
5. To verify code coverage thresholds

## How I work

I execute: `make test`

This Makefile target runs pytest with coverage:

```bash
make test
```

Which runs:
```bash
uv run python -m pytest --cov --cov-config=pyproject.toml --cov-report=xml tests
```

**Coverage requirements**:
- Minimum 80% code coverage (`fail_under=80` in pyproject.toml)
- HTML reports generated to `htmlcov/`
- XML reports for CI/CD integration

## What I report

I'll show you:
- ✅ **All tests pass** - With coverage percentage
- ❌ **Test failures** - Which tests failed and why
- 📊 **Coverage summary** - Overall and per-module coverage
- 🔴 **Coverage gaps** - Which lines/functions lack tests

## What to do if tests fail

If `make test` fails:
- **Test errors**: Review the pytest output for assertion failures
- **Coverage gaps**: Add tests for uncovered code paths
- **Import errors**: Check for missing test dependencies
- **Fixture issues**: Verify pytest fixtures are properly defined

## Coverage best practices

- Aim for 80%+ coverage (enforced by config)
- Critical paths should have 100% coverage
- Use `@pytest.mark.coverage` for critical tests
- Test edge cases, not just happy paths

## Integration tips

After you implement code, ask me to:
- "Load the test-project skill and run tests"
- "Check if my new feature has adequate test coverage"
- "Run the full test suite on my changes"

Or I may automatically suggest this skill after you've written tests.

---

**Related Skills**: `lint-project`, `check-project`
