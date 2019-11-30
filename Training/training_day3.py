# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:03:51 2019

# https://docs.python.org/3/library/random.html

@author: gupta
"""

import random

#from random import *
#from random import random, randint, randrange

#giving a random value between 0 to 1
rvalue = random.random() 

print(rvalue, int(rvalue*100))

rvalue2 = random.randrange(0,100)
print("value with randrange",rvalue2)
rvalue3 = random.randrange(0,100)
print("value with randrange",rvalue3)
rvalue4 = random.randrange(0,100)
print("value with randrange",rvalue4)

