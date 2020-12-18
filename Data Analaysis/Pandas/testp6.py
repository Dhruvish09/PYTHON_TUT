# .unique()
# .nunique()
# .value_counts()
# # .apply()
# .sort_values()
# .isnull()
# .pivot_tables()

import numpy as np
import pandas as pd

df=pd.DataFrame({'col1':[1,2,3,4],
                 'col2':[43,45,45,76],
                 'col3':['dp','diplo','BE','EXCELENCE']})
print(df)

print("----------------------------")

print("display unique value,no")
un=df['col2'].unique()
print(un)
print("----------------------------")
nun=df['col2'].nunique()
print(nun)
print("----------------------------")
count=df['col2'].value_counts()
print(count)

print("---------------------------------")
print("Apply method")
def multiply2(x):
    return x*2

print(df['col1'].apply(multiply2))
print(df['col3'].apply(len))

print("------------------------------------")


print(df.sort_values('col2'))
print(df.isnull())

d={'A':['Red','Red','Red','Green','Green','Green'],
   'B':['One','One','One','Two','Two','Two'],
   'C':['X','Y','X','Y','X','Y'],
   'D':[1,3,5,2,4,1]}
df=pd.DataFrame(df)
print(df)

print(df.pivot_table(values='D',index=['A','B'],columns='C'))
# print(df2)