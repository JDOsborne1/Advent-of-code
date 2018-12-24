# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:08:04 2018

@author: j_osborne
"""

#day10 puzzle1 


#%% Data import and process

import re
import pandas as pd
import datetime as dt

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=240)

posx = re.compile(r'position=<(.\d*)')
posy = re.compile(r'position=<.\d*, (.\d*)')
velx = re.compile(r'velocity=<(.\d*)')
vely = re.compile(r'velocity=<.\d*, (.\d*)')

#%%
coords = []
vels = []

for i in inputtxt:
    xpos = int(posx.findall(i)[0])/1000 + 55     
    ypos = int(posy.findall(i)[0])/1000 + 55
    xvel = int(velx.findall(i)[0])/1000
    yvel = int(vely.findall(i)[0])/1000
    coords.append(np.array([xpos,ypos]))
    vels.append(np.array([xvel, yvel]))

#%% Update
maxes = 110
spaces = np.full((maxes, maxes), '.')
for j in range(50000):
    for i in range(len(coords)):
        coords[i] += vels[i]
        intcoord = np.round(coords[i]).astype(int)
        spaces[intcoord[0], intcoord[1]] = '#'
    
    #np.savetxt("C:/Users/j_osborne/Downloads/Day10/output/iter{}.csv".format(j) , spaces, fmt = '%c')
    #print(spaces)
                    