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

# Error Handling
Error handling in Python is the same as in other languages. The keywords “try”, “except”, and “finally” are used. In the try block is where code that could throw an error is placed. If an error does occur it is caught and handled by code in the except block. Regardless if there is an error or not, the code in the finally block will run. You can create custom errors using raise.

```python
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
```

# Imports
Python comes with a lot of libraries that can be used for a myriad of classes, functions, and objects. There are three ways to import from a library: 
<li><b>Import</b> alone will import an entire library. You must precede any usage with the name of the library. 
<li><b>From <i>library</i> import <i>___</i></b> will import a specific item from a library. You can do list with commas if you want more than one. When imported like this, you do not need to precede it with the library name. 
<li><b>Import <i>library</i> as <i>name</i></b> will import an entirely library, but under a different name of your choice. It is utilized the same as the first method, but this alias can be whatever you’d like. 

```python
# Importing can be done in three ways in Python
import math # This will import the entire package
from random import randint # This will import the specified class/function
import os as operating_system # This will import a package and rename it

# To use a math function, you need to precede it with math
print(math.log(9, 3))

# To use randint, you can just call it
print(randint(0, 10))

# To use os, you need to precede with operating_system instead
print(operating_system.cpu_count())
```

# Dictionary Functions
Dictionaries can be directly addressed similar to lists, using []. Also similarly, referencing a non-existing key (like a non-existent index) will cause an error to occur, stopping your code. Dictionaries come with several useful methods to address this: 
<li><b>Get</b> allows you retrieve a value without an error occurring if it does not exist. If one doesn’t exist, you will receive None, but you can change what it returns. 
<li><b>Setdefault</b> allows you to create a new key-value pair without overwriting an existing one. If you try to overwrite an existing key, it will do nothing, but if the key does not exist, it will make one with the value you have provided 
<li><b>Pop</b> can be used to remove an existing key-value pair. If the key does not exist, it will give an error, but you can add a different default instead. 
<li><b>Keys</b> will return a list of all the keys in a dictionary. 
<li><b>Values</b> will return a list of all the values in a dictionary. 
<li><b>Items</b> will return a list with two tuples, the first containing the keys, the second containing the values 
<br> <br>
The keys, values, and items methods all return lists, meaning you can iterate over them with a normal for loop (items does so a little differently, you will see in the example)  <br> <br>

```python
# Dictionaries have several useful methods in them
example_dict = {
    'key1': 1,
    'key2': 2,
    'key3': 3
}

# Without methods, you can grab key values using []
print(f'Key1 is: {example_dict['key1']}')

# If you use the above on a non-existent key, an error occurs. Use get to prevent this, and receive None instead
print(f'Key4 is: {example_dict.get('key4')}')

# You can use pop to delete a key. This takes a second parameter that gives a default over an error
print(f'Deleting key10: {example_dict.pop('key10', 'Key doesn\'t exist!')}')

# Get can also be used to provide a default value if one isn't present
print(f'Key5 is: {example_dict.get('key5', 'Key doesn\'t exist!')}')

# If you need a key to exist but are unsure if it does, you can use setdefault
example_dict.setdefault('key3', True) # If the key exists, it does not get overwritten
example_dict.setdefault('key4', 4)
print(example_dict)

# The keys method provides all of the keys in a dictionary
print(example_dict.keys())

# The values method provides all of the values in a dictionary
print(example_dict.values())

# You can use items to get both. This is primarily for use in for loops
print(example_dict.items()) # This will return a array of tuples

# You can iterate over items like so
for key, value in example_dict.items():
    print(f'There is a pair of {key} and {value}')
```

# File reading/writing (I/O)
You can use open to open a file in Python alone. However, you should always use the with function in conjunction, as it will automatically close the file for you. You can use this to read from files, as well as write to files, or create them. Using with also passes the file into a temporary variable of your choice, making usage even more convenient.

```python
# When processing JSON, we use the library
import json

# This is the path to our file
small_user_data_file = 'data\\small_users.json'

# Python has a built in with function for use with files. It closes it automatically
with open(small_user_data_file, 'r') as file: # 'r' here means read
    small_users = json.load(file) # This will parse the data from a string into usable Python

# Our JSON data is a list, so we can iterate over it
for user in small_users:
    if user.get('isAdult'):
        print(user)

# You can use with to create and write to a file too. You must pass 'w' as an argument in open
nonexistent_file = 'data\\nonexistent_file.txt' # The file will be created under this path with this name

with open(nonexistent_file, 'w') as file:
    file.write('This file now exists!')

# Do note that you can rename 'file' in with
receipts = {
    'Meijer': {
        'fruit': ['cherries', 'apples'],
        'cleaning': ['glass_cleaner', 'disinfectant']
    },
    'Walmart': {
        'vegetables': ['broccoli', 'lettuce'],
        'paper_towel': 2
    }
}

receipt_file = 'data\\receipts.json'

# You can pass a variable for writing using json.dump
with open(receipt_file, 'w') as my_receipts:
    json.dump(receipts, my_receipts, indent=4) # Without indent, it will all be on one line

"""
# For this small user data file, this seems useless. If we use a much larger file however, you can see the use.
large_user_data_file = 'data\\large_users.json'

with open(large_user_data_file) as file:
    large_users = json.load(file)

for user in large_users:
    if user.get('isAdult'):
        print(user)
"""
```

If you want more practice, there is a friends.json file available under the data folder. Try writing some code that can:
<li>Read the file, and print to the console only people that are younger than 30
<li>Choose a random person, and iterate over their hobbies, printing them off
<li>Choose a random person, and iterate through the address dictionary use the list function
<li>Write a new file consisting of every other individual listed in friends.json (hint: you should make use of continue for this)
<br><br>

A more advanced example of file usage is available under adv_files.py. It shows a little more of the benefit of reading/writing from denser JSON files, rather than a simple one.

# OS
When you need to interact with the operating system, you will want to use the os library. It is also used to interact with the environment you are in; you can modify files and directories, and get general information on the operating system being used.

Here are some common os functions:
<li><b>os.getcwd</b> stands for "get current working directory", to find where you are located.
<li><b>os.listdir</b> lists the names and folders inside a directory. You can use "." to use the current working directory.
<li><b>os.mkdir</b> makes a new directory in the current working directory.
<li><b>os.makedirs</b> makes a new directory, alongside any missing parent directories.
<li><b>os.path.exists</b> checks if a path/file exists or not, returning a boolean.
<li><b>os.name</b> gives a code for the current operating system. "nt" is Windows, "posix" Linux, MacOS, and other POSIX systems.
<li><b>os.remove</b> deletes a file.

Here are some examples of these functions in action:

```python
# First, import the library
import os

# Getting the current directory
current_dir = os.getcwd()
print(current_dir)
print()

# List files in directory
print(os.listdir('.')) # This will use the current_dir
print()
print(os.listdir('data'))
print()

# Making directories
os.mkdir('example_dir')
os.makedirs('dir1/dir2/dir3')

# You can use exist_ok to avoid errors
os.makedirs('dir1/dir2/dir3', exist_ok=True)
# This would error without it, due to it already existing

# Checking existence
if os.path.exists('data'):
    print('Data folder present!')
else:
    print('No data folder.')
print()

# OS name
print('Your operating system is:', os.name)
print()

# Delete a file
pause = input('Press enter to delete the file')
os.remove('deleteme.txt')
```

<br><br>

# Path
You likely missed something very important in the file examples. When we read/wrote to files, we had to pass the location of the file. For the first example, this was 'data\\small_users.json'. However, there is actually a critical flaw with doing this.

Python works on any operating system. This creates a problem, because Windows uses a different slash to get to files. Windows uses a backslash (\), while MacOS/Linux uses a forward slash (/). When you hardcode your file locations as we did in the Windows format, it will fail on other systems. This is where the Path class from pathlib comes in.

To use Path, you need to break the path to the file you want into parts separated by folders. So, for example:
```
data/receipts/meijer/receipt.json
```
In this, we have 3 folders prior to the 1 file. To access this, divide by folders, with the file itself being at the end. So:

```
data
receipts
meijer
receipt.json
```

These 4 chunks are key. Within our Python code, you will first create a Path object utilizing the root folder in this path. For our example, that would be data. Following that, use a / to continue adding the subsequent folders, up until the file. The Path module overwrites division in this scenario, to create a custom object that works across any OS. So for the above:

```python
from pathlib import Path

file_path = Path('data') / 'receipts' / 'meijer' / 'receipt.json
```

There is a path_demo folder that contains a path_demo.py file. You'll see some code that corresponds to the data in the folder. If you have a dual-booting device, or a VM, feel free to test it for yourself and you'll see that the non-Path way of accessing the file fails!

# Shutil
Shutil stands for shell utilies. It is used for copying, moving, and removing files & folders.

There are a few important functions to know:
<li><b>shutil.copy</b> will copy the file provided.
<li><b>shutil.copy2</b> is the same, but will try to preserve more metadata.
<li><b>shutil.copytree</b> will copy an entire directory and its contents, including subdirectories.
<li><b>shutil.move</b> will move a file, but can also rename it. This will overwrite existing files.
<li><b>shutil.rmtree</b> will delete an entire directory, including subdirectories.

<br><br>

You can see these functions in action below:

```python
# First, import the library
import shutil
from pathlib import Path

# Copy a file
shutil.copy('example.txt', 'example_copy.txt')

# You can also copy it into a folder
example_folder = Path('example_folder')
shutil.copy('example.txt', example_folder / 'example_copy.txt')

# You can copy an entire tree and its contents
shutil.copytree('nested', 'nested_backup')

# You can use dirs_exist_ok=True to make it append to a tree if it exists
shutil.copytree('example_folder', 'nested_backup', dirs_exist_ok=True)

# You can move a file
shutil.move('example2.txt', 'copies')

# This is also used to rename. This will overwrite files, be careful
shutil.move('example3.txt', 'different_example.txt')

# You can also delete an entire directory
pause = input('Press enter to delete the nested_backup folder:')
shutil.rmtree('nested_backup')
```