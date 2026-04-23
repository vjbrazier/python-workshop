"""
This file has some basic examples.
"""

# Sample code from notes
def multiply(a: int | float, b: int | float) -> int | float:
    """
    Multiplies two numbers together and returns the result.
    """
    return a * b

print(multiply(2, 3))

def add(a: int | float, b: int | float, c: int | None | float = None):
    """
    Adds 2-3 numbers together and returns the result.
    """
    if c:
        return a + b + c

    return a + b

print(add(1, 2))
print(add(1, 2, 3))

class Car:
    # You do not need a type hint for self, nor a return for __init__
    def __init__(self, make: str, model: str, year: int):
        """
        A car with a make, model, and year.
        """
        self.make = make
        self.model = model
        self.year = year

    def goVroom(self, n: int) -> None:
        """
        Prints Vroom with (n + 1) os behind it
        """
        return f'Vr{'o' * (n + 1)}m!'
    
honda = Car('Honda', 'Civic', 2012)
print(honda.goVroom(5))

def driveCar(car: Car) -> None:
    car.goVroom(5)

driveCar(honda)