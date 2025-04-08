"""Calculator module providing basic arithmetic operations."""


class Calculator:
    """A simple calculator class that provides basic arithmetic operations."""

    def add(self, a, b):
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The difference between a and b
        """
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        return a * b

    def divide(self, a, b):
        """Divide two numbers.
        
        Args:
            a: First number (dividend)
            b: Second number (divisor)
            
        Returns:
            The quotient of a divided by b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

