# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:55:57 2024

Author: NadanGuerdoe
"""

import numpy as np, matplotlib.pyplot as plt, pandas as pandas, math as math

e0 = 8.8541878128*10**(-12)
q1 = 1
q2 = -1
d = 0.1 

xq1 = -d/2
yq1 = 0
xq2 = d/2
yq2 = 0

minX = -0.1
maxX = 0.1

#mylevels = np.arange(min(V),max(V)))

xrange = np.linspace(minX, maxX, 100)
yrange = np.linspace(-0.2, 0.2, 100)

def V(q, x, y, xq, yq, d, e0 = e0):
    V = []
    E = []
    for j in xrange:
        for k in yrange:
            r = np.sqrt((j-xq)**2+(k-yq)**2)
            V.append((q/(4*np.pi*e0*r)))
            E.append(-(q/(4*np.pi*e0*r**2)))
    #breakpoint()
    return [V, E]

df = {'V1': V(q1, xrange, yrange, xq1, yq1, d)[0], 'V2': V(q2, xrange, yrange, xq2, yq2, d)[0], 
     'E1': V(q1, xrange, yrange, xq1, yq1, d)[1], 'E2': V(q2, xrange, yrange, xq2, yq2, d)[1]}

dataframe = pandas.DataFrame.from_dict(data=df)

V1 = dataframe[['V1']].values.ravel()
V2 = dataframe[['V2']].values.ravel()
E1 = dataframe[['E1']].values.ravel()
E2 = dataframe[['E2']].values.ravel()

V_tot = V1 + V2
V_tot = V_tot.reshape(len(xrange),len(yrange)).T

#dV_tot_dx = np.gradient(E1, xrange)
#dV_tot_dy = np.gradient(E2, yrange)
E_tot =  E1 + E2
E1 = E1.reshape(len(xrange),len(yrange)).T
E2 = E2.reshape(len(xrange),len(yrange)).T
E_tot = E_tot.reshape(len(xrange),len(yrange)).T

#mylevels = np.arange(min(V),max(V), 1000)

plt.figure()
plt.gcf().set_size_inches(16, 12)
plt.title('Contour Plot of the Electric Potentials\nbetween two charges', size = 30)
plt.xlabel('Horizontal Axis x (m)', size = 30)
plt.ylabel('Vertivcal Axis y (m)', size = 30)
plt.contourf(xrange, yrange, V_tot, levels = 30)
colorbar = plt.colorbar()
colorbar.set_label('Electric Potential V', fontsize=30)  # Set title and font size
colorbar.ax.tick_params(labelsize=15)
plt.tick_params(labelsize=15)
plt.grid(color = "k")
plt.savefig('potential.png')

plt.figure()
plt.gcf().set_size_inches(16, 12)
plt.title('Quiver plot of the Electric Field versus Position', size = 30)
plt.xlabel('Horizontal Axis x (m)', size = 20)
plt.ylabel('Vertivcal Axis y (m)', size = 20)
Q = plt.quiver(xrange, yrange, E1, E2, E_tot, width = 0.002, scale = 10**15)
plt.tick_params(labelsize=15)
plt.quiverkey( Q, X=0.1, Y=-0.055, U=10**14, label='Quiver key, length = 10^14 V/m', labelpos='E')
plt.grid(linewidth=0.2, color = "k")
plt.savefig('efield.png')
#qk = ax.quiverkey(Q, 0.5*d, 0.5*d, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   #coordinates='figure')
