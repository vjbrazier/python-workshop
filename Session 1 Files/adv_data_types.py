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