"""
Helpful math functions.
"""

def add(a: int | float, b: int | float) -> int | float:
    """
    Adds 2 numbers.
    """
    return a + b

def subtract(a: int | float, b: int | float) -> int | float:
    """
    Subtracts 2 numbers.
    """
    return a - b

def multiply(a: int | float, b: int | float) -> int | float:
    """
    Multiplies 2 numbers.
    """
    return a * b

def divide(a: int | float, b: int | float) -> int | float:
    """
    Divides 2 numbers.
    """
    return a / b

# Inserting this here will demonstrate why this if statement is important.
if __name__ == '__main__':
    print('I am main')