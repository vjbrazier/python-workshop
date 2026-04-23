import json
from pathlib import Path

# Enumerate counts alongside a list
fruits = ['apple', 'banana', 'coconut']

# It uses a lazy iterator, making it faster than managing your own index variable
for index, fruit in enumerate(fruits):
    print(index)
    print(fruit)
print()

# This seems pointless, so here's a use case
friends_data = Path('data') / 'friends.json'

with open(friends_data, 'r') as f:
    friends = json.load(f)

# You can also add a start parameter (the default is 0)
for index, friend in enumerate(friends, start=1):
    print(f'{index}. {friend.get('name')}')
print()

try:
    choice = int(input('Who\'s email do you need? (enter their number) '))
    print(friends[choice - 1].get('email'))
except ValueError:
    print('Please input a number.')