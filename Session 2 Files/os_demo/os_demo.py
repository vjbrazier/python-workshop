# First, import the library
import os

# Getting the current directory
current_dir = os.getcwd()
print(current_dir)
print()

# List files in directory
print(os.listdir('.')) # This will use the current_dir
print()
print(os.listdir('data'))
print()

# Making directories
os.mkdir('example_dir')
os.makedirs('dir1/dir2/dir3')

# You can use exist_ok to avoid errors
os.makedirs('dir1/dir2/dir3', exist_ok=True)
# This would error without it, due to it already existing

# Checking existence
if os.path.exists('data'):
    print('Data folder present!')
else:
    print('No data folder.')
print()

# OS name
print('Your operating system is:', os.name)
print()

# Delete a file
pause = input('Press enter to delete the file')
os.remove('deleteme.txt')