# Agent-Based Development

This project is designed for **agent-based code development**—where Claude helps you write, improve, and maintain code.

## What is Agent-Based Development?

Agent-based development means:
- Claude reads and understands your project structure and conventions
- Claude suggests improvements based on best practices
- Claude writes code that follows your project's standards
- Claude helps debug and refactor existing code
- All guidance is captured in `.claude/` for consistency

## How Claude Uses This Project Memory

Everything in `.claude/` is loaded into Claude's context:

- **`.claude/CLAUDE.md`** - Project overview and quick reference
- **`.claude/rules/*.md`** - Specific guidelines for different aspects
  - `code-style.md` - How code should be organized and written
  - `testing.md` - Testing patterns and coverage requirements
  - `best-practices.md` - Security, type checking, code quality standards
  - `deployment.md` - CI/CD workflows and release process

When you ask Claude to help with your code, it automatically:
1. References these conventions
2. Suggests code that follows them
3. Tests against the 80%+ coverage requirement
4. Ensures type hints are included
5. Validates security best practices

## Using Claude for Development

### In Claude Code (Recommended)

Open this project in Claude Code to get:
- Full project context automatically loaded
- Claude understands your code structure
- Suggestions follow all local conventions
- Direct file editing with proper validation

```bash
# Open in Claude Code
claude your-project-directory/
```

Claude will automatically load all `.claude/` files and understand your project's standards.

### Key Workflows

**1. Creating new modules**
```
You: "Create a new module in {{cookiecutter.project_slug}}/parser.py that validates JSON data"
Claude: 
- Creates module following your code-style.md conventions
- Adds type hints (required by mypy)
- Suggests docstring format
- Creates accompanying test in tests/test_parser.py
```

**2. Fixing code issues**
```
You: "The test coverage in tests/test_utils.py only reaches 65%. Add tests to reach 80%"
Claude:
- Identifies uncovered code paths
- Writes tests following your testing.md patterns
- Uses appropriate pytest fixtures
- Ensures parametrized tests where relevant
```

**3. Code review**
```
You: "Review this function for security issues and best practices"
Claude:
- Checks against best-practices.md (bandit rules, type safety)
- Suggests refactoring for complexity
- Ensures error handling is appropriate
- Verifies tests exist
```

**4. Refactoring**
```
You: "This function has a McCabe complexity of 12. Refactor it."
Claude:
- Splits function following code-style.md
- Maintains proper type hints
- Updates tests
- Verifies all checks still pass
```

## Claude's Capabilities

Claude can help with:

### ✓ Code Writing
- New modules and functions
- Tests and fixtures
- Refactoring existing code
- Bug fixes

### ✓ Quality Assurance
- Type checking guidance
- Security reviews
- Performance optimization
- Documentation updates

### ✓ Troubleshooting
- Debugging failed tests
- Understanding error messages
- Type checking failures
- Ruff linting suggestions

### ✓ Best Practices
- Following project conventions
- Maintaining consistency
- Code organization
- Design patterns

## Project Structure for Claude

Claude understands this layout:

```
{{cookiecutter.project_name}}/
├── {{cookiecutter.project_slug}}/        ← Your source code (empty to start)
│   └── __init__.py
├── tests/                       ← Tests (Claude tests new code)
│   ├── test_*.py
│   └── conftest.py
├── .claude/                     ← This directory (Claude reads all)
│   ├── CLAUDE.md
│   └── rules/
│       ├── code-style.md
│       ├── testing.md
│       ├── best-practices.md
│       └── deployment.md
├── docs/                        ← Documentation
├── Makefile                     ← Commands Claude can explain
├── pyproject.toml             ← Configuration Claude understands
└── README.md                  ← Project info
```

## Example Claude Session

```
You: "I need to create a config module that reads from YAML files, validates schema, and caches results"

Claude: 
Looking at your project conventions, I'll create this following:
- code-style.md requirements (type hints, Google docstrings)
- best-practices.md security standards (safe file handling)
- testing.md patterns (80%+ coverage, fixtures)

Creates:
1. {{cookiecutter.project_slug}}/config.py
   - Proper type hints for all functions
   - Safe YAML parsing with error handling
   - Caching decorator with type safety
   - Comprehensive docstrings

2. tests/test_config.py
   - Unit tests for each function
   - Fixture for sample YAML files
   - Error condition tests
   - Coverage exceeds 85%

3. Updates to tests/conftest.py
   - Shared fixtures for YAML test data

Then runs:
$ make check     # Passes all linting, typing, tests
$ make test      # 85% coverage ✓
```

## Making Claude More Helpful

### 1. Be Specific
```
# Better: Describes what you want
"Create a data validation module that checks email and phone formats, with regex patterns from RFC standards"

# Vague: Leaves too much interpretation
"Make a validator"
```

### 2. Reference Guidelines
```
# Better: Directly references project guidelines
"Following code-style.md, create a data loader that uses generators for memory efficiency"

# Vague: Claude might guess what you want
"Make a data loader"
```

### 3. Show Examples
```
# Better: Gives Claude concrete examples
"Create a parser following this pattern: (show your existing parser)"

# Vague: Claude might misunderstand style
"Create a parser"
```

## Asking Claude for Help

### Type Checking
```
"I'm getting 'Cannot access member "x" for type "y"' from mypy. What's wrong?"
Claude: Explains the type issue and shows the fix
```

### Test Coverage
```
"Which functions in my module don't have tests?"
Claude: Scans your test file, identifies gaps, suggests tests
```

### Performance
```
"This algorithm is slow. How can I optimize it?"
Claude: Reviews code, suggests improvements following best-practices.md
```

### Security
```
"Is this safe? I'm reading a user-provided file path."
Claude: Checks against bandit rules, suggests safe patterns
```

## Tips for Success

1. **Always run `make check` locally** before asking Claude to review changes
2. **Show Claude failing tests** - it can debug them
3. **Reference specific guidelines** in `.claude/rules/` when asking for code
4. **Ask Claude to explain** ruff/mypy/pytest errors
5. **Review Claude's code** before committing - it's a tool, not perfect
6. **Keep `.claude/` files updated** as conventions evolve

## When to Use Claude vs. Manual Coding

### Claude is Great For:
- Writing new modules
- Creating comprehensive test suites
- Refactoring for readability
- Debugging errors
- Explaining code

### Manual Coding is Better For:
- Very complex business logic you fully understand
- Architecture decisions
- Learning Python concepts
- Trialing new approaches

## Feedback Loop

1. **Ask Claude to write code**
2. **Run `make test` and `make check`**
3. **If it fails, show Claude the errors**
4. **Claude explains and suggests fixes**
5. **Repeat until all checks pass**

This loop is fast and produces high-quality code.

## Privacy & Security

- `.claude/` files are stored in your repository
- Treat them as internal project documentation
- Never commit secrets or passwords
- Claude's context is local to your session
- You control what Claude sees via `.claude/` content

## Extending Claude's Knowledge

As your project evolves, update `.claude/` files:

```markdown
# In .claude/rules/code-style.md, add a new section:

## Database Conventions
- All queries use SQLAlchemy ORM
- Connection pooling via psycopg2
- Migrations via Alembic in db/migrations/
```

This teaches Claude about your new patterns automatically.
