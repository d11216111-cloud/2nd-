"""
Unit tests for the safe_division function
"""

import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """Test cases for the safe_division function"""
    
    def test_normal_division(self):
        """Test normal division with positive numbers"""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(100, 4), 25.0)
        self.assertEqual(safe_division(7, 2), 3.5)
    
    def test_negative_division(self):
        """Test division with negative numbers"""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
    
    def test_boundary_values(self):
        """Test division with boundary values"""
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertEqual(safe_division(1, 1), 1.0)
        self.assertAlmostEqual(safe_division(1, 3), 0.3333333333333333)
    
    def test_division_by_zero(self):
        """Test division by zero returns None instead of raising an exception"""
        self.assertIsNone(safe_division(10, 0))
        self.assertIsNone(safe_division(-10, 0))
        self.assertIsNone(safe_division(0, 0))
    
    def test_large_numbers(self):
        """Test division with large numbers"""
        self.assertEqual(safe_division(1000000, 1000), 1000.0)
        self.assertEqual(safe_division(999999, 3), 333333.0)
    
    def test_decimal_division(self):
        """Test division with decimal numbers"""
        self.assertEqual(safe_division(5.5, 2), 2.75)
        self.assertEqual(safe_division(10.5, 3.5), 3.0)


if __name__ == '__main__':
    unittest.main()
