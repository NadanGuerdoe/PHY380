# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:42:15 2024

Author: NadanGuerdoe
"""

import random as rd, numpy as np, matplotlib.pyplot as plt

steps = 100
walkers = 500

startX = 0
startY = 0
endX = steps + 1
endY = 15

t1 = np.arange(0, endX, 1)
t2 = np.arange(0, endX, 1)
x = np.zeros(endX)

def walkerAvg(walkerData):
    avg = np.mean(walkerData, axis = 0)
    return avg

walkerPosList = []

j = 0
while j < walkers:
    x[0] = startX
    i = 0
    while i < endX - 1:
        x[i+1] = x[i] + rd.uniform(-1,1)
        i += 1
    walkerPosList.append(np.array(x))
    plt.plot(t1, x)
    j += 1
    
plt.grid()


walkerAverages = walkerAvg(walkerPosList)
walkerAveragesSq = np.square(walkerAverages)
plt.title('Zombie Walker Simulation 1D\nfor {} zombies with Position\nversus number of Steps'.format(walkers))
plt.xlabel('Step Number I')
plt.ylabel('Position x')
plt.figure()

#walkerDist = np.linspace(min(walkerxf), max(walkerxf), walkers)
plt.plot(t2, walkerAveragesSq)

plt.title('Zombie Walker Simulation 1D\nfor {} zombies with Mean Distance Squared\nversus the number of Steps'.format(walkers))
plt.xlabel('Step Number I')
plt.ylabel('Mean Distance Squared $<{x_{n}}^{2}>$')
plt.grid()