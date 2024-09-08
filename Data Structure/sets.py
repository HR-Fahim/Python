# Creating a set
my_set = {1, 2, 3, 4}

# Adding elements
my_set.add(5)

# Removing elements
my_set.remove(2)

# Checking membership
print(3 in my_set)  # Output: True

# Set operations
another_set = {3, 4, 5, 6}
union_set = my_set.union(another_set)
intersection_set = my_set.intersection(another_set)

print(union_set)  # Output: {1, 3, 4, 5, 6}
print(intersection_set)  # Output: {3, 4, 5}
