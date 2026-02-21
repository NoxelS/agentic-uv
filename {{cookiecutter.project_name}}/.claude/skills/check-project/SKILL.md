---
name: check-project
description: Run full code quality and testing pipeline (lint + test)
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: code-quality
---

## What I do

After significant code changes, I run a comprehensive validation pipeline that combines:

- **Full linting** - Ruff, mypy, pre-commit, deptry validation
- **Complete tests** - All pytest tests with coverage analysis
- **Quality assurance** - Ensures code meets all project standards

## When to use me

Use this skill **for thorough validation before commits**:

1. Before pushing to remote repository
2. Before creating a pull request
3. After major refactoring
4. As final validation before release
5. When all code quality is critical

## How I work

I execute both: `make check` and `make test`

**Step 1: Code Quality** (`make check`)
```bash
uv lock --locked              # Validate lock file
uv run pre-commit run -a      # All hooks
uv run mypy                   # Type checking
uv run deptry .               # Dependency audit
```

**Step 2: Testing** (`make test`)
```bash
uv run pytest --cov           # Run tests + coverage
```

## What I report

**Phase 1 - Linting Results**:
- ✅ All quality checks passed
- ❌ Specific failures with locations
- 🔧 Auto-fixable issues

**Phase 2 - Test Results**:
- ✅ Test count and pass rate
- ❌ Failed test names and reasons
- 📊 Coverage percentage and gaps

**Final Status**:
- 🎉 Ready to commit/push
- 🚫 Blocking issues to fix

## Workflow examples

### Example 1: After implementing a feature
```
Agent: [Implement new feature]
Agent: Load check-project skill to validate
Check: [Run make check] → All linting passes
Check: [Run make test] → 85% coverage ✅
Agent: Ask user what to do next
```

### Example 2: Before submitting PR
```
Agent: [Complete code changes]
Agent: Load check-project skill for final validation
Check: [Run make check] → Type error found
Agent: Fix type error
Agent: Reload check-project skill
Check: [Run make check] → All pass ✅
Check: [Run make test] → 92% coverage ✅
Agent: Ready for PR
```

## Integration tips

Before committing changes, ask me to:
- "Load the check-project skill to validate everything"
- "Run full validation on my changes"
- "Make sure all tests and linting pass"

Or ask me after initial changes and I may suggest this skill for final validation.

## Performance

Typical execution time:
- `make check` - 30-60 seconds
- `make test` - 1-3 minutes (varies with test suite size)
- **Total** - 2-4 minutes

## When to use specific skills instead

| Scenario | Use Instead |
|----------|------------|
| Just fixed linting issues | `lint-project` |
| Just wrote new tests | `test-project` |
| Quick format check | `lint-project` (faster) |
| Full PR validation | `check-project` (recommended) |

---

**Related Skills**: `lint-project`, `test-project`
