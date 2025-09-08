import pandas as pd
import numpy as np
df1=pd.DataFrame({
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3'],
    'C':['C0','C1','C2','C3'],
})
df2=pd.DataFrame({
    'A':['A3','A4','A5'],
    'B':['B3','B4','B5'],
    'C':['C3','C4','C5'],
})
# print(df1)
# print(df2)
print(pd.concat([df1,df2]))##default axis=0
#common columns to bilkul common rahaye gyein ,jo pahly likha vo upar hoga 2sra neechay
print(pd.concat([df1,df2],axis=1))##columns ke hisaab se concatenate
# agr saat mein jorna hai
