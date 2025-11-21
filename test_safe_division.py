"""
Unit tests for the safe_division function.
"""

import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """Test cases for safe_division function."""

    def test_normal_division(self):
        """Test normal division with positive integers."""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(20, 4), 5.0)
        self.assertEqual(safe_division(100, 10), 10.0)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(safe_division(10, 0))
        self.assertIsNone(safe_division(0, 0))
        self.assertIsNone(safe_division(-10, 0))

    def test_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)

    def test_zero_numerator(self):
        """Test division when numerator is zero."""
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertEqual(safe_division(0, -5), 0.0)

    def test_decimal_numbers(self):
        """Test division with decimal numbers."""
        self.assertAlmostEqual(safe_division(10.5, 2), 5.25)
        self.assertAlmostEqual(safe_division(7.5, 2.5), 3.0)
        self.assertAlmostEqual(safe_division(1, 3), 0.3333333333333333)

    def test_large_numbers(self):
        """Test division with large numbers."""
        self.assertEqual(safe_division(1000000, 1000), 1000.0)
        self.assertEqual(safe_division(1e10, 1e5), 1e5)

    def test_small_numbers(self):
        """Test division with very small numbers."""
        self.assertAlmostEqual(safe_division(0.001, 0.1), 0.01)
        self.assertAlmostEqual(safe_division(1e-10, 1e-5), 1e-5)

    def test_result_types(self):
        """Test that results are of expected types."""
        result = safe_division(10, 2)
        self.assertIsInstance(result, float)
        
        result_none = safe_division(10, 0)
        self.assertIsNone(result_none)


if __name__ == '__main__':
    unittest.main()
