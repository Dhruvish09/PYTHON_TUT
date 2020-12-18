import numpy as np
import pandas as pd

print("define with pandas")
my_data=[12,23,45,67]
print(pd.Series(my_data))
print("-------------------------")

labels=["a","b","c","d"]
print(pd.Series(my_data,labels))

print("--------------------------")
print("define panda with numpy")
ar=np.array(my_data)
print(ar)
print(pd.Series(ar))
print(pd.Series(ar,labels))

print("--------------------------")
print("define dictonery:")
d={"name":"Dhruvish",
   "age":21,
   "weight":70}
print(pd.Series(d))


print("--------------------------")
print("Grabe info from series")
sr1=pd.Series([1,2,3,4],["a","b","c","d"])
sr2=pd.Series([1,2,3,4],["w","b","x","d"])
print(sr1)
print(sr2)
print(sr1["a"])
print(sr2["d"])


print("add two str1+str2")
print(sr1+sr2)
