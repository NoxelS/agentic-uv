# Testing Conventions & Patterns

## Overview

- **Framework:** pytest
- **Minimum Coverage:** 80%
- **Location:** `tests/` directory
- **Running Locally:** `make test`
- **Running in CI/CD:** Tests run automatically on every PR and commit

## Test Structure

```
tests/
├── test_foo.py           # Tests for foo module
├── test_data/            # Test data files (if needed)
└── conftest.py           # Shared fixtures and configuration
```

## Test File Naming

- Files must start with `test_` or end with `_test.py`
- Match module names they test: `module.py` → `test_module.py`
- Keep tests organized by feature or module

## Basic Test Pattern

```python
import pytest
from {{cookiecutter.project_slug}}.utils import calculate_mean


def test_calculate_mean_with_values() -> None:
    """Test mean calculation with normal values."""
    result = calculate_mean([1.0, 2.0, 3.0])
    assert result == 2.0


def test_calculate_mean_empty_list_raises_error() -> None:
    """Test that empty list raises ValueError."""
    with pytest.raises(ValueError, match='Cannot calculate mean'):
        calculate_mean([])


@pytest.mark.parametrize('values,expected', [
    ([1.0], 1.0),
    ([1.0, 3.0], 2.0),
    ([-1.0, 1.0], 0.0),
])
def test_calculate_mean_various_inputs(
    values: list[float],
    expected: float,
) -> None:
    """Test mean with various input values."""
    assert calculate_mean(values) == expected
```

## Fixtures

Use fixtures for setup/teardown and shared test data:

```python
import pytest
from {{cookiecutter.project_slug}}.models import User


@pytest.fixture
def sample_user() -> User:
    """Provide a sample user for testing."""
    return User(name='Alice', email='alice@example.com')


def test_user_email_validation(sample_user: User) -> None:
    """Test email validation."""
    assert sample_user.email == 'alice@example.com'
```

## Test Coverage

- **Minimum:** 80% coverage required
- **View Report:** `make test-coverage` generates HTML report
- **Coverage Config:** Defined in `pyproject.toml`

### Coverage Markers

Mark edge cases and critical paths:

```python
import pytest

@pytest.mark.coverage  # Mark critical tests
def test_mission_critical_feature() -> None:
    """This test is critical for coverage."""
    pass
```

## Mocking

Use `unittest.mock` for external dependencies:

```python
from unittest.mock import MagicMock, patch

def test_api_call_with_mock() -> None:
    """Test API interaction with mocked response."""
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'status': 'ok'}
        
        # Your code that calls requests.get
        result = your_function()
        
        assert result == {'status': 'ok'}
        mock_get.assert_called_once()
```

## Running Tests

```bash
# Run all tests
make test

# Run specific test file
uv run pytest tests/test_module.py

# Run specific test function
uv run pytest tests/test_module.py::test_function_name

# Run with verbose output
uv run pytest -v

# Run with pattern matching
uv run pytest -k "keyword"

# Show coverage report
make test-coverage
```

## Type Hints in Tests

All test functions must have type hints:

```python
# ✓ Good
def test_calculation() -> None:
    """Test calculation."""
    result: int = calculate(5)
    assert result == 10

# ✗ Bad - missing return type
def test_calculation():
    result = calculate(5)
    assert result == 10
```

## Naming Test Functions

- Start with `test_`
- Describe what you're testing: `test_calculate_mean_with_positive_values()`
- Use clear, descriptive names

```python
# ✓ Good names
def test_user_registration_with_valid_email() -> None:
    pass

def test_user_registration_with_invalid_email_raises_error() -> None:
    pass

def test_database_connection_timeout_retries() -> None:
    pass

# ✗ Bad names
def test_1() -> None:
    pass

def test_user() -> None:
    pass

def test_error() -> None:
    pass
```

## Test Organization

Organize tests logically:

```python
# Group related tests in a class
class TestUserValidation:
    """Tests for user validation logic."""
    
    def test_valid_email_format(self) -> None:
        """Test recognition of valid email."""
        assert validate_email('user@example.com')
    
    def test_invalid_email_format(self) -> None:
        """Test rejection of invalid email."""
        assert not validate_email('invalid-email')


class TestUserCreation:
    """Tests for user creation process."""
    
    def test_create_user_with_valid_data(self) -> None:
        """Test successful user creation."""
        user = create_user('Alice', 'alice@example.com')
        assert user.name == 'Alice'
```

## Pre-Commit Test Checks

Tests run during:
- Local pre-commit hooks: `git commit` triggers `make check`
- CI/CD: Every PR and commit to main
- Manual: `make test` anytime

Run `make check` before committing to catch issues early.

## Test Design Principles (Red-Green-Refactor)

### Phase 1: Red - Write Failing Test
Start with a clear test that demonstrates the feature you want to implement:

```python
def test_user_registration_success() -> None:
    """Test successful user registration with valid email."""
    user = register_user('alice@example.com', 'Alice')
    
    assert user.email == 'alice@example.com'
    assert user.name == 'Alice'
    assert user.is_active is True
```

This test **fails** because `register_user()` doesn't exist yet. That's expected and good.

### Phase 2: Green - Implement to Pass
Implement the simplest code that makes the test pass:

```python
def register_user(email: str, name: str) -> User:
    """Register a new user."""
    return User(email=email, name=name, is_active=True)
```

Now the test passes. Don't worry about perfection yet.

### Phase 3: Refactor - Improve Design
Once the test passes, refactor for:
- Type safety
- Error handling
- Edge cases
- Performance
- Maintainability

```python
def register_user(email: str, name: str) -> User:
    """Register a new user with validation.
    
    Args:
        email: User email address (must be valid).
        name: User display name (1-255 chars).
        
    Returns:
        Created User instance.
        
    Raises:
        ValueError: If email or name is invalid.
    """
    if not email or '@' not in email:
        raise ValueError('Invalid email address')
    if not name or len(name) > 255:
        raise ValueError('Name must be 1-255 characters')
    
    return User(email=email, name=name, is_active=True)
```

### Red-Green-Refactor Cycle Benefits
- **Focus**: Only implement what tests require
- **Safety**: Changes are backed by tests
- **Clarity**: Tests define expected behavior
- **Confidence**: Refactoring won't break functionality
- **Coverage**: Naturally reaches 80%+ (tests drive implementation)

## Test Categories

### Unit Tests (Test Individual Functions)
- No external dependencies
- Mock database, APIs, file systems
- Fast (milliseconds)
- Focus on logic

```python
def test_calculate_tax_rate() -> None:
    """Test tax calculation with known inputs."""
    # No database access, no API calls
    rate = calculate_tax_rate(income=50000, state='CA')
    assert rate == 0.093
```

### Integration Tests (Test Component Interaction)
- Use real dependencies where practical
- Database transactions (rolled back)
- Multiple modules working together
- Slower but catch real bugs

```python
def test_user_registration_creates_profile(
    db_session: Session,
) -> None:
    """Test that registration also creates user profile."""
    user = register_user(db_session, 'alice@example.com', 'Alice')
    
    # Check user was created
    assert user.id is not None
    
    # Check profile exists (integration point)
    profile = db_session.query(UserProfile).filter_by(
        user_id=user.id
    ).first()
    assert profile is not None
    assert profile.full_name == 'Alice'
```

### Error Path Tests (Test Failure Scenarios)
- **Always include error cases**
- Test that errors are raised appropriately
- Verify error messages are helpful

```python
def test_register_user_with_invalid_email_raises_error() -> None:
    """Test that registration rejects invalid emails."""
    with pytest.raises(ValueError, match='Invalid email'):
        register_user('not-an-email', 'Alice')

def test_register_user_with_duplicate_email_raises_error(
    db_session: Session,
) -> None:
    """Test that duplicate emails are rejected."""
    # Create first user
    register_user_in_db(db_session, 'alice@example.com', 'Alice')
    
    # Try to create second user with same email
    with pytest.raises(IntegrityError):
        register_user_in_db(db_session, 'alice@example.com', 'Alice2')
```

## Debugging Failed Tests

```bash
# Drop into debugger on failure
uv run pytest --pdb tests/test_module.py

# Show print statements
uv run pytest -s tests/test_module.py

# Stop on first failure
uv run pytest -x tests/test_module.py

# Show local variables on failure
uv run pytest -l tests/test_module.py

# Run single test by name
uv run pytest tests/test_module.py::test_function_name -v
```

## Coverage Expectations

- **New code:** Must have >80% coverage
- **Modified code:** Coverage should not decrease
- **Exceptions:** Certificate edge cases in `pyproject.toml`

### What to Test

**Must test:**
- Business logic (the core domain)
- Error conditions (exceptions, edge cases)
- Boundary conditions (empty lists, zero values, max values)
- Integration points (database, APIs)

**Don't need to test:**
- Standard library functions (they're tested)
- Third-party dependencies (assume they work)
- Simple pass-through methods
- Auto-generated code

Example:
```python
# This needs a test
def calculate_discount(price: float, rate: float) -> float:
    """Business logic - test it."""
    if rate < 0 or rate > 1:
        raise ValueError('Rate must be 0-1')
    return price * (1 - rate)

# Test the logic
def test_calculate_discount() -> None:
    assert calculate_discount(100, 0.1) == 90
    
    with pytest.raises(ValueError):
        calculate_discount(100, 1.5)  # Rate out of bounds

# This doesn't need a test (obvious pass-through)
def format_user(user: User) -> str:
    """Auto-generated formatting."""
    return f'{user.__class__.__name__}(...)'
```

## Anti-patterns to Avoid

### ❌ Test Interdependence
```python
# BAD: Tests depend on execution order
def test_1_create_user(db: Database) -> None:
    user_id = db.create_user('alice@example.com')

def test_2_fetch_user(db: Database) -> None: 
    # Assumes test_1 ran first
    user = db.get_user(1)  # Hard-coded ID! 
    assert user.email == 'alice@example.com'
```

### ✅ Independent Tests
```python
# GOOD: Each test is self-contained
def test_create_and_fetch_user(db: Database) -> None:
    user_id = db.create_user('alice@example.com')
    user = db.get_user(user_id)
    assert user.email == 'alice@example.com'
```

### ❌ Brittle Tests
```python
# BAD: Test fails on implementation details
def test_user_string_format() -> None:
    user = User('alice@example.com', 'Alice')
    # Tests exact string - breaks if format changes
    assert str(user) == '<User: alice@example.com>'
```

### ✅ Resilient Tests
```python
# GOOD: Test behavior, not implementation
def test_user_identifies_correctly() -> None:
    user = User('alice@example.com', 'Alice')
    assert user.email in str(user)
```

### ❌ Unclear Test Names
```python
def test_1() -> None:
    pass

def test_error() -> None:
    pass
```

### ✅ Descriptive Test Names
```python
def test_user_registration_with_valid_email_succeeds() -> None:
    pass

def test_user_registration_with_invalid_email_raises_error() -> None:
    pass
```
