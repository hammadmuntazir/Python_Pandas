import pandas as pd
import numpy as np

df1=pd.DataFrame({
    'A':[1,2,3,4,5],
    'B':[10,20,30,40,50],
    'C':[100,200,300,400,500]

})
# print(df1)
##    A   B    C
## 0  1  10  100
## 1  2  20  200
## 2  3  30  300
## 3  4  40  400
## 4  5  50  500

 #     # shape btanay ky lie
## shape attribute hai it is not a method
# print(df1.shape) 
##(5,3)5 rows and 3 columns
       #columns
# print(df1.columns)
##Index(['A', 'B', 'C'], dtype='object')

 #     #info method puri information of data frame tell me by non null and null values
print(df1.info())
## <class 'pandas.core.frame.DataFrame'>
## RangeIndex: 5 entries, 0 to 4
## Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
## ---  ------  --------------  -----
##  0   A       5 non-null      int64
##  1   B       5 non-null      int64
##  2   C       5 non-null      int64
## dtypes: int64(3)
## memory usage: 252.0 bytes
## None

      #describe method
print(df1.describe())


#               A          B           C
# count  5.000000   5.000000    5.000000
# mean   3.000000  30.000000  300.000000
# std    1.581139  15.811388  158.113883
# min    1.000000  10.000000  100.000000
# 25%    2.000000  20.000000  200.000000
# 50%    3.000000  30.000000  300.000000
# 75%    4.000000  40.000000  400.000000
# max    5.000000  50.000000  500.000000

   #kia isy column mein kuch add krskty ho broadcasting ka use krky
print(df1['A']+10) 
# A ki sub values mein 10 add krdyga
## 0    11
## 1    12  
## 2    13
## 3    14
## 4    15
## Name: A, dtype: int64
print(df1['B']*2)
# B ki sub values mein 2 multiply krdyga

       #DataFrame applying function
def square(x):
    return x**2
print(df1.apply(square))
print(df1['A'].apply(square))
# for applying changes in real data frame
df1['A']=df1['A'].apply(square)
print(df1)
# can also create new column
df1['D']=df1['B'].apply(square)

# can also use lambda function
df1['E']=df1['C'].apply(lambda x:x+5)
print(df1)