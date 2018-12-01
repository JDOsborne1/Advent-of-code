# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 17:39:14 2018

@author: Joe
"""
#import numpy as np
# Puzzle 2

## find the first repeated number
#%% Making the empty variables
History = []
Current = 0
track = 0
#%% The Iterative process
#testlist = np.array([1,-2,3,1])

while (Current not in History[:-1]):
    Current += inputtxt[track]
    History.append(Current)
    track += 1
    track %= len(inputtxt)
    print(Current, track)
    
