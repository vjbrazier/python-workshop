# Same chain of classes from before with modifiers
class Car:
    # Protected variables and methods have a single underscore
    _protected = 'Shared with subclasses!'
    def _printMake(self):
        print(self.make)

    # Private variables and methods have a double underscore
    __private = 'Me and me alone'

    def _printMake(self):
        print(self.make)

    def __printPrivate(self):
        print(self.__private)

    def showPrivate(self):
        self.__printPrivate()

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def goVroom(self, n):
        return f'Vr{'o' * (n + 1)}m!'
    
class Truck(Car):
    def __init__(self, make, model, year, lifted):
        super().__init__(make, model, year)
        self.lifed = lifted

    def goVroom(self, n):
        return super().goVroom(n).upper()
    
honda = Car('Honda', 'Civic', 2012)
ford = Truck('Ford', 'Ram', 2025, True)

# The ford object has access to the protected in Car
print(ford._protected)
ford._printMake()

ford.showPrivate()

# Honda can use private from its own class
honda.showPrivate()