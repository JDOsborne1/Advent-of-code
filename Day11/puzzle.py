# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 13:02:36 2018

@author: j_osborne
"""
import numpy as np

zone = np.zeros((300,300))

def value(i,j, serial):
    return (((j * pow(i + 1, 2) + serial * (i + 10))//100) % 10) - 5
#%%
for i in range(len(zone)):
    for j in range(len(zone)):
        zone[j,i] = value(i, j, 8141)
        
#%%
cells = np.zeros((298,298))
for i in range(298):
    for j in range(298):
        cells[j,i] = np.sum(zone[j:j+3,i:i+3])
#%%
np.amax(cells)
#%%
maxloc = np.isin(cells, [31.0])
#%%
np.where(maxloc)