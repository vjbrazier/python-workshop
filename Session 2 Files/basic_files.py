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