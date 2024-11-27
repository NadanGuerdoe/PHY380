# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:42:15 2024

Author: NadanGuerdoe
"""

import random as rd, numpy as np, matplotlib.pyplot as plt

steps = 10
walkers = 500

startX = 0
startY = 0
endX = steps + 1
endY = steps + 1


t1 = np.arange(0, endX, 1)
t2 = np.arange(0, endX, 1)
x = np.zeros(endX)
y = np.zeros(endY)

def walkerAvg(walkerData):
    avg = np.mean(walkerData, axis = 0)
    return avg

walkerPosListX = []
walkerPosListY = []

j = 0
while j < walkers:
    x[0] = startX
    y[0] = startY
    i = 0
    while i < steps:
        x[i+1] = x[i] + rd.uniform(-1,1)
        y[i+1] = y[i] + rd.uniform(-1,1)
        i += 1
    walkerPosListX.append(np.array(x))
    walkerPosListY.append(np.array(y))
    plt.scatter(x, y, s = 1)
    #plt.plot(x, y, linewidth = 1)
    j += 1
    

#plt.grid()


walkerAverages = walkerAvg(walkerPosListX)
walkerAveragesSq = np.square(walkerAverages)
plt.title('A 2D Random Uniform Step Zombie Walker Simulation\nfor {} zombies with their Positions in {} Steps'.format(walkers, steps))
plt.xlabel('Step Number I')
plt.ylabel('Position x')
plt.figure()
'''
#walkerDist = np.linspace(min(walkerxf), max(walkerxf), walkers)
plt.plot(t2, walkerAveragesSq)

plt.title('Zombie Walker Simulation 1D\nfor {} zombies with Mean Distance Squared\nversus the number of Steps'.format(walkers))
plt.xlabel('Step Number I')
plt.ylabel('Mean Distance Squared $<{x_{n}}^{2}>$')
plt.grid()
'''