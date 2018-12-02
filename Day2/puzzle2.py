# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 11:43:47 2018

@author: Joe
"""

# Puzzle 2
## get the common letters between the entries with only one letter different

#%% defining the unlikeness metric
def unlikeness(string1, string2):
    unlikeness = 0
    for i,j in zip(string1, string2):
        if i != j:
            unlikeness += 1
    return(unlikeness)
    

#%% testing
print(unlikeness('fghij','fguij'))

#%% defining the function to return only the common letters between two strings
def likeletters(string1, string2):
    likeletters = ''
    for i,j in zip(string1, string2):
        if i == j:
            likeletters += i
    return likeletters
#%% testing
print(likeletters('fghij','fguij'))
    
#%% segment to iterate over all combinations of elements in the input
testblock = inputtxt
for i in range(len(testblock)):
    for j in range(i+1):
        if unlikeness(testblock[i], testblock[j]) == 1:
            print(likeletters(testblock[i], testblock[j]))
    