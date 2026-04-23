# Example shown

class City:
    # Without using a separate module (which we aren't discussing), static variables don't have type hints
    total_population = 0

    def __init__(self, name: str, population: int):
        """
        Creates a city with a name and population.
        """
        self.name = name
        self.population = population
        City.total_population += population

    def get_population(self) -> int:
        return self.population

    # You've actually seen a modifier before, right here!
    @staticmethod
    def get_total_population() -> int:
        return City.total_population