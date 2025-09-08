           # Discovering Duplicates
# Duplicate rows are rows that have been registered more than one time.
# By taking a look at our test data set, we can assume that row 11 and 12 are duplicates.

# To discover duplicates, we can use the duplicated() method.

# The duplicated() method returns a Boolean values for each row:
import pandas as pd
df=pd.read_csv('data.csv')
print(df.duplicated())
        #   Removing Duplicates
# To remove duplicates, use the drop_duplicates() method.
df.drop_duplicates(inplace=True)
print(df)