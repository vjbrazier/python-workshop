class City:
    # A variable declared right in the class is static and shared across objects
    total_population = 0

    def __init__(self, name, population):
        self.name = name
        self.population = population

        # You target static variables by preceding the with the class name
        City.total_population += population

    def get_population(self):
        return self.population

    # Put this right above a static method to make it such
    @staticmethod
    def get_total_population(): # Self is not needed
        return City.total_population

# You can see here that objects can have their own attribute that are separate from each other
print('Unique populations:')
houston = City('Houston', 1000)
dallas = City('Dallas', 2000)

print('Houston:', houston.get_population())
print('Dallas:', dallas.get_population())
print()

# A static variable is the same independent of object
print('Total population:')
print(houston.get_total_population())
print(dallas.get_total_population())
print(City.get_total_population()) # Static methods don't require an object to be called