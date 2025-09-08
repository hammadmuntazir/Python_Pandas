            # Empty Cells
# Empty cells can potentially give you a wrong result when you analyze data.

  # Solution 1
#-> removing row containing empty cells
# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

import pandas as pd
df=pd.read_csv('data.csv')
newdf=df.dropna()# will drop empty rows
# print(newdf.info())
# print(df.info())

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
# If you want to change the original DataFrame, use the inplace = True argument:


df.dropna(inplace = True)

# print(df.to_string())

# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

