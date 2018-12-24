# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:14:19 2018

@author: j_osborne
"""
import numpy as np
import re
#Puzzle 1 and 2
## identify the number of overclaimed squares

fabinch = np.full((1000,1000),'emp')


def claim(id, xstart, ystart, xwidth, ywidth):
    for i in range(xstart,xstart+xwidth):
        for j in range(ystart, ystart+ywidth):
            if fabinch[j,i] == 'emp':
                fabinch[j,i] = id
            else:
                fabinch[j,i] = 'dup'
                


#%%
#making the regex to strip the relevant information from the data
xwidthregex = re.compile(r'^\d*')
ywidthregex = re.compile(r'\d*$')

xstartregex = re.compile(r'(\d*),')
ystartregex = re.compile(r'(\d*):')

idregex = re.compile(r'#(\d*)')

for i in range(len(inputtxt)):
    row = inputtxt[i]
    xwidth = int(xwidthregex.findall(row[3])[0])
    ywidth = int(ywidthregex.findall(row[3])[0])
    xstart = int(xstartregex.findall(row[2])[0])
    ystart = int(ystartregex.findall(row[2])[0])
    id = idregex.findall(row[0])[0]
    claim(id, xstart, ystart, xwidth, ywidth)

#%% finding the sum of all the overclaimed zones
    
side = len(fabinch)
track = 0
for i in range(side):
    for j in range(side):
        if fabinch[j,i] == 'dup':
            track += 1
            
print(track)

#%% checking the integrity of all the claims
def claim_check(xstart, ystart, xwidth, ywidth):
    conflict = 0
    for i in range(xstart,xstart+xwidth):
        for j in range(ystart, ystart+ywidth):
            if fabinch[j,i] == 'dup':
                conflict += 1
            else:
                pass
    if conflict == 0:
        print(fabinch[ystart,xstart])
for i in range(len(inputtxt)):
    row = inputtxt[i]
    xwidth = int(xwidthregex.findall(row[3])[0])
    ywidth = int(ywidthregex.findall(row[3])[0])
    xstart = int(xstartregex.findall(row[2])[0])
    ystart = int(ystartregex.findall(row[2])[0])
    claim_check(xstart, ystart, xwidth, ywidth)        
