# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:56:42 2019

@author: gupta
"""

#https://www.python.org/dev/peps/pep-0008/#indentation
#for coding guidelines

afile = "some_file.txt"

def get_line1(afile)
    with open("some_file.txt") as fp:
        for line in fp.readlines():
            print(line)

def get_line2(afile):
        line = fp.readline()
        while(line):
            line = fp.readline()
            return line
                
def get_line3(afile):
        line = fp.readline()
        while(line):
            line = fp.readline()
            yield line
        




