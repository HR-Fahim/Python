import pandas as pd  # Importing the pandas library

# Creating a DataFrame named 'certificates_earned' with two columns: 'Certificates' and 'Time (in months)'
certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],  # Values for the 'Certificates' column
    'Time (in months)': [16, 5, 9, 12]  # Values for the 'Time (in months)' column
})

names = ['Tom', 'Kris', 'Ahmad', 'Beau']  # Creating a list of names

certificates_earned.index = names  # Setting the index of 'certificates_earned' DataFrame to the 'names' list

# Creating a Series named 'longest_streak' with values and index based on the 'names' list
longest_streak = pd.Series([13, 11, 9, 7], index=names)

# Adding a new column 'Longest streak' to the 'certificates_earned' DataFrame with values from 'longest_streak' Series
certificates_earned['Longest streak'] = longest_streak

print(certificates_earned)  # Printing the 'certificates_earned' DataFrame
