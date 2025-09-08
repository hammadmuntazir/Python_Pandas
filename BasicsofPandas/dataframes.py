# ## A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

# import pandas as pd
# import numpy as np

# data={
#     'calories':[40,20,80],
#     'duration':[50,40,20]
# }
# df=pd.DataFrame(data)
# # print(df)

# ##    calories  duration
# ## 0        40        50
# ## 1        20        40
# ## 2        80        20

# # Pandas use the loc attribute to return one or more specified row(s)  loc=>locate rows
# # print(df.loc[[0,1]])

#       #output
# ## calories    40
# ##  duration    50

# # return row 0 and 1
# # print(df.loc[[0,1]])

# ##    calories  duration
# ## 0       420        50
# ## 1       380        40
           
#            #Named Indexes
# # With the index argument, you can name your own indexes.
# labels=['day1','day2','day3']
# df2=pd.DataFrame(data,index=labels)
# # print(df2)
# # print(df2.loc['day1'])

# ##       calories  duration
# ## day1        40        50
# ## day2        20        40
# ## day3        80        20


# # #If your data sets are stored in a file, Pandas can load them into a DataFrame.
# ## Load a comma separated file (CSV file) into a DataFrame:



# df2=pd.read_csv('data.csv')
# # print(df2)

# # The head() method returns the headers and a specified number of rows, starting from the top.
# #print(df2.head(5))
# ## Note: if the number of rows is not specified, the head() method will return the top 5 rows.

# # print(df2.tail()) 
# ## This will print last 5 rows

                            
#                    #Summary
#      # data Frames
# # Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# # Series is like a column, a DataFrame is the whole table.

#             #    Info About the Data
# # The DataFrames object has a method called info(), that gives you more information about the data set.

# print(df2.info())

#         #   OUTPUT
# #1# <class 'pandas.core.frame.DataFrame'> 
# # RangeIndex: 169 entries, 0 to 168     
# #2# Data columns (total 4 columns):       
# #  #   Column    Non-Null Count  Dtype  
# # ---  ------    --------------  -----  
# #  0   Duration  169 non-null    int64  
# #  1   Pulse     169 non-null    int64  
# #  2   Maxpulse  169 non-null    int64  
# #  3   Calories  164 non-null    float64
# # dtypes: float64(1), int64(3)
# # memory usage: 5.4 KB
# # None

# #1to2 The result tells us there are 169 rows and 4 columns:

# # rest of lines are telling s about number of rows,datatypes and null values

#               # Null Values
# # The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.

# # Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.

# # Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data, and you will learn more about that in the next chapters.

import numpy as  np
import pandas as pd

## creating a data Frame
# data_dictonary={
#     'Name':['John','Anna','Peter','Linda'],
#     'Age':[28,34,29,42],
#     'City':['New York','Paris','Berlin','London'],
#     'Salary':[65000,70000,62000,85000]
# }
# df2=pd.DataFrame(data_dictionary)
# print (df2)

data_list=[
    ['John',28,'New York',65000,],
     ['Anna',34,'Paris',70000],
    ['Peter',29,'Berlin',85000],
    ['Linda',42,'Linda',62000]
]
columns=['Name','Age','City','Salary']
df2=pd.DataFrame(data_list,columns=columns)
print(df2)
# print(df2['Name'])
# idr columns ky name kaam krty hain
# for targeting more than one column provide list  of list
# print(df2[['Name','Age']])
# Creating a new column
df2['Designation']=['Doctor','Engineer','Doctor','Engineer']
# print(df2)

# # For removing a column
# print(df2.drop('Designation',axis=1))#assy remove krky sirf aik coppy dekhata hai
# print(df2)
# df2.drop(['City','Salary'],axis=1 ,inplace=True)
# print(df2)
# print(df2.drop(0,axis=0))
print(df2.loc[[0,1]])

## index location
print(df2.iloc[1])

## Selecting sub sets of rows and column

# print(df2.loc[[0,1]][['Name','City']])
#   Name      City
# 0  John  New York
# 1  Anna     Paris

# Selecting name area from row 2 and 3
print(df2.loc[[2,3]][['Name','Age']])

# Condition based Selection
# if i only want to see those people whose age is greater than 30
# print(df2[df2['Age']>30])
#I only want to see those people whose age is greater than 30 and salary is greater than 65000
print(df2[(df2['Age']>30) & (df2['Salary']>60000)])