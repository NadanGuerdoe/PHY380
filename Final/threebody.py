# -*- coding: utf-8 -*-

import numpy as np, matplotlib.pyplot as plt

G = 6.674*10**(-11)
MS = 1988400*10**(24)
ME = MS#5.9722*10**(24)
MJ = 1.89813*10**(27)
AU = 1.49598*10**11
time_conversion = 365.25*24*3600 # years to seconds

x0 = 1 # In AU for Earth
y0 = 0

xJ0 = 5.2
yJ0 = 0

xS0 = 0
yS0 = 0

xE0 = x0*AU 
yE0 = y0*AU
vxE0 = 0
vyE0 = 2*np.pi*np.sqrt(xE0**2+yE0**2)/time_conversion

xJ0 = xJ0*AU 
yJ0 = yJ0*AU
vxJ0 = 0
vyJ0 = 2*np.pi*np.sqrt(xJ0**2+yJ0**2)/(12*time_conversion)

xS0 = xS0*AU 
yS0 = yS0*AU
vxS0 = 0
vyS0 = 0

xCM0 = (xS0*MS+xE0*ME+xJ0*MJ)/(MS+ME+MJ)
yCM0 = (yS0*MS+yE0*ME+yJ0*MJ)/(MS+ME+MJ)
vxCM0 = 0
vyCM0 = 0

dt = 0.001*time_conversion # years
t0 = 0
tf = 0.01

t = np.arange(t0*time_conversion, tf*time_conversion, dt)

xE = np.zeros(len(t))
yE = np.zeros(len(t))
vxE = np.zeros(len(t))
vyE = np.zeros(len(t))

xJ = np.zeros(len(t))
yJ = np.zeros(len(t))
vxJ = np.zeros(len(t))
vyJ = np.zeros(len(t))

xS = np.zeros(len(t))
yS = np.zeros(len(t))
vxS = np.zeros(len(t))
vyS = np.zeros(len(t))

xCM = np.zeros(len(t))
yCM = np.zeros(len(t))
vxCM = np.zeros(len(t))
vyCM = np.zeros(len(t))

xE[0] = xE0
yE[0] = yE0
vxE[0] = vxE0 
vyE[0] = vyE0

xJ[0] = xJ0
yJ[0] = yJ0
vxJ[0] = vxJ0 
vyJ[0] = vyJ0

xS[0] = xS0
yS[0] = yS0
vxS[0] = vxS0 
vyS[0] = vyS0

xCM[0] = xCM0
yCM[0] = yCM0
vxCM[0] = vxCM0 
vyCM[0] = vyCM0

for i in range(len(t) - 1):
    #breakpoint()
    
    
    
    rCM = np.sqrt(xCM[i]**2 + yCM[i]**2)
    rE = np.sqrt((xE[i] + xCM[i])**2 + (yE[i]+xCM[i])**2)
    rJ = np.sqrt((xJ[i] + xCM[i])**2 + (yJ[i]+xCM[i])**2)
    rS = np.sqrt((xS[i] + xCM[i])**2 + (yS[i]+xCM[i])**2)
    
    rES = rE - rS
    rSE = rS - rE
    rEJ = rE - rJ
    rJE = rJ - rE
    rJS = rJ - rS
    rSJ = rS - rJ
    
    #rEJ = np.sqrt((xE[i] - xJ[i])**2 + (yE[i] - yJ[i])**2)
    #rES = np.sqrt((xE[i] - xS[i])**2 + (yE[i] - yS[i])**2)
    #rJS = np.sqrt((xJ[i] - xS[i])**2 + (yJ[i] - yS[i])**2)
    
    #breakpoint()
    
    FgES = -G*MS*ME/(rES**3)*np.array([xE[i] - xS[i], yE[i] - yS[i]])
    FgSE = -G*MS*ME/(rSE**3)*np.array([xS[i] - xE[i], yS[i] - yE[i]])
    FgEJ = -G*MJ*ME/(rEJ**3)*np.array([xE[i] - xJ[i], yE[i] - yJ[i]])
    FgJE = -G*MJ*ME/(rJE**3)*np.array([xJ[i] - xS[i], yJ[i] - yE[i]])
    FgJS = -G*MS*MJ/(rJS**3)*np.array([xJ[i] - xS[i], yJ[i] - yS[i]])
    FgSJ = -G*MS*MJ/(rSJ**3)*np.array([xS[i] - xJ[i], yS[i] - yJ[i]])
    
    aE = (FgSE - FgJE)/ME
    aJ = (FgEJ + FgSJ)/MJ
    aS = (FgES - FgJS)/MS
    
    print(aS[1])
    
    vxE[i+1] = vxE[i] + aE[0]*dt
    vyE[i+1] = vyE[i] + aE[1]*dt
    xE[i+1] = xE[i] + vxE[i+1]*dt
    yE[i+1] = yE[i] + vyE[i+1]*dt
    
    vxJ[i+1] = vxJ[i] + aJ[0]*dt
    vyJ[i+1] = vyJ[i] + aJ[1]*dt
    xJ[i+1] = xJ[i] + vxJ[i+1]*dt
    yJ[i+1] = yJ[i] + vyJ[i+1]*dt
    
    vxS[i+1] = vxS[i] + aS[0]*dt
    vyS[i+1] = vyS[i] + aS[1]*dt
    xS[i+1] = xS[i] + vxS[i+1]*dt
    yS[i+1] = yS[i] + vyS[i+1]*dt
    
    xCM[i+1] = (xS[i+1]*MS+xE[i+1]*ME+xJ[i+1]*MJ)/(MS+ME+MJ)
    yCM[i+1] = (yS[i+1]*MS+yE[i+1]*ME+yJ[i+1]*MJ)/(MS+ME+MJ)
    
    
    
    
#plt.plot(xE, yE)
plt.figure(figsize=(8, 8))
plt.plot(xE/AU,yE/AU, label='Earth')
plt.plot(xJ/AU,yJ/AU, label='Jupiter')
plt.plot(xS/AU,yS/AU, label='Sun', color = 'red')
plt.scatter(xCM/AU,yCM/AU, color = 'k')
plt.xlabel('X Axis (AU)')
plt.ylabel('Y Axis (AU)')
plt.legend()
plt.grid()
plt.title('Earth Around the Sun\nat Initial Position of {} AU\nand Jupiter at {} AU'.format(np.sqrt(xE0**2+yE0**2)/AU, np.sqrt(xJ0**2+yJ0**2)/AU))
#plt.plot(t, axE)
    


