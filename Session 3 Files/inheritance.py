# The super class remains unchanged from before
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def goVroom(self, n):
        return f'Vr{'o' * (n + 1)}m!'
    
# Pass the super class in parenthesis
class Truck(Car):
    def __init__(self, make, model, year, lifted):
        # You can call methods from the original using super()
        super().__init__(make, model, year) # For creation, call the __init__ of the super
        self.lifed = lifted

    # You can override an existing method
    def goVroom(self, n):
        # Utilize super() again, this time taking the method
        return super().goVroom(n).upper() # Upper makes a string all uppercase

cars = [Car('Honda', 'Civic', 2012), Truck('Ford', 'Ram', 2025, True)]

for car in cars:
    print(car.model, car.goVroom(5))