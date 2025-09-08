import pandas as pd
import numpy as np

df1=pd.DataFrame({
    'name':['Alice','Bob','Charlie']
   },index=[1,2,3])
# Second DataFrame
df2=pd.DataFrame({
    'score':[85,90,75]
},index=[2,3,4])
# print(df1)
# print(df2)

# Joining DataFrames on index
print(df1.join(df2,how='outer')) #by default how='left' to ignore index use ignore_index=True
# print(pd.concat([df1,df2],ignore
