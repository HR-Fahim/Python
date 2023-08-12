import pandas as pd  # Importing the pandas library for data manipulation
import numpy as np  # Importing the numpy library for numerical operations

# Creating a pandas Series with missing values
s = pd.Series([np.nan, 1, 2, np.nan, 3])

# Filling the missing values using forward fill method
s = s.fillna(method='ffill')

# Printing the resulting Series
print(s)
