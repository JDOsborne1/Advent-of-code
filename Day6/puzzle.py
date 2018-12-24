# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 13:04:30 2018

@author: j_osborne
"""

#Day 6
#%% Libraries
import numpy as np


#%%
#defining manhattan function
def manhattan(tup1, tup2):
    return abs(tup1[0] - tup2[0]) + abs(tup1[1] - tup2[1])
#%%
#defining the space the co-ordinates occupy
zone = np.zeros(400)

#%%


