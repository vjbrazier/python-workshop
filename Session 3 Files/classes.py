# Although not required, it is recommended to capitalize class names
class Car:
    # The __init__ function is reserved for creation of an object
    def __init__(self, make, model, year):
        # Self refers to the current object. You must assign attributes to it
        self.make = make
        self.model = model
        self.year = year

    # Methods tied to object must start with self as a parameter
    def goVroom(self, n):
        # This returns as many o's as (n + 1)
        return f'Vr{'o' * (n + 1)}m!'
    
# You do not use a new keyword for object creation
honda = Car('Honda', 'Civic', 2012)
print(honda.goVroom(5))