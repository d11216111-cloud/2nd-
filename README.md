# 2nd-

## Safe Division Function

This repository contains a safe division function that handles division by zero gracefully.

### Files

- `safe_division.py`: Contains the `safe_division` function that safely divides two numbers
- `test_safe_division.py`: Comprehensive unit tests for the safe_division function

### Usage

```python
from safe_division import safe_division

# Normal division
result = safe_division(10, 2)  # Returns 5.0

# Division by zero
result = safe_division(10, 0)  # Returns None

# Negative numbers
result = safe_division(-10, 2)  # Returns -5.0
```

### Running Tests

To run the unit tests:

```bash
python -m unittest test_safe_division.py -v
```

### Test Coverage

The unit tests cover:
- Normal division with positive integers
- Division by zero (returns None)
- Negative numbers
- Zero as numerator
- Decimal numbers
- Large numbers
- Small numbers
- Type validation