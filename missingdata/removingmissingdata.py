import pandas as pd
import numpy as np
data={
    'A':[1,2,np.nan,4,5
         ]
    ,'B':[np.nan,2,3,4,5],
    'C':[1,2,3,np.nan,np.nan],
    'D':[1,2,np.nan,np.nan,5]
}
df=pd.DataFrame(data)
print(df)
print(df.dropna(inplace=True))# ye puri row ko drop kr deta ha jahan null value ho
print(df.dropna(thresh=2))# ye un rows ko drop krta ha jahan 2 se kam non null value ho
# rows mein non none value utni honi chyiea jtna thresh mein likh rahye hain
