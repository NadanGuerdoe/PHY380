# -*- coding: utf-8 -*-

import numpy as np, matplotlib.pyplot as plt

G = 6.674*10**(-11)
MS = 1988400*10**(24)
ME = 5.9722*10**(24)
AU = 1.49598*10**11
time_conversion = 365.25*24*3600 # years to seconds

x0 = 1 # In AU for Earth
y0 = 0

xE0 = x0*AU 
yE0 = y0*AU
vxE0 = 0
vyE0 = 2*np.pi*np.sqrt(xE0**2+yE0**2)/time_conversion

dt = 0.002*time_conversion # years
t0 = 0
tf = 5

t = np.arange(t0*time_conversion, tf*time_conversion, dt)
xE = np.zeros(len(t))
yE = np.zeros(len(t))
vxE = np.zeros(len(t))
vyE = np.zeros(len(t))


xE[0] = xE0
yE[0] = yE0
vxE[0] = vxE0 
vyE[0] = vyE0

for i in range(len(t) - 1):
    r = np.sqrt(xE[i]**2+yE[i]**2)
    
    #breakpoint()
    
    Fg = -G*MS*ME/(r**2)
    
    aX = Fg * (xE[i] / r) / ME
    vxE[i+1] = vxE[i] + aX*dt
    xE[i+1] = xE[i] + vxE[i+1]*dt
    
    aY = Fg * (yE[i] / r) / ME
    vyE[i+1] = vyE[i] + aY*dt
    yE[i+1] = yE[i] + vyE[i+1]*dt
    
    
#plt.plot(xE, yE)
plt.figure(figsize=(8, 8))
plt.plot(xE/AU,yE/AU)
plt.xlabel('X Axis (AU)')
plt.ylabel('Y Axis (AU)')
plt.grid()
plt.title('Earth Around the Sun\nat Initial Position of {} AU'.format(xE0/AU))
#plt.plot(t, axE)
    


