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