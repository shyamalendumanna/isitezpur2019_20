# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:40:14 2019

@author: gupta
"""

import numpy as np


def test1():
    v1 = np.array([ 1,2,3,4 ])
    print(v1, type(v1))
    v2 = np.array([[1,2], [3,4]])
    
    small_l1 = [1,2, "hello"]
    small_l2 = [3,4,5]
    l1 = [small_l1, small_l2]
    v3 = np.array([[1,2], small_l2])

    v4 = np.array(l1)
    
    print(v2, "size=",v2.size, "shape=",v2.shape,  "data type", v2.dtype)
    print(v3, "size=",v3.size, "shape=",v3.shape,  "data type", v3.dtype)
    print(v4, "size=",v4.size, "shape=",v4.shape,  "data type", v4.dtype)
    
    

    
if __name__ == "__main__":
    test1()    