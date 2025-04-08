"""Test suite for the calculator package."""

import unittest
from calculator.calculator import Calculator


class CalcTest(unittest.TestCase):
    """Test cases for the Calculator class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
        print(f"\n執行測試: {self._testMethodName}")

    def test_add(self):
        """Test addition functionality."""
        test_cases = [(3, 5, 8), (-1, 1, 0), (-1, -1, -2)]
        for a, b, expected in test_cases:
            with self.subTest(f"{a} + {b} = {expected}"):
                result = self.calc.add(a, b)
                print(f"測試: {a} + {b} = {result} (預期: {expected})")
                self.assertEqual(result, expected)

    def test_subtract(self):
        """Test subtraction functionality."""
        test_cases = [(5, 3, 2), (1, 5, -4), (-1, -1, 0)]
        for a, b, expected in test_cases:
            with self.subTest(f"{a} - {b} = {expected}"):
                result = self.calc.subtract(a, b)
                print(f"測試: {a} - {b} = {result} (預期: {expected})")
                self.assertEqual(result, expected)

    def test_multiply(self):
        """Test multiplication functionality."""
        test_cases = [(3, 5, 15), (-2, 3, -6), (0, 5, 0)]
        for a, b, expected in test_cases:
            with self.subTest(f"{a} * {b} = {expected}"):
                result = self.calc.multiply(a, b)
                print(f"測試: {a} * {b} = {result} (預期: {expected})")
                self.assertEqual(result, expected)

    def test_divide(self):
        """Test division functionality."""
        test_cases = [
            (6, 2, 3.0),
            (-6, 2, -3.0),
            (5, 2, 2.5)
        ]
        for a, b, expected in test_cases:
            with self.subTest(f"{a} / {b} = {expected}"):
                result = self.calc.divide(a, b)
                print(f"測試: {a} / {b} = {result} (預期: {expected})")
                self.assertEqual(result, expected)
        
        print("\n測試除以零的情況")
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
        print("成功捕獲除以零錯誤")


if __name__ == '__main__':
    unittest.main(verbosity=2)

