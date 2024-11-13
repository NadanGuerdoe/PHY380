# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:36:28 2024

Author: NadanGuerdoe
"""
import numpy as np, matplotlib.pyplot as plt, sympy as smp

h = 0.1
startX = 0
endX = 20
startT = 0
endT = 20
x = np.arange(startX,endX,h)
t = np.arange(startT,endT,h)

k = 3
m = 2 
A = k/m
C = 5
V_0 = 0
y0 = 2

def ode(y,V,A,C):
    dvdt = -C*V - A*y
    return dvdt

def Euler(y,V, A, C):
    v1 = V + ode(y, V, A, C)*h
    y1 = y + V*h
    return [y1,v1]

'''
def RK2(A,C,v,y,t):
    k1 = ode(y, t, A, C, V)*h
    k2 = ode(y + k1/2,t + k1/2)*h
    yn = y + k2
    return yn
 
'''

EulerY = [y0]
V = [V_0]
RK2Y = [y0]


i = 0    
while i < len(t) - 1:
    y_2 = Euler(EulerY[i], V[i], A, C)[0]
    v_2 = Euler(EulerY[i], V[i], A, C)[1]
    EulerY.append(y_2)
    V.append(v_2)
    
    i += 1

plt.figure()
plt.title('Eulers Method for ODE, C = {}'.format(C))
plt.xlabel('X range')
plt.ylabel('Y range')
plt.plot(x, EulerY)
#plt.plot(x, RK2Y)
plt.grid()




