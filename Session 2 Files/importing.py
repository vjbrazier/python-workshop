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