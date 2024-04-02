import pandas as pd  # Importing the pandas library

# Creating a DataFrame using the pd.DataFrame() function
# The DataFrame consists of two columns: 'Certificates' and 'Time (in months)'
# The values in 'Certificates' column are [8, 2, 5, 6]
# The values in 'Time (in months)' column are [16, 5, 9, 12]
certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12]
})

# Assigning custom index labels to the DataFrame
# The index labels are ['Tom', 'Kris', 'Ahmad', 'Beau']
certificates_earned.index = ['Tom', 'Kris', 'Ahmad', 'Beau']

# Printing the row with index label 'Ahmad' using the iloc[] function
print(certificates_earned.iloc[2])
