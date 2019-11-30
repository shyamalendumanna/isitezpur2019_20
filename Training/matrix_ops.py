# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 11:15:01 2019

@author: gupta
"""

import numpy as np

def matrix():
    a = np.matrix('1 2 3 4; 3 4 5 6; 10 22 1 44')
    b = np.matrix([[1, 2], [3, "4"]])
    
    print(a, a.dtype, type(a))
    print(b, b.dtype, type(b))

def add(m1, m2):
    print(m1, "= is m1")
    print(m2, "= is m2")
    _sum = np.add(m1,m2)
    print(_sum, "= is sum of given \n",_sum.dtype, type(_sum))
    return _sum    

def multiply(m,n):
    return np.multiply(m,n)
#multiply = lambda m,n: np.multiply(m,n)

def dot(m,n):
    return np.dot(m,n)

def get_transpose(A):
    return A.T



    
if __name__ == "__main__":
    m1 = np.array([[1,2],[10,20]])
    m2 = np.array([[11,12],[9,8]])
    m3 = np.matrix('1 2 3 4; 3 4 5 6; 10 22 1 44')
    m4 = np.array([[3, 4 ,5 ,6],[10, 22 ,1, 44], [99,2,4,1]])

    m5 = np.array([[1,2],
                   [1,2]])
    
    m6 = np.array([[5,6],
                   [3,4]])

    multiply_output = multiply(m5,m6)
    #matrix()
    #sum_matrix = add(m1, m2)
    #sum_matrix2 = add(m3, m4)
    out = dot(m5,m6)
    print(multiply_output, multiply_output.dtype, type(multiply_output))
    
    print(out, "= dot function output \n",out.dtype, type(out))
    
    print(m6,"\nTranspose of above matrix is ---> \n", get_transpose(m6))
    print("matrix is \n",m6)    
    #print("\n each element square root , matrix is --> \n" ,np.sqrt(m6))
    print(np.sum(m6, axis=0)) 
    
    print(np.sum(m6, axis=1)) 
    
    