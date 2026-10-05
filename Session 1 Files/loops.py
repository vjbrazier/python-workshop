# There is no do while, only while
var1 = 3

while (var1 != 0):
    print('while')
    var1 -= 1 # Operations like var-- and var++ do not exist in Python

print() # This is just adding a gap for readability

# For loops will iterate on each element of a list, set, or tuple (called iterables)
fruits = ['apple', 'banana', 'coconut']

for fruit in fruits:
    print(fruit)

print()

# For loops do not effect the array itself if you modify the iterator
for fruit in fruits:
    fruit = 'broccoli'

print(fruits)

print()

# You can still do a for loop with a set count using range
for i in range(0, 3):
    print('for')

print()

# len() gets the size of an iterable. Pair this with range, and you can modify an array's items
for i in range(0, len(fruits)):
    fruits[i] = 'broccoli'

print(fruits)