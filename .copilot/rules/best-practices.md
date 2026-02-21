# Best Practices & Quality Standards

This project enforces high code quality standards through automated tooling and strict configurations.

## Type Safety ({% if cookiecutter.type_checker == "mypy" %}MyPy Strict{% else %}Ty{% endif %})

{% if cookiecutter.type_checker == "mypy" -%}
**All code must pass mypy in strict mode.** This means:
- Every function parameter must have a type annotation
- Every function must have a return type annotation
- All variables must be typed (where not obvious from context)
- No `Any` types allowed without explicit `# type: ignore` comments
{%- else -%}
**All code must pass ty (Astral's type checker).** This means:
- Fast, modern type checking on all functions
- Type annotations required on all public functions
- No untyped definitions allowed
{%- endif %}

### Type Annotation Examples

```python
# ✓ Correct
from typing import Optional

def fetch_user(user_id: int) -> Optional[dict]:
    """Fetch user by ID, or None if not found."""
    # Implementation here
    pass

class DataStore:
    def __init__(self) -> None:
        self.data: dict[str, str] = {}
    
    def add(self, key: str, value: str) -> None:
        """Add item to store."""
        self.data[key] = value

# ✗ Incorrect - missing types
def fetch_user(user_id):
    pass

class DataStore:
    def __init__(self):
        self.data = {}
```

### Checking Type Correctness

```bash
# Check types locally
make check

# See type errors
uv run {% if cookiecutter.type_checker == "mypy" %}mypy{% else %}ty check{% endif %}

# Auto-fix imports and simple issues
uv run ruff check --fix
```

## Security (Bandit & Code Analysis)

**Security is enforced via pre-commit hooks.** High-severity issues will fail commits.

### Security Rules

Bandit checks for common security vulnerabilities:

- No hard-coded passwords or secrets
- No use of `eval()` or `exec()`
- No weak cryptography
- No SQL injection vulnerabilities
- Safe file handling practices

### Examples

```python
# ✓ Safe
import secrets
token = secrets.token_hex(32)

# ✗ Insecure - hard-coded secret
PASSWORD = "mypassword123"

# ✓ Safety
from pathlib import Path
with open(Path('config.yaml')) as f:
    config = f.read()

# ✗ Unsafe - potential path traversal
with open(user_provided_path) as f:
    config = f.read()
```

### Dealing with Security Warnings

If you must bypass a security check, document it:

```python
# Security: This function uses eval() because it requires dynamic code execution.
# Inputs are pre-validated to prevent injection.
# noinspection PyUnresolvedReference
result = eval(formula, {"x": value})  # noqa: S307
```

## Code Quality (Ruff - 17+ Rule Sets)

Ruff automatically enforces:

| Rule Set | Purpose |
|----------|---------|
| `YTT` | Python 2020+ syntax issues |
| `S` | Security (bandit) |
| `B` | Common bugs (bugbear) |
| `A` | Use of builtins as variables |
| `C4` | Comprehension issues |
| `T10` | Debugger imports (no pdb in production) |
| `SIM` | Code simplification |
| `I` | Import sorting |
| `C90` | McCabe complexity (max 10) |
| `E, W` | Style (PEP 8) |
| `F` | PyFlakes (undefined names) |
| `PGH` | PyGrep hooks |
| `UP` | PyUpgrade (modern Python) |
| `RUF` | Ruff-specific rules |
| `TRY` | Exception handling best practices |

### Running Quality Checks

```bash
# Check all files
make check

# Auto-fix issues (many are auto-fixable)
uv run ruff check --fix

# View specific rule details
uv run ruff rule RUF001  # Example rule
```

### Code Complexity

McCabe complexity (max 10 per function):

```python
# ✓ Good - simple, clear logic
def process_item(item: dict) -> str:
    """Process a single item."""
    if item.get('active'):
        return item['name'].upper()
    return 'INACTIVE'

# ✗ Bad - too complex, refactor needed
def process_item(item):
    if item.get('active'):
        if item.get('premium'):
            if item.get('verified'):
                return item['name'].upper()
            else:
                return f"UNVERIFIED: {item['name']}"
        else:
            return item['name'].lower()
    else:
        return 'INACTIVE'
```

If a function is too complex, refactor it:

```python
# ✓ Better - split into smaller functions
def process_item(item: dict) -> str:
    """Process a single item."""
    if not item.get('active'):
        return 'INACTIVE'
    return _format_active_item(item)

def _format_active_item(item: dict) -> str:
    """Format an active item based on status."""
    if not item.get('verified'):
        return f"UNVERIFIED: {item['name']}"
    if item.get('premium'):
        return item['name'].upper()
    return item['name'].lower()
```

## Dependency Management

{% if cookiecutter.deptry == 'y' -%}
**deptry** checks for unused or missing dependencies. All dependencies must be:
- Declared in `pyproject.toml`
- Imported and used in the code
- At appropriate levels (dev vs. prod)
{%- endif %}

### Managing Dependencies

```bash
# Install new dependency
uv add package_name

# Install development-only dependency
uv add --dev package_name

# Check for unused dependencies
make check  # deptry runs as part of checks
```

## Documentation Standards

### Module Docstrings

Every module should have a docstring:

```python
"""Database models for user management.

This module provides ORM models for user accounts, profiles, and permissions.
It uses SQLAlchemy for database operations.
"""

import sqlalchemy as sa
# rest of module
```

### Function Docstrings

Use Google-style docstrings:

```python
def calculate_discount(
    price: float,
    discount_rate: float,
) -> float:
    """Calculate final price after discount.
    
    Args:
        price: Original price in dollars.
        discount_rate: Discount as decimal (0.1 = 10%).
        
    Returns:
        Final price after discount applied.
        
    Raises:
        ValueError: If price or discount_rate is negative.
        
    Example:
        >>> calculate_discount(100.0, 0.1)
        90.0
    """
    if price < 0 or discount_rate < 0:
        raise ValueError('Price and discount rate must be non-negative')
    return price * (1 - discount_rate)
```

### Class Docstrings

```python
class UserManager:
    """Manage user accounts and profiles.
    
    This class handles user creation, deletion, and profile updates
    through a clean API.
    
    Attributes:
        db: Database connection pool.
        cache: In-memory cache for frequently accessed users.
    """
    
    def __init__(self, db: Database, cache: Cache) -> None:
        """Initialize the manager."""
        self.db = db
        self.cache = cache
```

## Performance Considerations

- Avoid N+1 database queries (use eager loading)
- Cache frequently accessed data
- Use generators for large datasets
- Profile code before optimizing

```python
# ✗ N+1 problem
for user in users:
    print(user.name, get_user_stats(user.id))  # Query per user!

# ✓ Better - batch query
user_stats = get_multiple_user_stats([u.id for u in users])
for user in users:
    print(user.name, user_stats[user.id])
```

## Error Handling

- **Specific exceptions:** Catch specific exception types, not `Exception`
- **Logging:** Use logging module, not print statements
- **Context:** Include context in error messages

```python
import logging

logger = logging.getLogger(__name__)

# ✓ Good error handling
try:
    data = parse_json(raw_data)
except json.JSONDecodeError as e:
    logger.error(f'Invalid JSON in file {filename}: {e}')
    raise ValueError(f'Cannot parse {filename}') from e

# ✗ Bad error handling
try:
    data = parse_json(raw_data)
except:
    print('Error!')
```

## Testing Requirements

- **Target:** 80%+ code coverage
- **Critical paths:** Must have tests
- **Edge cases:** Test boundary conditions
- **Error paths:** Test exception handling

```bash
# View coverage report
make test-coverage
```

## Pre-Commit

Before every commit:

```bash
# Runs full checks (linting, typing, tests)
make check

# Or individually
uv run pre-commit run -a
uv run {% if cookiecutter.type_checker == "mypy" %}mypy{% else %}ty check{% endif %}
uv run pytest --cov
```

## CI/CD Pipeline

Your code is checked automatically:

1. **Lint:** ruff checks code style and security
2. **Type:** {% if cookiecutter.type_checker == "mypy" %}mypy{% else %}ty{% endif %} checks type correctness
{% if cookiecutter.deptry == 'y' -%}
3. **Dependencies:** deptry checks for unused/missing dependencies
{%- endif %}
4. **Tests:** pytest runs all tests with coverage
5. **Lock File:** uv lock must be consistent

Failing any of these will block merges to main.

## When to Break Rules

**Never.** If you absolutely must (with approval), document it:

```python
# HACK: Temporary workaround for issue #123
# This should be refactored when we upgrade the library
items = collection  # noqa: E501, type: ignore[assignment]
```

But this should be rare and tracked as technical debt.
