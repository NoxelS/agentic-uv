# Code Style & Organization

## Project Structure

This project uses a **{{cookiecutter.layout}} layout**:
{% if cookiecutter.layout == "src" -%}
- All source code lives in `src/{{cookiecutter.project_slug}}/`
- Tests are in `tests/`
- This keeps the project root clean
{%- else -%}
- Source code lives in `{{cookiecutter.project_slug}}/` at the root
- Tests are in `tests/`
- This is simpler for smaller projects
{%- endif %}

## Naming Conventions

- **Modules:** `lowercase_with_underscores.py`
- **Classes:** `PascalCase`
- **Functions:** `lowercase_with_underscores()`
- **Constants:** `UPPERCASE_WITH_UNDERSCORES`
- **Private:** Prefix with single underscore `_private_function`

## Type Hints (Required)

**All** functions and variables must have type hints. This is enforced via {% if cookiecutter.type_checker == "mypy" %}mypy strict mode{% else %}ty{% endif %}.

```python
# ✓ Good
def process_data(items: list[str]) -> dict[str, int]:
    """Process items and return counts."""
    result: dict[str, int] = {}
    for item in items:
        result[item] = len(item)
    return result

# ✗ Bad - missing type hints
def process_data(items):
    result = {}
    for item in items:
        result[item] = len(item)
    return result
```

## Imports

- Organize imports in three groups: standard library, third-party, local (separated by blank lines)
- Use absolute imports, not relative imports
- ruff will automatically organize imports via `make check`

```python
# ✓ Good
import os
from typing import Optional

import requests

from {{cookiecutter.project_slug}}.utils import helper_function
```

## Code Style

- **Line length:** Maximum 120 characters
- **Formatting:** ruff formatter (enforced)
- **Indentation:** 4 spaces
- **Docstrings:** Google-style docstrings

```python
def calculate_mean(values: list[float]) -> float:
    """Calculate the arithmetic mean of values.
    
    Args:
        values: A list of numeric values.
        
    Returns:
        The arithmetic mean of the input values.
        
    Raises:
        ValueError: If the list is empty.
    """
    if not values:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(values) / len(values)
```

## String Formatting

- Use f-strings for all string formatting
- Use single quotes for regular strings
- Use triple quotes for docstrings

```python
# ✓ Good
name = 'Alice'
greeting = f'Hello, {name}!'

# ✗ Avoid
greeting = 'Hello, %s!' % name
greeting = 'Hello, {}'.format(name)
```

## Error Handling

- Catch specific exceptions, not bare `except`
- Avoid using `Exception` when more specific types apply

```python
# ✓ Good
try:
    result = int(value)
except ValueError:
    logger.error(f'Invalid integer: {value}')

# ✗ Bad
try:
    result = int(value)
except:
    pass
```

## Comments & Documentation

- Write clear, concise comments
- Prefer self-documenting code over comments
- Use docstrings for all public functions and classes
- Link related functions/concepts

```python
# ✓ Good - code is self-explanatory
max_retries = 3
while attempts < max_retries and not success:
    success = attempt_connection()
    attempts += 1

# ✗ Bad - unclear
m = 3
while a < m and not s:
    s = f()
    a += 1
```

## Example Module

```python
"""Utilities for data processing.

This module provides helper functions for common data manipulation tasks.
"""

from typing import Optional


def validate_email(email: str) -> bool:
    """Check if the email format is valid.
    
    Args:
        email: The email address to validate.
        
    Returns:
        True if email format is valid, False otherwise.
    """
    return '@' in email and '.' in email.split('@')[1]


class DataProcessor:
    """Processes and transforms data."""
    
    def __init__(self, name: str) -> None:
        """Initialize the processor.
        
        Args:
            name: Name of this processor instance.
        """
        self.name = name
    
    def process(self, data: list[dict]) -> list[dict]:
        """Process a list of data dictionaries.
        
        Args:
            data: Input data to process.
            
        Returns:
            Processed data.
        """
        return [self._transform(item) for item in data]
    
    def _transform(self, item: dict) -> dict:
        """Transform a single item (private method).
        
        Args:
            item: Single data item.
            
        Returns:
            Transformed item.
        """
        return {**item, 'processed': True}
```
