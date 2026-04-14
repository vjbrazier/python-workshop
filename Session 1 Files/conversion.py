# Implicit conversion
var1 = 1
var2 = 1.5
print(f'Implicit: {var1 + var2}') # var1 is automatically converted

# Explicit conversion
var3 = '1.5'

print(f'Int conversion: {int(var2) + 2}') # If you use int on a float, it doesn't round, it drops
print(f'Float conversion: {float(var3) + 1.5}')
print(f'String conversion: {str(var2) + ' is a decimal'}')
print(f'Bool conversion: {bool(var1)}')

# Overwriting
var1 = False # Despite 1 being True, you can overwrite it
print(var1)