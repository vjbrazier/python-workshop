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