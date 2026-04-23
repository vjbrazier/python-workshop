import json
from pathlib import Path

# Comprehension is not limited to 1D arrays
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flat = [num for row in matrix for num in row]
print(flat)
print()

# You can still attach conditions
flat = [num for row in matrix for num in row if num % 2 == 0]
print(flat)
print()

# You can perform it on data read from a file!
friend_data_path = Path('data') / 'friends.json'

with open(friend_data_path, 'r') as f:
    friends = json.load(f)

age_mapping = {friend.get('name'): friend.get('age') for friend in friends}
print(age_mapping)
print()

# You can make nested dictionaries as well
students = ['alice', 'bob', 'charlie']
grades = [95, 60, 75]
report_cards = {
    student.capitalize(): {
        'name_length': len(student),
        'uppercase': student.upper(),
        'grade': grade,
        'passing': True if grade > 60 else False
    }
    for student, grade in zip(students, grades)
}

print(report_cards)