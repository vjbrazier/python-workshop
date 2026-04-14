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