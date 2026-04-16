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