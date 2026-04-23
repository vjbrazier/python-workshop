"""
A car class.
"""
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