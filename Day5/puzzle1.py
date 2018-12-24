# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 14:39:08 2018

@author: j_osborne
"""

## Day 5 puzzle

## Head
###Summary
# if there are charaters nadjacent whicha re the same letter of a different case, then they are anhillated
### Libraries
import numpy as np
## Data in
## Preparation
indat = str(inputtxt)
s = indat
## Processing
#%%


#%%
refnew = 0
ref = -1
while refnew != ref:
    ref = len(s)
    for i in range(len(s)):
        try:
            if s[i] == s[i+1]:
                pass
            elif s[i].upper() == s[i+1]:
                s = s[:i] + s[i+2:]
                break
            elif s[i] == s[i+1].upper():
                s = s[:i] + s[i+2:]
                break
            else:
                pass
        except IndexError:
            pass
    refnew = len(s)
#%% Puzzle 2 which letter is impeding the concatenation
refnew = 0
ref = -1
refletter = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h',
             9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o',
             16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 
             23:'w', 24:'x', 25:'y', 26:'z'}

alphalist = np.full(26, indat)
#%%
refnew = 0
ref = -1
letter = 'g'
while refnew != ref:
    ref = len(s)
    for i in range(len(s)):

        if s[i] == letter.upper():
            s = s[:i] + s[i+1:]
            break
        elif s[i] == letter:
            s = s[:i] + s[i+1:]
            break
        else:
            pass

    refnew = len(s)
refnew = 0
ref = -1
while refnew != ref:
    ref = len(s)
    for i in range(len(s)):
        try:
            if s[i] == s[i+1]:
                pass
            elif s[i].upper() == s[i+1]:
                s = s[:i] + s[i+2:]
                break
            elif s[i] == s[i+1].upper():
                s = s[:i] + s[i+2:]
                break
            else:
                pass
        except IndexError:
            pass
    refnew = len(s)
#%%


