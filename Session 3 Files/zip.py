# Let's make two sample lists
nums = [1, 2, 3]
fruits = ['apple', 'banana', 'coconut']

# You can iterate over both at once using zip
for num, fruit in zip(nums, fruits):
    print(num)
    print(fruit)
print()

# This has no limit on the amount of lists
vegetables = ['asparagus', 'broccoli', 'carrot']

for num, fruit, vegetable in zip(nums, fruits, vegetables):
    print(num)
    print(fruit)
    print(vegetable)
print()

# However, it will stop iterating at the end of the shortest list
nums = [1, 2]

# This will stop at 2, 'banana'
for num, fruit in zip(nums, fruits):
    print(num)
    print(fruit)