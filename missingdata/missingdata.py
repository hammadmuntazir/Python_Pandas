import numpy as np
import pandas as pd

data={
    'A':[1,2,np.nan,4,5]
    ,'B':[np.nan,2,3,4,5],
    'C':[1,2,3,np.nan,np.nan],
    'D':[1,np.nan,np.nan,np.nan,5]
}
df=pd.DataFrame(data)
print(df)
#     A    B    C    D
# 0  1.0  NaN  1.0  1.0
# 1  2.0  2.0  2.0  NaN
# 2  NaN  3.0  3.0  NaN
# 3  4.0  4.0  NaN  NaN
# 4  5.0  5.0  NaN  5.

# isi Nan ko null value khety inhy ab agr find krna ha to
# print(df.isna())
    #    A      B      C      D
# 0  False   True  False  False
# 1  False  False  False   True
# 2   True  False  False   True
# 3  False  False   True   True
# 4  False  False   True  False
print(df.isna().sum())
# is sy humy pata chl jata ha k konse column me kitny null value ha
print(df.isna().any())# dekhny ky liay k konse column me koi na koi null value ha
