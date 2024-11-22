# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:23:36 2024

Author: NadanGuerdoe
"""

import numpy as np, matplotlib.pyplot as plt


m = 70
P = 400 
v0 = 4
h = 2
A = 0.33 # m^3
g = 9.81
C_d = 0.9 
rho = 1.225 # kg/m^3
eta = 2*10**(-5) # Pa*s
theta = 10

dt = 0.1
t0 = 0 
tf = 200 

t = np.arange(t0, tf, dt)

y = np.zeros(len(t))
yDragA = np.zeros(len(t))
yDragAV = np.zeros(len(t))
v = np.zeros(len(t))
vDragA = np.zeros(len(t))
vDragAV = np.zeros(len(t))
F_dragA = np.zeros(len(t))
F_dragAV = np.zeros(len(t))
F_viscDrag = np.zeros(len(t))
dvdt = np.zeros(len(t))
dvdtDragA = np.zeros(len(t))
dvdtDragAV = np.zeros(len(t))

v[0] = v0
vDragA[0] = v0
vDragAV[0] = vDragA[0]

i = 0
while i < len(t) - 1:
    #breakpoint()
    F_dragA[i] = -(1/2)*C_d*rho*A*vDragA[i]**2
    F_dragAV[i] = -(1/2)*C_d*rho*A*vDragAV[i]**2
    F_viscDrag[i] = -eta*A*vDragAV[i]/h
    
    dvdtDragA[i] = P/(m*vDragA[i]) + F_dragA[i]/m
    dvdtDragAV[i] = P/(m*vDragAV[i]) + F_dragAV[i]/m + F_viscDrag[i]/m - (g)*np.sin(np.arctan(theta/100))
    dvdt[i] = P/(m*v[i])
    
    vDragA[i+1] = vDragA[i] + dvdtDragA[i]*dt
    vDragAV[i+1] = vDragAV[i] + dvdtDragAV[i]*dt
    v[i+1] = v[i] + dvdt[i]*dt
    
    yDragA[i+1] = yDragA[i] + vDragA[i+1]*dt
    yDragAV[i+1] = yDragAV[i] + vDragAV[i+1]*dt
    y[i+1] = y[i] + v[i+1]*dt
    
    i += 1
    

plt.figure()
plt.title('Cycling with and without Drag')
plt.xlabel('Time t (s)')
plt.ylabel('Velocity v (m/s)')
plt.plot(t, vDragAV, '--', label = 'Aerodynamic, Viscous Drag, and Gravity at {}%'.format(theta))
plt.plot(t, vDragA, label = 'Aerodynamic Drag')
plt.plot(t, v, label = 'No Drag')
plt.legend()
#plt.plot(x, RK2Y)
plt.grid()
