import numpy as np
import pandas as pd

labels=['a','b','c']
my_list=[10,20,30]
d={1:10,2:20,3:30}

# print(pd.Series(my_list))
# # 0    10
# # 1    20
# # 2    30  series vertically nazar aye gi indexpoint(mean label),datapoints

# # dtype: int64

#  #custom labels
# print(pd.Series(my_list,index=labels))
#    #  output
# # a    10
# # b    20
# # c    30
# # dtype: int64

# print(pd.Series(arr))
# # 0    10
# # 1    20
# # 2    30
# # dtype: int64
# print(pd.Series(arr,index=labels))
# # a    10
# # b    20
# # c    30
# # dtype: int64

# # series one dimensional hota hai

# print(pd.Series(d))

# To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day3"])

# print(myvar)

print(pd.Series(my_list,[1,5,6]))



                   # summary
# SERIES : 
# A Series is a one-dimensioanl labeled array capable
# of holding any data type.The axis labels are collectively called index.  