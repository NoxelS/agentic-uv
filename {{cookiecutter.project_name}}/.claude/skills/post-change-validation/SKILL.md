---
name: post-change-validation
description: Automatic validation workflow after code changes (loads appropriate skill)
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: automation
---

## What I do

After you've made code changes, I guide you through automatic validation:

- **Detect change scope** - Determine what was modified
- **Recommend validation** - Suggest which skill to load based on changes
- **Execute validation** - Run the appropriate make target
- **Report results** - Show pass/fail status and next steps

## When to use me

Use this skill **after any code changes**:

1. After writing new functions/classes
2. After modifying existing code
3. After refactoring
4. After fixing bugs
5. Before committing changes

## How I work

I analyze your changes and recommend:

### For **code changes only**
→ Load `lint-project` skill
- Run: `make check`
- Validates: Formatting, types, linting

### For **code + test changes**
→ Load `test-project` skill then `lint-project`
- Run: `make test` then `make check`
- Validates: Tests + coverage + linting

### For **major changes or PR preparation**
→ Load `check-project` skill
- Run: `make check` then `make test`
- Full comprehensive validation

### For **dependency changes**
→ Load `lint-project` skill
- Run: `make check`
- Validates: Lock file + dependency audit

## Example workflow

```
You: [Make code changes]
Agent: [Detect changes and load this skill]
Validation Skill: Analyzing changes...
→ Code modified: app.py
→ Tests modified: test_app.py
Recommendation: Load test-project skill
Agent: [Load test-project]
Test Skill: Running make test...
Results: ✅ All tests pass (89% coverage)
Agent: Ask what to do next
```

## What triggers recommendations

**Just code changes** → `lint-project`
```
Modified: app.py, utils.py
→ Recommend: lint-project
```

**Code + Tests** → `test-project`
```
Modified: app.py, test_app.py
→ Recommend: test-project
```

**Dependencies changed** → `lint-project`
```
Modified: pyproject.toml
→ Recommend: lint-project
```

**Complex changes** → `check-project`
```
Modified: 5+ files, including tests
→ Recommend: check-project
```

## Integration with agent protocol

This skill works with your agent-interaction rules:

1. Agent makes code changes
2. Agent detects this skill is available
3. Agent recommends loading this skill to user
4. User chooses validation approach
5. Agent loads recommended skill (or alternative)
6. Agent runs make target via loaded skill
7. Agent asks user what to do next

## Quick references

**Shallow validation** (lint only):
- Use: `lint-project`
- Time: ~1 minute
- Good for: Type/format fixes

**Deep validation** (lint + test):
- Use: `test-project`
- Time: ~2-3 minutes
- Good for: New features, tests

**Complete validation** (full pipeline):
- Use: `check-project`
- Time: ~3-4 minutes
- Good for: PRs, releases

## Pro tips

- Load this skill after each meaningful code change
- It will guide you to the right validation tool
- Trust the recommendations but override if needed
- Use `check-project` when in doubt

---

**Related Skills**: `lint-project`, `test-project`, `check-project`
