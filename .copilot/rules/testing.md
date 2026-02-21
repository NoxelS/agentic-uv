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
```

## Coverage Expectations

- **New code:** Must have >80% coverage
- **Modified code:** Coverage should not decrease
- **Exceptions:** Certificate edge cases in `pyproject.toml`

Example:
```python
# This needs a test
def important_function(param: int) -> int:
    return param * 2

# This likely doesn't (obvious pass-through)
def __repr__(self) -> str:
    return f'{self.__class__.__name__}(...)'
```
