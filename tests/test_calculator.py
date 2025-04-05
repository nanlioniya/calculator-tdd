import unittest
from calculator.calculator import Calculator  # The class we are going to implement

class CalcTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        # 印出當前執行的測試方法名稱
        print(f"\n執行測試: {self._testMethodName}")

    def test_add(self):
        """測試加法功能"""
        test_cases = [(3, 5, 8), (-1, 1, 0), (-1, -1, -2)]
        for a, b, expected in test_cases:
            with self.subTest(f"{a} + {b} = {expected}"):
                result = self.calc.add(a, b)
                print(f"測試: {a} + {b} = {result} (預期: {expected})")
                self.assertEqual(result, expected)

    def test_subtract(self):
        """測試減法功能"""
        test_cases = [(5, 3, 2), (1, 5, -4), (-1, -1, 0)]
        for a, b, expected in test_cases:
            with self.subTest(f"{a} - {b} = {expected}"):
                result = self.calc.subtract(a, b)
                print(f"測試: {a} - {b} = {result} (預期: {expected})")
                self.assertEqual(result, expected)

    def test_multiply(self):
        """測試乘法功能"""
        test_cases = [(3, 5, 15), (-2, 3, -6), (0, 5, 0)]
        for a, b, expected in test_cases:
            with self.subTest(f"{a} * {b} = {expected}"):
                result = self.calc.multiply(a, b)
                print(f"測試: {a} * {b} = {result} (預期: {expected})")
                self.assertEqual(result, expected)

    def test_divide(self):
        """測試除法功能"""
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
        
        # 測試除以零的情況
        print("\n測試除以零的情況")
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
        print("成功捕獲除以零錯誤")

if __name__ == '__main__':
    # 使用更詳細的輸出
    unittest.main(verbosity=2)