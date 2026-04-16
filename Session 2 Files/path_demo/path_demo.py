import json
from pathlib import Path # To use the class Path, we need to import it

# You create a Path object by just inserting a path of either OS
user_data_file = 'data\\users.json'
path_user_data_file = Path(user_data_file)

def read_file(file_path):
    # The same function is used as before
    with open(file_path, 'r') as file:
        users = json.load(file)
    
    for user in users:
        if user.get('isAdult'):
            print(user)

# Both will execute fine on Windows. How about Linux?
try:
    read_file(user_data_file)
    read_file(path_user_data_file)
except Exception as e:
    print(f'An exception occurred: {e}')