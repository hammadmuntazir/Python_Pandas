import numpy as np
import pandas as pd

data={
    'Category':['A','B','A','C','B','A','C','C'],
    'Store':['X','Y','X','Y','X','Y','X','Y'],
    'Sales':[100,200,150,300,250,200,350,400],
    'Quantity':[1,2,1,3,2,2,3,4],
    'Date':pd.date_range(start='2023-01-01', periods=8)
}
df=pd.DataFrame(data)
# print(df)
## Group by Category and Calculate sum of sales
cat=df.groupby('Category')
for i,v in cat:
    print(i)
    print(v)
# sales ka sum chyiea cateogry mein sy
print(df.groupby('Category')['Sales'].sum())
## Group  by create object jisy ap khud sy dekh nai skty hain

## group by Store and calculate total sales 
cat=df.groupby('Store')['Sales'].sum()
print(cat)

## group by multiple columns
cat=df.groupby(['Category','Store'])['Sales'].sum()
print(cat) #group by qualititive ki base pr krty hain