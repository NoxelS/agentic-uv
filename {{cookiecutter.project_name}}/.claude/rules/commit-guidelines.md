# Commit Message Guidelines

This document defines the commit message standards for your project. All commits MUST follow the Conventional Commits specification to maintain a clean, searchable git history and enable automated changelog generation.

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
| `feat` | A new feature | `feat(auth): add JWT token validation` |
| `fix` | A bug fix | `fix(api): correct response format` |
| `docs` | Documentation updates | `docs(readme): update setup instructions` |
| `style` | Code style changes (formatting, missing semicolons, etc.) | `style: format code with ruff` |
| `refactor` | Code refactoring without feature changes | `refactor(utils): simplify helper functions` |
| `test` | Adding or updating tests | `test(auth): add JWT validation tests` |
| `chore` | Maintenance tasks, dependencies, tooling | `chore: update dependencies` |
| `ci` | CI/CD pipeline changes | `ci: add security audit workflow` |

### Scope (Optional but Recommended)

The `<scope>` specifies what part of the project is affected:

- `api` - API endpoints
- `auth` - Authentication and authorization
- `db` - Database changes
- `ui` - User interface components
- `utils` - Utility functions
- `test` - Test files and infrastructure
- `doc` - Documentation
- `ci` - CI/CD and GitHub Actions
- Or any other module-specific scope

### Description (Required)

The `<description>` MUST:
- Use imperative mood: "add", not "added" or "adds"
- Start with lowercase letter
- NOT include a period at the end
- Be concise (50 characters or less)
- Describe what the commit does, not what issue it fixes

✅ **Good examples:**
```
feat(auth): add JWT token validation
fix(api): correct response format
docs: update setup instructions
refactor(utils): simplify helper functions
test(auth): add JWT validation tests
```

❌ **Bad examples:**
```
Added JWT authentication
Fixed some bugs in API
UPDATED DOCUMENTATION
Updates (not specific about what)
```

## Message Body (Optional)

If additional context is needed, include a blank line followed by a body that explains:
- What was changed and why
- Any breaking changes
- How to test the changes

**Example:**
```
feat(auth): add JWT token validation

Added JWT token validation to the authentication middleware to
improve security. Tokens are now verified before allowing access
to protected routes.

Breaking change: /login endpoint now returns JWT in secure cookie
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
feat(auth): add two-factor authentication
```

### Example 2: Bug Fix with Details
```
fix(api): correct response format in user endpoint

The user endpoint was returning the old response format, causing
client errors. Updated to match the new schema.

Closes #42
```

### Example 3: Chore with Breaking Change
```
chore: upgrade authentication library

Updated auth library from v1 to v2.

BREAKING CHANGE: Password reset flow now requires email verification
```

### Example 4: Documentation
```
docs(readme): add deployment instructions
```

## Pre-Commit Hook Validation

This project uses a pre-commit hook that validates commit messages:

```bash
git commit -m "feat(auth): add new feature"
# ✅ Passes validation
```

```bash
git commit -m "Updated some stuff"
# ❌ Fails: doesn't follow conventional commits format
```

## Why Conventional Commits?

1. **Semantic Versioning** - Automatically determine version bumps (MAJOR.MINOR.PATCH)
2. **Automated Changelogs** - Generate release notes from commit history
3. **Better Git History** - Easy to search and understand changes
4. **Tool Integration** - Works with conventional-changelog and other tools
5. **Team Communication** - Clear, consistent commit messages

## Quick Reference

| Need | Format |
|------|--------|
| New feature | `feat(scope): describe feature` |
| Bug fix | `fix(scope): describe fix` |
| Update docs | `docs(scope): describe update` |
| Refactor code | `refactor(scope): describe refactor` |
| Add tests | `test(scope): describe tests` |
| Style/format | `style: describe changes` |
| Update deps | `chore: describe update` |
| CI/CD change | `ci: describe change` |

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
**Scope:** All commits in your project
