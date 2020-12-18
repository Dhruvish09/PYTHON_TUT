import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

df=pd.DataFrame(randn(5,4),["a","b","c","d","e"],["w","x","y","z"])
print(df)
print(df["w"])
print(df[["x","y"]])

print("---------------------------")
print("create new column:")
df["new"]=df["x"]+df["z"]
print(df)

print("----------------------------")
print("drop or delete column")
print(df.drop("new",axis=1,inplace=True))
print(df)

print("------------------------------")
print("selecting rows")
print(df.loc["c"])
print("selecting rows with index")
print(df.iloc[1])

print("------------------------")
print("selecting subsets of rows and columns")
print(df.loc["b","w"])
print(df.loc[["a","b"],["y","z"]])


print("----------------------------------")
print("boolean value:")
print(df>0)

print("----------------------------------")
print("boolean value for perticulat column:")
print(df["w"]>0)

print("----------------------------------")
print("print perticular with condition fullfil:")
d=df[df["z"]>0]
print(d)

print("----------------------------------")
print("print perticular rows-cols:")
d=df[df['z']>0][['x','y']]
print(d)

print("----------------------------------")
print("print perticular rows-cols:")
print(df[(df['y']>0) & (df['z']>1)])

print("-------------------------------------")
print("reset index value:")
print(df.reset_index())

print("-------------------------------------")
print("create new index value:")
new_index="R G B Y O".split()
print(new_index)

print("-------------------------------------")
print("create new index value:")
new_index="R G B Y O".split()
df['colors']=new_index
print(df)

print("-------------------------------------")
print("set index value:")
print(df.set_index('colors'))






