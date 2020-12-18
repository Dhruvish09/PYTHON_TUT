print("Merging , Joining and Concatenating")

import numpy as np
import pandas as pd

df1=pd.DataFrame({'A':['A0','A1','A2','A3'],
                  'B':['B0','B1','B2','B3'],
                  'C':['C0','C1','C2','C3'],
                  'D':['D0','D1','D2','D3']},
                  index=[0,1,2,3])

df2=pd.DataFrame({'A':['A4','A5','A6','A7'],
                  'B':['B4','B5','B6','B7'],
                  'C':['C4','C5','C6','C7'],
                  'D':['D4','D5','D6','D7']},
                  index=[4,5,6,7])

df3=pd.DataFrame({'A':['A8','A9','A10','A11'],
                  'B':['B8','B9','B10','B11'],
                  'C':['C8','C9','C10','C11'],
                  'D':['D8','D9','D10','D11']},
                  index=[8,9,10,11])

print(df1)
print(df2)
print(df3)

print("--------------------------------------")
print("concatinate data")
print(pd.concat([df1,df2,df3]))

print("--------------------------------------")
print("concatinate data with axis")
print(pd.concat([df1,df2,df3],axis=1))

df4=pd.DataFrame({'Key':['K0','K1','K2','K3'],
                  'A':['A0','A1','A2','A3'],
                  'B':['B0','B1','B2','B3']})

df5=pd.DataFrame({'Key':['K0','K1','K2','K3'],
                  'C':['C0','C1','C2','C3'],
                  'D':['D0','D1','D2','D3']})


print("----------------------------------------")
print("Merge DataFrame")
print(pd.merge(df4,df5,how='inner',on='Key'))



df6=pd.DataFrame({'A':['A0','A1','A2','A3'],
                  'B':['B0','B1','B2','B3']},
                  index=['K0','K1','K2','K3'])

df7=pd.DataFrame({'Key':['K0','K1','K2','K3'],
                  'C':['C0','C1','C2','C3']},
                  index=['K0','K1','K2','K3'])
print("----------------------------------------")
print("Joins Data Frame")
print(df6.join(df7))
