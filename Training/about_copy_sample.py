# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:56:55 2019

@author: gupta
"""
import copy



l1 = [1,2,3,[100,200]]
l2 = l1 # points to same
lc2 = copy.copy(l1)

l3 = l1[:] # copies all values
lc2 = copy.deepcopy(l1)

l2[0] = [15,20]
l3[0] = [20,30]
print(l1[3][0])
l3[3][0] = 1
#print(l2, id(l2))
#print(l3, id(l3))
print(l1, id(l1))
print(l3, id(l3))


l1 = [1,2,3,(100,200)]

