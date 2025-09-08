import numpy as np
import pandas as pd

data = {
    'Date': pd.date_range('2023-01-01', periods=20),
    'Product': ['A', 'B', 'C', 'D'] * 5,
    'Region': ['East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West',
               'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
    'Sales': np.random.randint(100, 1000, 20),
    'Units': np.random.randint(10, 100, 20),
    'Rep': ['John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary',
            'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice']
}
df=pd.DataFrame(data)
# print(df)           
# #is mein region dikh raha hoga east west north south
## mein chata hoon 0 sy ly kr 19 tak jo index hai vo convert ho jaye east west north south mein saat mein jo product hai columns bn jaye 

pivot1=(pd.pivot_table(df,values='Sales',index='Region',columns='Product',aggfunc='median'))
# print(pivot1)
# aggfunc is by default mean
# use case in cluster heat mapd
# if you want to use your values,your columns and your index 
# you can use pivot table

pivot2=pd.pivot_table(df,values=['Sales','Units'],index='Region',columns='Product',aggfunc='sum',fill_value=0)
# print(pivot2)
# values must be numeric

            #  Cross Tabs
# cross tab is used to compute a simple cross tabulation of two (or more) factors.
crosstab1=pd.crosstab(df['Region'],df['Product'])
print(crosstab1)
# it will give you frequency table
# it will count how many times east is there with product A
