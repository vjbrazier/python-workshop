# Functions are created using def
def sum(num1, num2):
    return num1 + num2

print('Integers: ', sum(1, 2))

# Due to the nature of not being strict, most overloading is unnecessary
print('Floats: ', sum(1.5, 1.5))

# Python executes code line by line. If you call a function, it must be created prior to the call
"""
This will give an error!

print(multiply(2, 3))

def multiply(num1, num2):
    return num1 * num2
"""