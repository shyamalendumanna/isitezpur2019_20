# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:51:09 2019

@author: gupta
"""

import pandas as pd
import numpy as np

DATA_SIZE = 10

names = ['Bob', "Ram", "Raj", "Hara", "Geeta"]
counts = [ 968, 155, 77, 578, 973 ]

vals100 = [ np.random.randint(2000) for n in range(DATA_SIZE)]
names100 = [ "value" + str(n) for n in range(DATA_SIZE)]
df_data2 = list(zip(names100, vals100))
df1 = pd.DataFrame(data=df_data2, columns = ["name", "value"])

print(df1.head())
df1.to_csv("sample_dataset.csv",index=False, header=False)
df2 = pd.read_csv("sample_dataset.csv", names=['Names', 'nums'])
print(df2.head())
print(df2.dtypes)
print(df2.Names.dtype)
print(df2.columns)
print(df2.nums)
print(df2.values)
print(df2.head())
df2["newcol"] = df2["nums"] * 2
print(df2.head())

print(df2["newcol"].max())
newcolvalues = df2['newcol'].unique()
print(len(newcolvalues))
print(df2['Names'].describe())

data2 = [5*x for x in range(DATA_SIZE)]

print(data2)
df3 = pd.DataFrame(data2)
print(df3.head())
print(df2.head())
df2["newcol"] = df2["newcol"] - 111
print(df2.head())
del df2['newcol']
print(df2.head())
indexing = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df2.index = indexing
print(df2.head())
print(df2.loc['a'])
df2.index = [x for x in range(DATA_SIZE)]
print(df2.head())
print(df2[1:3])
df2.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(df2['b':'g'])
old_cols = df2.columns
df2.columns = ["col1","col2"]
print(df2.head())
print(old_cols)
df2.columns = old_cols
print(df2.head(1))
print(df2.loc['b','nums'])
#print(df2.query('nums' < 200))
print(df2.nums.mean())