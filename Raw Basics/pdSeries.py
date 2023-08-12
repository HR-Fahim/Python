import pandas as pd  # Importing the pandas library

# Creating a pandas Series object called certificates_earned
# The Series contains the number of certificates earned by individuals
# The values are [8, 2, 5, 6]
# The index is ['Tom', 'Kris', 'Ahmad', 'Beau']
certificates_earned = pd.Series(
    [8, 2, 5, 6],
    index=['Tom', 'Kris', 'Ahmad', 'Beau']
)

# Printing the certificates_earned Series
print(certificates_earned)

# Printing a subset of the certificates_earned Series
# Only the values that are greater than 5 are printed
print(certificates_earned[certificates_earned > 5])
