# Commit Message Guidelines

This document defines the commit message standards for the agentic-uv project. All commits MUST follow the Conventional Commits specification to maintain a clean, searchable git history and enable automated changelog generation.

## Conventional Commits Format

Every commit message MUST follow this format:

```
<type>(<scope>): <description>

<body>

<footer>
```

### Type (Required)

The `<type>` MUST be one of the following:

| Type | Description | Example |
|------|-------------|---------|
| `feat` | A new feature | `feat(agent): add explore subagent support` |
| `fix` | A bug fix | `fix(skill): correct lint-project validation` |
| `docs` | Documentation updates | `docs(rules): update agent-interaction protocol` |
| `style` | Code style changes (formatting, missing semicolons, etc.) | `style: format cookiecutter template files` |
| `refactor` | Code refactoring without feature changes | `refactor(skills): simplify post-change-validation` |
| `test` | Adding or updating tests | `test(cookiecutter): add skill generation tests` |
| `chore` | Maintenance tasks, dependencies, tooling | `chore: add conventional-commits pre-commit hook` |
| `ci` | CI/CD pipeline changes | `ci: update github actions workflow` |

### Scope (Optional but Recommended)

The `<scope>` specifies what part of the project is affected:

- `agent` - Agent interaction protocol
- `skill` - OpenCode skills
- `rule` - Rules in `.copilot/rules/`
- `doc` - Documentation and README files
- `ci` - CI/CD and GitHub Actions
- `test` - Test files and test infrastructure
- `refactor` - Code refactoring
- `chore` - General maintenance

### Description (Required)

The `<description>` MUST:
- Use imperative mood: "add", not "added" or "adds"
- Start with lowercase letter
- NOT include a period at the end
- Be concise (50 characters or less)
- Describe what the commit does, not what issue it fixes

✅ **Good examples:**
```
feat(agent): add explore subagent guidance to agent-interaction
fix(skill): correct coverage threshold in test-project skill
docs(rule): add commit message guidelines
refactor(skill): simplify post-change-validation logic
```

❌ **Bad examples:**
```
Added agent subagent features
Fixed stuff in skills.
DOCS UPDATED - WOW
Updates (not specific about what)
```

## Message Body (Optional)

If additional context is needed, include a blank line followed by a body that explains:
- What was changed and why
- Any breaking changes
- How to test the changes

**Example:**
```
feat(agent): add explore subagent guidance to agent-interaction

The explore subagent is optimized for codebase analysis and should be
spawned whenever a task involves pattern discovery or file searching.

This reduces redundant manual searching and allows the main agent to
focus on implementation work.

Breaking change: None
```

## Message Footer (Optional)

Use footers for additional metadata:

```
Closes #123
Refs #456
BREAKING CHANGE: description of what broke
```

## Examples

### Example 1: Simple Feature
```
feat(skill): create lint-project validation skill
```

### Example 2: Bug Fix with Details
```
fix(rule): correct agent-interaction Rule 5 formatting

The Rule 5 section had incorrect markdown structure that prevented
proper rendering in OpenCode.

Closes #42
```

### Example 3: Chore with Breaking Change
```
chore: add conventional-commits pre-commit hook

This adds commit message validation using conventional-commits.

BREAKING CHANGE: All future commits must follow Conventional Commits format
```

### Example 4: Documentation
```
docs(guide): add commit message guidelines to rules
```

## Pre-Commit Hook Validation

The project has a pre-commit hook that validates commit messages:

```bash
git commit -m "feat(agent): add new feature"
# ✅ Passes validation
```

```bash
git commit -m "Updated some stuff"
# ❌ Fails: doesn't follow conventional commits format
```

### Required Scopes

For this project, allowed scopes are:
- `agent` - Agent interactions and protocols
- `skill` - OpenCode skills and skill definitions
- `rule` - Rules in `.copilot/rules/`
- `doc` - Documentation
- `ci` - CI/CD and automation
- `test` - Tests and testing
- `refactor` - Code refactoring
- `chore` - General maintenance

## Why Conventional Commits?

1. **Semantic Versioning** - Automatically determine version bumps (MAJOR.MINOR.PATCH)
2. **Automated Changelogs** - Generate release notes from commit history
3. **Better Git History** - Easy to search and understand changes
4. **Tool Integration** - Works with conventional-changelog and other tools
5. **Team Communication** - Clear, consistent commit messages

## Quick Reference

| Need | Format |
|------|--------|
| New agent feature | `feat(agent): describe feature` |
| New skill | `feat(skill): describe skill` |
| New rule | `feat(rule): describe rule` |
| Fix a bug | `fix(scope): describe fix` |
| Update docs | `docs(scope): describe update` |
| Refactor code | `refactor(scope): describe refactor` |
| Add tests | `test(scope): describe tests` |
| Update deps | `chore: describe update` |

## Bypassing Validation (Not Recommended)

If you absolutely must bypass validation:

```bash
git commit --no-verify -m "Your message"
```

⚠️ **Note**: This is strongly discouraged. Maintain commit message quality.

## Additional Resources

- [Conventional Commits Specification](https://www.conventionalcommits.org/)
- [Pre-commit Framework](https://pre-commit.com/)
- [conventional-pre-commit Hook](https://github.com/compilerla/conventional-pre-commit)

---

**Last Updated:** 2026-02-21  
**Scope:** All commits in agentic-uv project
