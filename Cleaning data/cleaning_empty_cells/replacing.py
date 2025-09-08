#        #Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.

# This way you do not have to delete entire rows just because of some empty cells.

# The fillna() method allows us to replace empty cells with a value:
import pandas as pd
df=pd.read_csv('data.csv')
# print(df.info())
# #         OUTPUT
# #<class 'pandas.core.frame.DataFrame'>
# #RangeIndex: 32 entries, 0 to 31
# #Data columns (total 5 columns):
#  #   Column    Non-Null Count  Dtype
## ---  ------    --------------  -----
##  0   Duration  32 non-null     int64
##  1   Date      31 non-null     object
##  2   Pulse     32 non-null     int64
##  3   Maxpulse  32 non-null     int64
##  4   Calories  30 non-null     float64
## dtypes: float64(1), int64(3), object(1)
## memory usage: 1.4+ KB
## None

# df.fillna(130,inplace=True)
# print(df)
# print(df.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 32 entries, 0 to 31
# Data columns (total 5 columns):
#  #   Column    Non-Null Count  Dtype
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  32 non-null     int64
#  1   Date      32 non-null     object
#  2   Pulse     32 non-null     int64
#  3   Maxpulse  32 non-null     int64
#  4   Calories  32 non-null     float64
# dtypes: float64(1), int64(3), object(1)
# memory usage: 1.4+ KB
# None

        #  Replace Only For Specified Columns
# The example above replaces all empty cells in the whole Data Frame.

# To only replace empty values for one column, specify the column name for the DataFrame:
# Example:
# Replace NULL values in the "Calories" columns with the number 130:

# print(df.to_string())
df.fillna({'Calories':130},inplace=True)
# print(df.to_string())

#This operation inserts 130 in empty cells in the "Calories" column (row 18 and 28).



       # Replace Using Mean, Median, or Mode 
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

# df2=pd.read_csv('data.csv')
# x=df2['Calories'].mean()
# print(x)
# df2.fillna({'Calories':x},inplace=True)
# print(df2)

## Mean = the average value (the sum of all values divided by number of values).

## Median = the value in the middle, after you have sorted all values ascending.

x = df["Calories"].median()

df.fillna({"Calories": x}, inplace=True)
# print(df)
## Mode = the value that appears most frequently.
x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace=True)
print(df)