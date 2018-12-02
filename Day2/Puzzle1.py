# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 11:05:09 2018

@author: Joe
"""

# Puzzle 1
## Get the checksum



## Data import


#%% dictonary link for individual letter
alphanum = {'a':1,
            'b':2,
            'c':3,
            'd':4,
            'e':5,
            'f':6,
            'g':7,
            'h':8,
            'i':9,
            'j':10,
            'k':11,
            'l':12,
            'm':13,
            'n':14,
            'o':15,
            'p':16,
            'q':17,
            'r':18,
            's':19,
            't':20,
            'u':21,
            'v':22,
            'w':23,
            'x':24,
            'y':25,
            'z':26}

#%% function def for individual string
def stringcheck(string):
    string_out = zeros(1,26)
    for s in string:
        string_out[alphanum[s] - 1] +=  1
    return string_out
        
#%% Function def or checksum
def checksum(entry):
    doubles = 0
    trebles = 0
    for i in entry:
        if 3 in stringcheck(i):
            trebles += 1
        if 2 in stringcheck(i):
            doubles += 1
    return doubles * trebles

#%% testing
#testblock = inputtxt[:3]
print(checksum(inputtxt))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        