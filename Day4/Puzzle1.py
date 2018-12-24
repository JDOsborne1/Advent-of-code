# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:01:49 2018

@author: j_osborne
"""

#Puzzle 1

#%% Data import and process

import re
import pandas as pd
import datetime as dt

import numpy as np
dategrab = re.compile(r'\[(.*)')
idgrab = re.compile(r'.Guard #(\d*).')
                    
#%% make df

#test = dt.datetime.strptime(dategrab.findall(inputtxt[0])[0], '%Y-%m-%d %H:%M')
#test2 = len(idgrab.findall(inputtxt[0])) == 0
 
for i in inputtxt:
    i[0] = dt.datetime.strptime(dategrab.findall(i[0])[0], '%Y-%m-%d %H:%M')
#%%    
log = pd.DataFrame(inputtxt, columns = ['Date','Log'])

#%%
log2 = log.sort_values(by = "Date")
log2 = log2.reset_index()
#%%
test = []
for i,j in zip(log2["Date"],log2["Log"]):
    test.append([t.strptime(i, '%Y-%m-%d %H:%M:%S').tm_min,idgrab.findall(j), j])

#%%
    import time as t
    #%%
    t.strptime(log2.Date[0], '%Y-%m-%d %H:%M:%S').tm_min
    
#%%
print( re.match(idgrab, test[0][1]) == None)

#%% 
def sleepscore(start, end):
    sleeptime = np.zeros((1,60))[0]
    for i in range(60):
        if i < end-1 and i >= start-1:
            sleeptime[i] += 1
        else:
            pass
    return sleeptime
#%%
x = (sleepscore(10, 40))
x[9]
#%%
dicto = {'1021':np.zeros((1,60))[0]}
#%%
guard = '0'

for i in range(len(test)):
    if len(test[i][1]) != 0:
        guard = test[i][1][0]
    if test[i][2] == ' falls asleep':
        try:
            dicto[guard] += sleepscore(test[i][0],test[i+1][0])
        except KeyError:
            dicto[guard] = sleepscore(test[i][0],test[i+1][0])
#%% Puzzle 1 the guard most often asleep multiplied by the minute they are most often asleep in
currentmax = 0
for i in dicto.items():
    a = sum(i[1])
    if a > currentmax:
       currentmax = a
       print( int(i[0]) * (np.argwhere(i[1]==max(i[1]))[0][0]+1))
#%% Puzzle 2 the guard who sleeps the most in any minute, multiplied by that minute
maxmins = 0
for i in dicto.items():
    b = max(i[1])
    if b > maxmins:
        maxmins = b
        print(i[0])
        print( int(i[0]) * (np.argwhere(i[1]==max(i[1]))[0][0]+1))