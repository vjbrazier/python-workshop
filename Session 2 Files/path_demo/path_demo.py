import json
from pathlib import Path # To use the class Path, we need to import it

# If you write the path like this, you are hard-coding it
user_data_file = 'data\\users.json'

# You instead create a Path object by building the path manually using /
path_user_data_file = Path('data') / 'users.json'

# The same open is used as before
def read_file(file_path):
    with open(file_path, 'r') as file:
        users = json.load(file)
    
    for user in users:
        if user.get('isAdult'):
            print(user)

# Both will execute fine on Windows. How about Linux/MacOS?
try:
    read_file(user_data_file)
except Exception as e:
    print(f'An exception occurred: {e}')

try:
    read_file(path_user_data_file)
except Exception as e:
    print(f'An exception occurred: {e}')