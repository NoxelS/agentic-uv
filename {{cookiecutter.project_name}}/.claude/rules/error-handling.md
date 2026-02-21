# Error Handling & Debugging

## Error Handling Philosophy

### Principle: Fail Fast, Fail Clearly

**Fail Fast**: Detect errors immediately rather than letting bad data propagate
```python
# ❌ Bad: Silent failure
def process_data(data: dict) -> None:
    value = data.get('amount')  # Returns None if missing
    total = value * 2  # TypeError later when value is None
    return total

# ✅ Good: Fail immediately with clear message
def process_data(data: dict) -> float:
    if 'amount' not in data:
        raise ValueError('Missing required field: amount')
    
    value = data['amount']
    if not isinstance(value, (int, float)):
        raise TypeError(f'amount must be numeric, got {type(value).__name__}')
    if value < 0:
        raise ValueError(f'amount must be non-negative, got {value}')
    
    return value * 2
```

**Fail Clearly**: Provide helpful error messages
```python
# ❌ Bad: Cryptic error
if not check_format(email):
    raise ValueError('Invalid')

# ✅ Good: Helpful error
if not check_format(email):
    raise ValueError(
        f'Invalid email format: {email!r}. '
        'Expected format: user@domain.com'
    )
```

### Error Hierarchy: Specific → General

Always catch specific exceptions before general ones:

```python
# ✅ Good: Specific before general
try:
    process_file(filename)
except FileNotFoundError as e:
    logger.error(f'File not found: {filename}')
    raise ConfigError(f'Config file missing: {filename}') from e
except PermissionError as e:
    logger.error(f'Cannot read file: {filename}')
    raise SecurityError(f'Cannot access file: {filename}') from e
except IOError as e:
    logger.error(f'IO error: {e}')
    raise ProcessError(f'Cannot process file: {filename}') from e

# ❌ Bad: General catches everything
try:
    process_file(filename)
except Exception as e:
    # Catches FileNotFoundError, PermissionError, and everything else
    # Can't distinguish between error types
    logger.error(f'Error: {e}')
```

## Custom Exceptions

### Define Domain-Specific Exceptions

```python
"""Custom exceptions for payment processing module."""

class PaymentError(Exception):
    """Base class for payment-related errors."""
    pass


class InsufficientFundsError(PaymentError):
    """Raised when account balance is too low."""
    
    def __init__(self, required: float, available: float):
        self.required = required
        self.available = available
        super().__init__(
            f'Insufficient funds: required ${required:.2f}, '
            f'available ${available:.2f}'
        )


class PaymentGatewayError(PaymentError):
    """Raised when payment gateway is unreachable."""
    
    def __init__(self, gateway: str, message: str):
        self.gateway = gateway
        super().__init__(
            f'{gateway} gateway error: {message}'
        )


class TransactionNotFoundError(PaymentError):
    """Raised when transaction ID doesn't exist."""
    
    def __init__(self, transaction_id: str):
        self.transaction_id = transaction_id
        super().__init__(f'Transaction not found: {transaction_id!r}')
```

### Usage Example

```python
def process_payment(user_id: int, amount: float) -> str:
    """Process payment and return transaction ID.
    
    Args:
        user_id: User to charge.
        amount: Amount in dollars.
        
    Returns:
        Transaction ID.
        
    Raises:
        InsufficientFundsError: If account balance too low.
        PaymentGatewayError: If gateway unreachable.
        PaymentError: For other payment-related errors.
    """
    # Check balance
    account = get_account(user_id)
    if account.balance < amount:
        raise InsufficientFundsError(
            required=amount,
            available=account.balance
        )
    
    # Process with gateway
    try:
        response = stripe.charge(amount)
    except stripe.error.APIError as e:
        raise PaymentGatewayError('Stripe', str(e)) from e
    
    if response.status != 'succeeded':
        raise PaymentError(f'Payment declined: {response.reason}')
    
    return response.id
```

## Context Managers for Error Handling

### Resource Cleanup

```python
@contextmanager
def temporary_connection(db_url: str):
    """Ensure database connection is closed.
    
    Usage:
        with temporary_connection('postgresql://...') as db:
            user = db.query(User).first()
    """
    connection = None
    try:
        connection = connect(db_url)
        yield connection
    except ConnectionError as e:
        logger.error(f'Connection failed: {e}')
        raise
    finally:
        if connection:
            connection.close()


# Usage
with temporary_connection('postgresql://localhost/mydb') as db:
    users = db.query(User).all()
    # Connection automatically closed, even if exception occurs
```

### Transactional Error Handling

```python
@contextmanager
def transaction(db_session: Session):
    """Database transaction with automatic rollback on error.
    
    Usage:
        with transaction(db) as session:
            user = User(name='Alice')
            session.add(user)
            # Committed automatically on success
            # Rolled back if exception occurs
    """
    try:
        yield db_session
        db_session.commit()
    except Exception:
        db_session.rollback()
        raise
    finally:
        db_session.close()
```

## Logging for Error Context

### Log Levels

```python
import logging

logger = logging.getLogger(__name__)

# DEBUG: Detailed information for diagnosis
logger.debug(f'Processing user {user_id}, age={user.age}')

# INFO: Confirmation that things are working
logger.info(f'User {user_id} registered successfully')

# WARNING: Something unexpected but not critical
logger.warning(f'Slow query detected: {query_time_ms}ms (expected <100ms)')

# ERROR: Serious problem, something failed
logger.error(f'Failed to send email to {user.email}: {error}')

# CRITICAL: Very serious, system may not recover
logger.critical('Database connection lost, shutting down')
```

### Structured Logging for Errors

```python
# ❌ Bad: Unclear what went wrong
logger.error('Error processing payment')

# ✅ Good: Include context
logger.error(
    'Payment processing failed',
    extra={
        'user_id': user_id,
        'amount': amount,
        'gateway': 'stripe',
        'error_code': error.code,
        'retry_count': retry_count,
    }
)
```

### Exception Logging

```python
try:
    risky_operation()
except SpecificError as e:
    # Full traceback helps debugging
    logger.exception(f'Risky operation failed: {e}')
    raise
```

## Debugging Strategies

### 1. Reproduce the Error

First, create a minimal example that shows the problem:

```python
# Bad: "It doesn't work"
# Good: Can you run this and reproduce?

def test_reproduce_error() -> None:
    """Minimal reproduction of reported issue."""
    data = {'name': 'Alice', 'age': -5}  # Negative age invalid
    
    # This should raise ValueError but doesn't
    user = User(**data)
    assert user.age >= 0  # Test fails
```

### 2. Isolate the Problem

Narrow down which part is failing:

```python
# Original: Process 1000 records, 50 fail
def process_batch(records: list[dict]) -> None:
    for record in records:
        process_record(record)

# Isolate: Process records one by one to find the bad one
for i, record in enumerate(records):
    try:
        process_record(record)
        print(f'✓ Record {i} OK')
    except Exception as e:
        print(f'✗ Record {i} FAILED: {e}')
        print(f'  Data: {record}')
```

### 3. Add Debug Output

```python
# ❌ Minimal output
def calculate_total(items: list[dict]) -> float:
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total

# ✅ Debug output helps diagnosis
def calculate_total(items: list[dict], debug: bool = False) -> float:
    total = 0
    for i, item in enumerate(items):
        subtotal = item['price'] * item['quantity']
        if debug:
            print(f'Item {i}: price={item["price"]}, qty={item["quantity"]}, '
                  f'subtotal={subtotal}')
        total += subtotal
    if debug:
        print(f'Total: {total}')
    return total

# Usage when debugging
calculate_total(problematic_items, debug=True)
```

### 4. Use Type Guards for Validation

```python
# Catch type errors early
from typing import Any, TypeGuard

def is_valid_user(value: Any) -> TypeGuard[dict]:
    """Check if value is a valid user dict."""
    return (
        isinstance(value, dict)
        and 'id' in value and isinstance(value['id'], int)
        and 'name' in value and isinstance(value['name'], str)
        and 'email' in value and isinstance(value['email'], str)
    )

def process_users(data: Any) -> list[dict]:
    """Validate input before processing."""
    if not isinstance(data, list):
        raise TypeError(f'Expected list, got {type(data).__name__}')
    
    valid_users = []
    for i, item in enumerate(data):
        if not is_valid_user(item):
            logger.warning(f'Item {i} is not a valid user: {item}')
            continue
        valid_users.append(item)
    
    return valid_users
```

## Common Error Patterns

### Pattern 1: Type Errors from Dynamic Data

```python
# ❌ Problem: JSON API returns dynamic types
data = json.loads('{"age": "25"}')  # Type is str, not int
years = data['age'] + 1  # TypeError: str + int

# ✅ Solution: Validate and convert
def get_age(data: dict) -> int:
    raw_age = data.get('age')
    
    if raw_age is None:
        raise ValueError('age field is required')
    
    try:
        age = int(raw_age)  # Convert to int
    except (ValueError, TypeError):
        raise ValueError(f'age must be numeric, got {raw_age!r}')
    
    if age < 0 or age > 150:
        raise ValueError(f'age must be 0-150, got {age}')
    
    return age
```

### Pattern 2: Resource Exhaustion

```python
# ❌ Problem: Loading entire dataset into memory
def process_all_users() -> None:
    all_users = db.query(User).all()  # Out of memory!
    for user in all_users:
        process_user(user)

# ✅ Solution: Process in chunks with generators
def process_all_users(batch_size: int = 1000) -> None:
    """Process users in chunks to avoid memory issues."""
    offset = 0
    while True:
        batch = db.query(User).offset(offset).limit(batch_size).all()
        if not batch:
            break
        
        for user in batch:
            process_user(user)
        
        offset += batch_size
        logger.info(f'Processed {offset} users')
```

### Pattern 3: Race Conditions

```python
# ❌ Problem: Check then act (race condition)
if account.balance >= amount:
    account.balance -= amount  # Might overdraw if another process changed it

# ✅ Solution: Atomic operation (database transaction)
def withdraw(account_id: int, amount: float) -> None:
    with transaction(db_session) as session:
        # Lock the account row (no other reads/writes until commit)
        account = session.query(Account).with_for_update().get(account_id)
        
        if account.balance < amount:
            raise InsufficientFundsError(amount, account.balance)
        
        account.balance -= amount
        # Committed atomically
```

## Testing Error Scenarios

### Test That Errors are Raised

```python
def test_invalid_age_raises_error() -> None:
    """Test that negative age is rejected."""
    with pytest.raises(ValueError, match='age must be non-negative'):
        User(name='Alice', age=-5)


def test_missing_required_field_raises_error() -> None:
    """Test that missing name field is detected."""
    with pytest.raises(ValueError, match='name is required'):
        User(age=25)  # Missing name
```

### Test Error Messages

```python
def test_error_message_is_helpful() -> None:
    """Test that error messages include context."""
    try:
        calculate_discount(price=100, rate=1.5)
    except ValueError as e:
        # Check message includes actual value and constraint
        assert '1.5' in str(e)
        assert '0-1' in str(e)
```

### Test Recovery from Errors

```python
def test_retry_on_temporary_failure(monkeypatch) -> None:
    """Test that temporary errors are retried."""
    attempts = 0
    
    def failing_api_call():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise ConnectionError('Temporary network issue')
        return {'status': 'success'}
    
    monkeypatch.setattr('requests.get', failing_api_call)
    
    # Should succeed after retries
    result = call_with_retry(failing_api_call, max_retries=3)
    assert result['status'] == 'success'
    assert attempts == 3
```

## Error Recovery Strategies

### Retry with Exponential Backoff

```python
import time


def call_with_retry(
    func: Callable,
    max_retries: int = 3,
    backoff_factor: float = 2.0,
) -> Any:
    """Call function with exponential backoff retry.
    
    Args:
        func: Function to call.
        max_retries: Maximum number of retries.
        backoff_factor: Multiplier for backoff (1 * 2^attempt seconds).
        
    Returns:
        Function result.
        
    Raises:
        Last exception if all retries fail.
    """
    last_error: Exception | None = None
    
    for attempt in range(max_retries):
        try:
            return func()
        except (ConnectionError, TimeoutError) as e:
            last_error = e
            
            if attempt < max_retries - 1:
                wait_time = backoff_factor ** attempt
                logger.warning(
                    f'Attempt {attempt + 1} failed: {e}. '
                    f'Retrying in {wait_time}s...'
                )
                time.sleep(wait_time)
            else:
                logger.error(f'All {max_retries} attempts failed')
    
    raise last_error or RuntimeError('Unknown error')
```

### Fallback to Alternative

```python
def get_data_with_fallback(primary_source: str, fallback_source: str) -> dict:
    """Try primary source, fall back to secondary if it fails.
    
    Args:
        primary_source: Main data source (faster, preferred).
        fallback_source: Backup source if primary fails.
        
    Returns:
        Data from whichever source succeeds.
        
    Raises:
        DataError: If both sources fail.
    """
    try:
        logger.info(f'Trying primary source: {primary_source}')
        return fetch_data(primary_source)
    except ConnectionError as e:
        logger.warning(f'Primary source failed: {e}')
        
        try:
            logger.info(f'Trying fallback source: {fallback_source}')
            return fetch_data(fallback_source)
        except ConnectionError as e2:
            logger.error(f'Both sources failed: {e2}')
            raise DataError('Cannot fetch data from any source') from e2
```
