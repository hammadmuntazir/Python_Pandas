# dropna 
# fillna
# isna check krny ky liye
import pandas as pd
import numpy as np
data={
    'A':[1,2,np.nan,4,5]
    ,'B':[np.nan,2,3,4,5],
    'C':[1,2,3,np.nan,np.nan],
    'D':[1,np.nan,np.nan,np.nan,5]
}
df=pd.DataFrame(data)
print(df)
values={'A':0,'B':100,'C':300,'D':400}
print(df.fillna(value=values))
# fillna aur selection column wise hota hai
# dropna row wise hota hai