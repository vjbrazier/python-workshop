# Classes and Objects
In Python classes are created with the keyword class followed by a code block describing the class. Here, functions and variables can be defined for the class. To make a class constructor, a function called \_\_init__ needs to be defined. This function is what runs when you call the class and creates a new object of that type. Object methods require the first argument to be self. It is not required, but recommended to name classes with a capital letter.

```python
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
```

# Inheritance and Polymorphism
Inheritance in Python is done by adding parenthesis and the desired superclass next to the initial class statement. Python does support multi-inheritance (in the form of a comma'd list), however, we won't delve into that as it is a bit confusing.

The keyword super is used to make use of the superclass. By default, all methods are available to the subclass, and overriding just entails rewriting the method.

```python
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
```

# Static variables and methods
Static variables are just placed within the class itself as a standalone variable. You can access the variable by preceding it with the class name. For methods you can skip the self parameter, however, it is recommended to instead use the @staticmethod modifier prior to the method's creation. Similar to static variables, static methods are called by preceding with the class name.

```python
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
```

# Access modifiers
There are no keywords tied to access modifiers in Python. Instead, it uses naming conventions.
<li><b>Public</b> variables and methods are just declared like usual
<li><b>Protected</b> variables and methods are preceded by a single underscore
<li><b>Private</b> variables and methods are preceded by two underscores

```python
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
```

# Zip
Zip is a function used to wrap two or more iterables together, allowing for multi-traversal with a for loop. This traversal is done in the way you would do so for the items function of dictionaries, where in the loop you declare comma separated variables. For zip, you declare one variable per iterable provided.

It should be noted that there is not a limit on the amount of iterables you can provide. By default however, it will only contain up to the length of the shortest iterable provided.

```python
# Let's make two sample lists
nums = [1, 2, 3]
fruits = ['apple', 'banana', 'coconut']

# You can iterate over both at once using zip
for num, fruit in zip(nums, fruits):
    print(num)
    print(fruit)
print()

# This has no limit on the amount of lists
vegetables = ['asparagus', 'broccoli', 'carrot']

for num, fruit, vegetable in zip(nums, fruits, vegetables):
    print(num)
    print(fruit)
    print(vegetable)
print()

# However, it will stop iterating at the end of the shortest list
nums = [1, 2]

# This will stop at 2, 'banana'
for num, fruit in zip(nums, fruits):
    print(num)
    print(fruit)
```

# Enumerate
Enumerate is a way to keep count whilst traversing an iterable. It takes an iterable, and will provide two values that can be used in a for loop. A helpful feature is that you can specify a start value over its normal behavior of starting at 0.

```python
import json
from pathlib import Path

# Enumerate counts alongside a list
fruits = ['apple', 'banana', 'coconut']

# It uses a lazy iterator, making it faster than managing your own index variable
for index, fruit in enumerate(fruits):
    print(index)
    print(fruit)
print()

# This seems pointless, so here's a use case
friends_data = Path('data') / 'friends.json'

with open(friends_data, 'r') as f:
    friends = json.load(f)

# You can also add a start parameter (the default is 0)
for index, friend in enumerate(friends, start=1):
    print(f'{index}. {friend.get('name')}')
print()

try:
    choice = int(input('Who\'s email do you need? (enter their number) '))
    print(friends[choice - 1].get('email'))
except ValueError:
    print('Please input a number.')
```

# Sorted
You can sort iterables using the sorted function. It takes the iterable you want to sort, but has two additional parameters. You can use key to determine what it sorts by, such as applying the len() function to a list of strings. While it normally sorts in ascending order, you can do descending instead by flipping reverse to True.

```python
# Sorted is a function that does exactly what you'd expect
nums = [42, 7, 89, 13, 56, 2, 91, 34, 68, 25]

# It is a function that returns. You need to assign it
sorted(nums)
print(nums) # Unsorted

nums = sorted(nums)
print(nums) # Sorted
print()

# It supports more than just numbers, too
fruits = ['mango', 'apple', 'kiwi', 'banana', 'cherry', 'orange', 'grape', 'pear', 'pineapple', 'strawberry']
print(sorted(fruits))

# By default, it does ascending order. You can add reverse to change this
print(sorted(fruits, reverse=True))
print()

# You can also add key, which takes a function. This will sort by the function
# A simple example is len(). This will sort by the length of each word
print(sorted(fruits, key=len)) # It takes function name, not a call. No parenthesis

# This can be reversed too
print(sorted(fruits, key=len, reverse=True))
```

# if \_\_name__ == \_\_main__
In most Python code, it is common to see this line at the bottom:

```python
if __name__ == '__main__':
    # Code
```

What does this do though?

Name is used to find the name of the current module running. When you import a module, it runs under the name of the module, which is typically just the name of the file itself. However, main is a special name. Main is assigned to the file you executed, meaning only the starting file holds this name.

The benefit of using this means that any code under this if statement will only run if you choose to run the file, but you can still import it elsewhere in your code. For a small few files, this can feel insignificant, but when you have dozens of files working in tandem, utilizing each other, this single statement can easily resolve a lot of unnecessary code from running with no need to chase down other files.

A better example of this can be found in the Session 4 files, where we discuss self imports more.