#methods:
# .dropna
# .fillna

import numpy as np
import pandas as pd

d={'A':[1,2,np.nan],'B':[3,np.nan,np.nan],'C':[4,5,6]}
df=pd.DataFrame(d)
print(df)

print("---------------------------")
print("Drope method")
print(df.dropna)

print("---------------------------")
print("Drope method for perticular axis")
print(df.dropna(axis=1))

print("---------------------------")
print("drop null value as define here thresh=2")
print(df.dropna(thresh=2))

print("---------------------------")
print("drop null value with define axis")
print(df.dropna(axis=1,thresh=2))

print("---------------------------")
print("replace null value as mean")
df_rep=df['A'].fillna(value=df['A'].mean())
print(df_rep)
