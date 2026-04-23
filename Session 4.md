# Docstrings and Type Hints
You've noticed both in Python and other languages that (most) functions and classes will have information when hovered over. This will show you the parameters, the types for the parameters, as well as a description of what the function/class does. Python allows this too, and makes it easy. Let's take a simple function.

```python
def multiply(a: int, b: int) -> int:
    """
    Multiplies two numbers together and returns the result.
    """
    return a * b

print(multiply(2, 3))
```
In the above, you will notice three things. First, to add a type hint to the parameters, you simply follow them with a colon, then the Class name of the type you expect. The single-dash arrow indicates the type of Class name of the return type you expect. The multi-line comment beneath the function definition will be the description you get when hovered over.

You should know that the types are hints however, and Python will not stop you from entering different numbers. It also does not return the type indicated

```python
# This will return 7.5 with no issues
multiply(2.5, 3)
```

For a case like multiply above, you can specify multiple return types using a single |.

```python
def multiply(a: int | float, b: int | float) -> int | float:
    """
    Multiplies two numbers together and returns the result.
    """
    return a * b
```

If something can be empty, simply specify None instead.

While we are here, you should have noticed in the previous session how a function like sorted has two values (key and sorted) that by default, have a value. When declaring a function, you can use = to place a default value. You can still apply type hints to this!

```python
def add(a: int | float, b: int | float, c: int | None | float = None):
    """
    Adds 2-3 numbers together and returns the result.
    """
    if c:
        return a + b + c

    return a + b

print(add(1, 2))
print(add(1, 2, 3))
```

This same logic applies to classes as well, but the description of the class goes under its \_\_init__ function.

```python
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
```

You can take custom or imported classes, and make these a type hint too!

```python
def driveCar(car: Car) -> None:
    car.goVroom(5)

driveCar(honda)
```

Paste these examples in your editor and hover over them to see the effect!

You can also add docstrings to modules, or files. Place the multi-line comment at the top of your file, and if imported elsewhere, hovering over the import will provide the information you've written. You will see this more clearly when we discuss self imports shortly.

```python
"""
This file has some basic examples.
"""
```

# PEP 8 and Pylint
PEP 8 is the styling guide for Python. You can find further insight by searching for the guide yourself (also at this link: https://peps.python.org/pep-0008/)

These styles are suggestions to make your code cleaner, according to devs, and it is updated regularly. However, there is a Visual Studio Code extension called PyLint available that will try to help make suggestions when it notices you are not following the guidelines laid out. Feel free to install it, and each time you save a file, it will comb through and make suggestions. It is not mandatory to follow these, keep that in mind! It also does not catch everything (like type hints, in fact).

# Modifiers
Modifiers are those special functions you saw before. They begin with an @ symbol, and go right above functions. These are functions by themselves, that wrap functions within them to modify how they work, hence the name. We won't be diving into how they work.

```python
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
```

# Self imports
We have already discussed imports before. However, imports in Python work by running all the code in a file. This means you have access to all of the variables, functions, and classes contained in a file created. To grab it, simply write an import with the path to the filename, or the filename itself if it isn't in a different folder.

Doing this will create a \_\_pycache__ folder in the directory it was run from. Feel free to test things with the self_import folder to see it in action (writing it here wouldn't really show it).

# Comprehension
Python supports list and dict comprehension. This is a way to create a list or dictionary in one line, and you can use a variety of operations within this one line. Explaining it in words is hard, so here are some examples.

```python
# Here is a normal for loop which squares a list
numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num * num)

print(squares)
print()

# Comprehension gets its name from being able to shrink this
# You write a for loop within list notation, performing what the loop would
# list = [new_value for item in iterables]
squares = [num * num for num in numbers]
print(squares)
print()

# Comprehension can add conditions into this same statement for filtering
# list = [new_value for item in iterables if condition]
evens = [num for num in numbers if num % 2 == 0]
print(evens)
print()

# You don't need simple arithmetic like in squares. You can call functions on them
names = ['alice', 'bob', 'charlie']
capitalized = [name.capitalize() for name in names] # Capitalize capitalizes the first letter
print(capitalized)
print()

# You can also give your own value in return
# [true if condition else false for item in iterable]
labels = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print(labels)
print()

# Comprehension can be used to create dictionaries, too
# dict = {key:value for item in iterables}
square_map = {num: num * num for num in numbers}
print(square_map)
print()

# You don't need to have a preexisting list/dict for this either
name_length = {
    name: len(name)
    for name in ['Jane', 'Carlos', 'Amy']
}
print(name_length)
print()

# You can use multiple existing lists for this.
# names = ['alice', 'bob', 'charlie]
grades = [95, 60, 75]

student_grades = {name.capitalize(): grade for name, grade in zip(names, grades)}
print(student_grades)
print()
```

You can utilize these basics to make much more advanced comprehension statements. It is typical to see it be used in tandem with files in particular.

```python
import json
from pathlib import Path

# Comprehension is not limited to 1D arrays
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flat = [num for row in matrix for num in row]
print(flat)
print()

# You can still attach conditions
flat = [num for row in matrix for num in row if num % 2 == 0]
print(flat)
print()

# You can perform it on data read from a file!
friend_data_path = Path('data') / 'friends.json'

with open(friend_data_path, 'r') as f:
    friends = json.load(f)

age_mapping = {friend.get('name'): friend.get('age') for friend in friends}
print(age_mapping)
print()

# You can make nested dictionaries as well
students = ['alice', 'bob', 'charlie']
grades = [95, 60, 75]
report_cards = {
    student.capitalize(): {
        'name_length': len(student),
        'uppercase': student.upper(),
        'grade': grade,
        'passing': True if grade > 60 else False
    }
    for student, grade in zip(students, grades)
}

print(report_cards)
```

As you can see, comprehension can quickly get out of hand. To combat this, there is a few general rules of thumb for comprehension:
1. Prioritize readability over finesse. If it is hard to tell what is going on yourself, you should probably use nested loops instead (if possible of course).
2. Comprehension is typically used to create a list/dict quickly, especially when you are creating one based around another (conditions help here). If you are modifying an existing one, you should rethink using comprehension.
3. Even if your comprehension statement is readable for most, you should think of just what it is doing. If you are implementing several functions, conditions, and other checks, you should see about splitting it into multiple parts instead, as relying on one large comprehension is much more likely to cause failure.

You do not need to use comprehension. However, people use it all the time, so having an understanding of it when entering Python is very vital.