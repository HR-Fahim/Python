# Creating a dictionary
student = {
    'name': 'John',
    'age': 22,
    'courses': ['Math', 'Science']
}

# Accessing values
print(student['name'])  # Output: John

# Adding/Modifying values
student['age'] = 23

# Removing key-value pairs
del student['courses']

# Iterating through a dictionary
for key, value in student.items():
    print(key, value)
