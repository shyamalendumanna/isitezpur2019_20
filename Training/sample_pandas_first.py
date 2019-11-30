# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:18:43 2019

@author: gupta
"""

import pandas as pd
import numpy as np


s1 = pd.Series([1,2,3])
s2 = pd.Series([1.,2.,3.])

s3 = pd.Series([1.,2.,3.], index=['a','b','c'])
s4 = pd.Series([1,2,3,4], index=['a','b','c','d'])

table1 = np.zeros((4,4))
#print(table1)

data = {1 : s1,
        2 : s2}

data2 = {"one" : s1,
         "two" : s2}

data3 = { "one" : s3,
         "two": s4}

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

df4 = pd.DataFrame(data=table1)

print(df2)
print(df3)
print(df4)

names = ['Bob', "Ram", "Raj", "Hara", "Geeta"]
counts = [ 968, 155, 77, 578, 973 ]


print(names100, vals100)

df_data = list(zip(names, counts))
#print(df_data)

pd1 = pd.DataFrame(data=df_data, columns=['name', 'counts'])
#print(pd1)
#print(pd1.name.dtype, pd1.counts.dtype)

df_data2 = list(zip(names100, vals100))

names100 = [ "value" + str(n) for n in range(100)]
print(names100)
vals100 = [ np.random.randint(2000) for n in range(100)]
pd2 = pd.DataFrame(data=df_data2, columns = ["name", "value"])
print(pd2)
print(pd2.index)
print(pd2.tail())
print(pd2.head())
print(pd2.head(3))
print(pd2.name)
print(pd2.value)
print(pd2.columns)
print(pd2.head())
max_value = pd2['value'].max()
print(max_value)
output = pd2["name"][ pd2["value"] == pd2["value"].max()]

#output2 = pd2["name"][ pd2["name"][-1] == "5"]
output2 = pd2["name"][pd2.name.str.endswith("5")]

print("-"*100)
print(output2)
#print(output)
#print(pd2)
#print("-"*100)
#print("output\n",pd2.loc[70])

