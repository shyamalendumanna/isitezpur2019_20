# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:02:36 2019

@author: gupta
"""

import numpy as np

def test():
    print(range(10))
    print(list(range(10)))
    output = list(range(3, 10))
    print(output)
    
    #for i in range(3,10):
    #    output.append(i)

    m1 = np.arange(11, -(11+20), -2)
    
    p = np.arange(10)
    q = np.arange(9, -1, -1)
    
    md = np.array([p,q])
    md2 = np.array([np.arange(5), np.arange(5)])

    print(p)
    print(q)
    print(md)
    print(md2)
    #print(m1, m1.dtype, type(m1), m1.size, m1.shape)



if __name__ == "__main__":
    test()