import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
print(hier_index)

print("--------------------------------")
print("multi index and index hierarchy")
hier_index=pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

print("--------------------------------")
print("multi index data Frame")
df=pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)

print("--------------------------------")
print("call data from multi level index")
df_loc=df.loc['G1'].loc[1]['A']
print(df_loc)

print("--------------------------------")
print("add name of index")
df.index.names=['Groups','Num']
print(df)


print("---------------------------------")
print("Cross section of index")
print(df.xs('G1'))

print("---------------------------------")
print("Cross selection for perticular of index")
df_xs=df.xs(1,level='Num')
print(df_xs)

