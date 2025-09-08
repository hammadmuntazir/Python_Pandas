import numpy as np
import pandas as pd
data={
    'Category':['A','B','A','C','B','A','C','C'],
    'Store':['X','Y','X','Y','X','Y','X','Y'],
    'Sales':[100,200,150,300,250,200,350,400],
    'Quantity':[1,2,1,3,2,2,3,4],
    'Date':pd.date_range(start='2023-01-01', periods=8)
}
# subko aggregate krky result nikalna
df=pd.DataFrame(data)
# print(df['Sales'].sum())
# mean  median max min count std # in sub ko use krskty hain
print(df['Sales'].agg(['sum','mean','max','min','count','std']))
# group by krky aggregate krna