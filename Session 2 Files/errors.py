# Python uses try, except, and finally for errors
var1 = True

# You do not need to specify an exception type
try:
    var1 = False
    print(var1)
except:
    print('An exception occured!')
print()

# A finally can be added as well
try:
    var1[0] = 'e'
except:
    print('An exception occurred!')
finally:
    print('Error handling is over now')
print()

# For generic exceptions, you can provide a name using 'except Exception as name'
try:
    var1[0] = 'e'
except Exception as e:
    print(f'Something went wrong: {e}')
print()

# Adding error handling means that your code will not stop when an error occurs. You can specify the exception too
var2 = [1]
try:
    var2[1] = 0
except IndexError:
    print('You are overwriting a non-existent index.')
print()

# You can add multiple exception blocks. They do not all have to be specific
try:
    var2[1] = 0
except InterruptedError:
    print('Interrupted')
except:
    print('Unknown error')
print()

# A unique feature of Python is that you can catch multiple errors in one exception block with parenthesis
var3 = [0, 1, '2']

for i in range(0, 4):
    try:
        var3[i] = 5 / var3[i]
    except (ZeroDivisionError, TypeError, IndexError) as e:
        print(f'An exception occurred: {e}')

# Printing here shows that the one acceptable value (1) was modified and the rest unchanged
print(var3)
print()

# You can also raise your own exception for a custom error
# If it is raised outside of a try exception, the program will end
var4 = 1

def check(num):
    if num != 0:
        raise Exception('I hate 0')
    
try:
    check(var4)
except Exception as e:
    print(f'Exception occurred: {e}')