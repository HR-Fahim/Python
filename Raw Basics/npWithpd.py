import pandas as pd  # Importing the pandas library for data manipulation
import numpy as np  # Importing the numpy library for numerical operations

# Creating a pandas Series object with some values
s = pd.Series(['a', 3, np.nan, 1, np.nan])

# Checking which values in the Series are not null and then counting them
count_not_null = s.notnull().sum()

# Printing the count of non-null values in the Series
print(count_not_null)
