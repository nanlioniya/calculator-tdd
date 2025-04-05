class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        """減法功能"""
        return a - b

    def multiply(self, a, b):
        """乘法功能"""
        return a * b

    def divide(self, a, b):
        """
        除法功能
        回傳浮點數結果
        如果除數為0，拋出ValueError
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return float(a) / b