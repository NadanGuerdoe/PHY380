# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:23:36 2024

Author: NadanGuerdoe
"""

import numpy as np, matplotlib.pyplot as plt


m = 70
P = 400 
v0 = 4

dt = 0.1
t0 = 0 
tf = 200 

t = np.arange(t0, tf, dt)

y = np.zeros(len(t))
v = np.zeros(len(t))
dvdt = np.zeros(len(t))

v[0] = v0

i = 0
while i < len(t) - 1:
    #breakpoint()
    dvdt[i] = P/(m*v[i])
    v[i+1] = v[i] + dvdt[i]*dt
    y[i+1] = v[i+1]*dt
    i += 1
    

plt.figure()
plt.title('Cycling without drag')
plt.xlabel('X range')
plt.ylabel('Y range')
plt.plot(t, y)
#plt.plot(x, RK2Y)
plt.grid()
