# Sorted is a function that does exactly what you'd expect
nums = [42, 7, 89, 13, 56, 2, 91, 34, 68, 25]

# It is a function that returns. You need to assign it
sorted(nums)
print(nums) # Unsorted

nums = sorted(nums)
print(nums) # Sorted
print()

# It supports more than just numbers, too
fruits = ['mango', 'apple', 'kiwi', 'banana', 'cherry', 'orange', 'grape', 'pear', 'pineapple', 'strawberry']
print(sorted(fruits))

# By default, it does ascending order. You can add reverse to change this
print(sorted(fruits, reverse=True))
print()

# You can also add key, which takes a function. This will sort by the function
# A simple example is len(). This will sort by the length of each word
print(sorted(fruits, key=len)) # It takes function name, not a call. No parenthesis

# This can be reversed too
print(sorted(fruits, key=len, reverse=True))