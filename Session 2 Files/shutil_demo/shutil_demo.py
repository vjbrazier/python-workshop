# First, import the library
import shutil
from pathlib import Path

# Copy a file
shutil.copy('example.txt', 'example_copy.txt')

# You can also copy it into a folder
example_folder = Path('example_folder')
shutil.copy('example.txt', example_folder / 'example_copy.txt')

# You can copy an entire tree and its contents
shutil.copytree('nested', 'nested_backup')

# You can use dirs_exist_ok=True to make it append to a tree if it exists
shutil.copytree('example_folder', 'nested_backup', dirs_exist_ok=True)

# You can move a file
shutil.move('example2.txt', 'copies')

# This is also used to rename. This will overwrite files, be careful
shutil.move('example3.txt', 'different_example.txt')

# You can also delete an entire directory
pause = input('Press enter to delete the nested_backup folder:')
shutil.rmtree('nested_backup')