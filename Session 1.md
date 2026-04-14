# Install Python
You can install Python at python.org/downloads <br>
If you have admin, add it to your PATH when prompted during the installation <br>

Alternatively, you can install it with Winget

```batch
winget install Python.Python.3.14
```

You will also need Visual Studio Code installed. You can either search for it, or use Winget

```batch
winget install Microsoft.VisualStudioCode
```
After installing it, you will need to get the Python extension in VS Code for your code to work properly.

# Alternative: Google Colab
If you'd prefer not to install anything, you can instead use Google Colab. Search for it, and sign in with your Google account. You will want to create a new notebook.

Once you are in a notebook, you will see segments for writing code. Colab will automatically detect that it is Python. You can write code in individual blocks and run them individually, or run everything all at once. This only requires a google account, and is saved to the cloud for you, so no need to track files!

# Hello world!
Now that Python is installed, we can make our first script. Make a new file called hello.py in VSCode, then type the following:

```python
print('Hello world!')
```
After saving, open your terminal with CTRL + SHIFT + `, and run
```bash
python ./hello.py
```

You should see "Hello world!" appear in your terminal.

# Comments
Documenting your code is very useful and helpful. Python provides two ways to write comments.
```python
# This is a single-line comment
print('Hello world!') # You can insert them like this too

"""
This is a multi-line comment
This is another line
WOAH! A third line!
"""
```

# Data types
Every variable in Python is an object. No type declaration is needed, you don't even need to state that you are making a variable. Every variable must be initialized however. Here are some common data types in Python: <br>
<li><b>Integers</b> are regular whole numbers.
<li><b>Floats</b> are non-whole or 'decimal' numbers with 64-bit precision.
<li><b>Booleans</b> are written capitalized (True, False).
<li><b>Strings</b> are written with single or double quotes. There are no chars in Python.
<li><b>Lists</b> are mutable and can have mixed types. They are called lists in Python, and are like arrays in other languages.
<li><b>None</b> is the equivalent to null in other languages.

```python
# This is an integer
var1 = 3

# This is a float
var2 = 3.14

# This is a boolean value
var3 = False

# This is a string
var4 = 'This is a string'
var5 = "This is also a string"

# This is a list. It can contain variables of different types, and is mutable
var6 = [3, 3.14, var3, 'This is a string', var5]
var6[0] = 4 # You can index a list

# If you don't have a value yet, use None
var7 = None
```

# Printing
As shown before, Python uses a fucntion called print to write text to the console. it takes any value, not just strings. These values include arrays as well; you do not need to iterate over it like most languages require. by splitting variables with commas it will automatically add spaces.
Python also has an f-string. This is used to write a string with variables mixed in and allows formatting of those variables. For example, you can round off a float.
```python
var1 = 3
var2 = 3.14
var3 = False
var4 = 'String1'
var5 = "String2"
var6 = [var1, var2, var3, var4, var5]

# Printing
print(var1)

# Comma printing
print(var2, var3, var4, var5)

# Array printing
print(var6)

# F-strings
name = 'Vincent'
print(f'Hello, my name is {name}')

value = 3.14159
print(f'Pi is about {value:.2f}')

# You can use f-strings like this, too
print(f'1 + 1 = {1 + 1}')
```

# User input
You can get users to enter data by using the input() function. This function by default returns only strings, and they match exactly what was typed. If you are looking for number input, you will need to convert it prior to usage.
You can also add a question string to be printed to the user, which won't be attached to the string that the user inputs.
```python
# The question is not attached to the input
name = input('What is your name?\n') # \n isn't required, but is nice
print(f'Hello {name}!')
```
# Type conversion
There are two main ways to convert data types in Python
<li><b>Implicit</b>: Occurs in scenarios where you add an int and a float. It will make both into a float prior to adding.
<li><b>Explicit</b>: You can convert using int(), float(), str(), and bool().

```python
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
```

# Advanced data types
Python contains a few additional data types that are more advanced. <br>
<li><b>Tuples</b> are immutable lists or strings. Duplicates are allowed in these. They are written as a list, but with parenthesis. 
<li><b>Sets</b> are immutable lists. Duplicated are removed. They are written like a list, but with curly braces. 
<li><b>Dicts</b> are composed of key-value pairs and are written with curly braces. Having a single pair in a variable creates a dict, rather than a set. <br> <br>

These can be converted from one to another using list(), tuple(), set(), and dict(). 
```python
# A list is mutable
arr = [1, 2, 3, 4, 5]
print(f'List before change: {arr}')

arr[0] = 5
print(f'List after change:  {arr}')

# Tuples are immutable and allow duplicates
# tup = tuple(arr) <- You can convert into a tuple
tup = (5, 2, 3, 4, 5)
print(f'Tuple: {tup}')
# tup[0] = 1 <- This will give an error!

# Sets are mutable, and do not allow duplicates. You cannot use indexing on them
# example_set = set(arr)
example_set = {5, 2, 3, 4, 5}
print(f'Set before change: {example_set}')
example_set.add(6)
print(f'Set after change:  {example_set}')
# print(example_set[0]) <- This will give an error!

# Dicts are key-value pairs. They are mutable.
# If no pairs are present, it will become a set.
example_dict = {
    'key1': 1,
    2: '2',
    'groceries': ['eggs', 'milk'],
    'dict': {
        'list': arr,
        'tuple': tup,
        'set': example_set
    }
}
print(example_dict)

# We will cover dicts more thoroughly in session 2 for I/O and JSON
```

# If, else-if, else
Python uses if-else statements for its basic logic. Else if is written as “elif”. However, you do not wrap the code in curly braces but instead need to add a colon to the end of the statement. Code blocks, such as the statements after an “if” statement, use indentation instead of curly braces seen in other languages 
```python
# If statements are written as so
if True:
    print('if')
    print('indent')

elif True:
    print('elif')
    print('indent')

else:
    print('else')
    print('indent')

# Note the colon and indent
```

# Logic
The types of logic available in Python are broader, with specific uses: <br>
<li>For the basic logic, Python uses “and” and “or”, instead of && and || like some other languages. 
<li>When comparing size, Python uses >= and <=. 
<li>When checking for equality, Python uses is, and ==. == is for value comparison, such as checking if two numbers are equal. is is for identity, such as comparing arrays, or checking if something is None (Python’s equivalent to null) 
<li>When checking for inequality, Python uses is not, and !=. These follow the same rules for above. 
<li>If you are negating something, you need to precede it with not. A single ! will give you an error. 

```python
# AND, OR
var1 = True
var2 = False

if var1 and var2:
    print('AND')

if var1 or var2:
    print('OR')

# Value comparisons and equality
var3 = 1
var4 = 2

# You can use basic >, <, >=, and <=

# == and != are used to compare values
if var3 == var4:
    print('Equal')

if var3 != var4:
    print('Not equal')

# is and is not are used to compare identity (objects), or checking for None
var5 = [1, 2, 3]
var6 = [1, 2, 3]
var7 = None

if var5 is var6:
    print('Same array')

if var5 is not var6:
    print('Different arrays')

if var7:
    print('Not None')

# You do not reverse values with ! in Python. You must use not
var8 = False

if not var8:
    print('var8 is False')

# You can check for values contained in an iterable with the word in
var9 = [1, 2, 3]

if 2 in var9:
    print('in')
```
# Loops
Python has two types of loops: while and for. Both are declared with their key words, ended with a colon, then have accompanied code indented. For loops in Python are a little different from other languages you might be familiar with. 
<li><b>While loops</b> run as long as the condition evaluates to true
<li><b>For loops</b> iterate on each element of a provided list, set, or tuple

```python
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
```

# Functions
You can declare a function using the def keyword. This follows the same pattern of a colon at the end and indented code beneath, as in loops

```python
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
```

# Break, continue, and pass
These are primarily used in if statements within loops but do have use-cases elsewhere. We will talk about them in the usage of a loop, as it is the most common. 
<li><b>Break:</b> Will completely leave the loop once encountered. The loop will not resume, and you will continue the code after the loop
<li><b>Continue:</b> Will skip the current loop. The code past the line will not be executed, and the loop will start again from the top.
<li><b>Pass:</b> Will continue the code after the line. These are typically not used but do exist. 

```python
# Break will end a loop entirely
for i in range(0, 5):
    if i == 3:
        break
    print(i)

print()

# Continue will skip the current loop
for i in range(0, 5):
    if i == 3:
        continue
    print(i)

print()

# Pass will do nothing and continue on
for i in range(0, 5):
    if i == 3:
        pass
    print(i)
```

# List methods
There are many useful methods built into lists.
<li><b>Append</b> adds an element to the end of a list.
<li><b>Insert</b> adds an element to the specified position.
<li><b>Pop</b> removes the element at the end. You can alternatively specify an index to remove
<li><b>Index</b> will return the index of the value specified
<li><b>A colon</b> provides a range of values from a list.
<li><b>A negative index</b> will start from the end of a list.

```python
# Lists have several useful methods
arr = [1, 2, 3, 4, 5]
print(f'Original list: {arr}')

# Appending adds the given element to the end of the list
arr.append(10)
print(f'Appended list: {arr}')

# You can use insert to set where it will go
arr.insert(5, 6)
print(f'Inserted to index 5: {arr}')

# Popping removes the element at the end of the list
arr.pop()
print(f'Popped list: {arr}')

# You can specify an index to pop as well
arr.pop(0)
print(f'Popped index 0: {arr}')

# You can use index to find where a value is located
print(f'The number 5 is at index {arr.index(5)}')

# You can use a colon to grab a range indices. The second value is where it stops
print(f'Elements 0-2: {arr[0:2]}')

# You can use negatives to start from the end of a list
print(f'The second to last element: {arr[-2]}')
```

# Pros & Cons of Python
Python is the most popular programming language in the world and has use-cases everywhere. However, there are of course pros and cons to it. 
<br><br>
Some Pros: 
<li>Python makes many tasks simple, so writing usable code is extremely quick 
<li>Due to its flexibility on mixing types, processing data is often very fast, and doesn’t require much handling 
<li>There are thousands of Python libraries available for almost anything you need 
<br> <br>
Some Cons: 
<li>Python is notorious for being much slower to run. This is because it is an interpreted language. 
<li>Python is often criticized for its formatting, as although it requires indentation, there isn’t much else enforced to make things readable 
<li>The lack of strict types, as well as allowing a mixture of data can make it tricky to debug Python code, especially the more complex it is. 