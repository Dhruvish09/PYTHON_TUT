import numpy as np
import pandas as pd

d={'name':['Alice','Bella','Sara','Emily'],
   'number':[18,20,22,24],
   'score':[85,87,83,89]}

print("Writting csv file:")
df=pd.DataFrame(d)
df.to_csv('test2.csv',index=False)
pd.read_csv('test2.csv')
print(df)
print("-------------------------")

print("Reading and Writting Excel Files:")
print(pd.read_excel('p.xlsx',sheet_name='sheet1'))