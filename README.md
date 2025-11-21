# 2nd- Unit Testing Project

## Task 3: Unit Testing Demonstration (任務三)

This repository demonstrates proper unit testing practices for a safe division function, including both passing (green light) and failing (red light) test scenarios.

## Files

- **safe_division.py**: Contains the `safe_division()` function that safely handles division by zero
- **test_safe_division.py**: Comprehensive unit tests with 6 test cases
- **test_results.md**: Complete documentation in Chinese (中文) showing both green and red light test scenarios

## Running the Tests

```bash
python -m unittest test_safe_division.py -v
```

## Test Coverage

The unit tests cover:
- ✅ Normal division with positive numbers
- ✅ Division with negative numbers
- ✅ Boundary value division (0, 1, etc.)
- ✅ Large number division
- ✅ Decimal number division
- ✅ **Division by zero** (returns None instead of crashing)

## Key Learning

The tests demonstrate the importance of handling edge cases:
- **Green Light (綠燈)**: All 6 tests pass when proper error handling is in place
- **Red Light (紅燈)**: Tests fail when division by zero handling is removed

See `test_results.md` for detailed Chinese documentation of both scenarios.