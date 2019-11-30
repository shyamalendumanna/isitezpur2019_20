# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 13:21:36 2019

@author: gupta
"""

def otherdeco(fun1):
    def internal(*args):
        #do additional things
        fun1(*args)
        # do additional things
        
    return internal

def validate(actual_func):
    def decorateing(a,b,c):
        print(a,b,c)
        #if b == "hara":
        actual_func(a,b,c)
    return decorateing

@otherdeco
@validate
def connect_to_DB(ip, user, pwd):
    print("connecting database")


#connect_to_DB = validate(connect_to_DB)




if __name__ == "__main__":
    #t = validate(id) 
    #print(t)
    connect_to_DB("192.168.100.201", "hara", "welcome123")
    connect_to_DB("192.168.100.201", "raj", "welcome123")
    pass
    
    
    