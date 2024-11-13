# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:55:57 2024

Author: NadanGuerdoe
"""

## Qgrid defined by Dr. Pawlowski

from numpy import arange,vstack,meshgrid,delete
from random import choice

def qgrid(n):
    '''Usage: data = qgrid(50)

    Assigns n charges to a qgrid at random.  qgrid returns a dictionary of two arrays:
    data['charges'] is an array of charges (in Coulombs)
    data['coordinates'] is an array of coordinate pairs corresponding to the location of each charge (each pair a 2 element array, [x,y])
    '''

    h = 1
    x = arange(-10,10+h,h)
    y = arange(-20,20+h,h)

    nCharges = n
    qCharge = [-1,-.5,-.25,.25,.5,1] #charges can have this sign

    coordinates = vstack(meshgrid(x,y)).reshape(2,-1).T

    q = []
    outCoordinates = []

    for i in range(nCharges):
        myCoorIndex = choice(range(len(coordinates)))
        q.append(choice(qCharge))
        outCoordinates.append(coordinates[myCoorIndex])
        coordinates = delete(coordinates,myCoorIndex,0)

    return {'charges':q,'coordinates':outCoordinates}

## Potential python grapher by NadanGuerdoe

import numpy as np, matplotlib.pyplot as plt, pandas as pandas, math as math

n = 20 # Number of random charges
grid = qgrid(n)

e0 = 8.8541878128*10**(-12)
q1 = 1
q2 = -1
d = 0.1 

xq1 = -d/2
yq1 = 0
xq2 = d/2
yq2 = 0

minX = -10#min(grid.get('coordinates')[:][0])
maxX = 10#max(grid.get('coordinates')[:][0])
minY = -20#min(grid.get('coordinates')[:][1])
maxY = 20#max(grid.get('coordinates')[:][1])

#mylevels = np.arange(min(V),max(V)))

xrange = np.linspace(minX, maxX, 100)
yrange = np.linspace(minY, maxY, 100)

def V(q, x, y, xq, yq, d, e0 = e0):
    V = []
    E = []
    Ex = []
    Ey = []
    for j in xrange:
        for k in yrange:
            r = np.sqrt((j-xq)**2+(k-yq)**2)
            V.append((q/(4*np.pi*e0*r)))
            E.append(-(q/(4*np.pi*e0*r**2)))
            Ex.append(-(q*j/(4*np.pi*e0*r)))
            Ey.append(-(q*k/(4*np.pi*e0*r)))
    #breakpoint()
    return [V, E, Ex, Ey]

df = {'V1': V(q1, xrange, yrange, xq1, yq1, d)[0], 'V2': V(q2, xrange, yrange, xq2, yq2, d)[0], 
     'E1': V(q1, xrange, yrange, xq1, yq1, d)[1], 'E2': V(q2, xrange, yrange, xq2, yq2, d)[1]}

dataframe = pandas.DataFrame.from_dict(data=df)

V1 = dataframe[['V1']].values.ravel()
V2 = dataframe[['V2']].values.ravel()
E1 = dataframe[['E1']].values.ravel()
E2 = dataframe[['E2']].values.ravel()

Vi = []
Ei = []
Ex = []
Ey = []

i = 0
while i < n:
    Vi.append(np.array(V(grid.get('charges')[i], xrange, yrange, grid.get('coordinates')[i][0], grid.get('coordinates')[i][1], d)[0]))
    Ei.append(np.array(V(grid.get('charges')[i], xrange, yrange, grid.get('coordinates')[i][0], grid.get('coordinates')[i][1], d)[1]))
    Ex.append(np.array(V(grid.get('charges')[i], xrange, yrange, grid.get('coordinates')[i][0], grid.get('coordinates')[i][1], d)[2]))
    Ey.append(np.array(V(grid.get('charges')[i], xrange, yrange, grid.get('coordinates')[i][0], grid.get('coordinates')[i][1], d)[3]))
    #print(Vi)
    i += 1

V_tot = sum(Vi)
V_tot = V_tot.reshape(len(xrange),len(yrange)).T

#dV_tot_dx = np.gradient(E1, xrange)
#dV_tot_dy = np.gradient(E2, yrange)
E1 = sum(Ex)
E2 = sum(Ey)
E1 = E1.reshape(len(xrange),len(yrange)).T
E2 = E2.reshape(len(xrange),len(yrange)).T
E_tot = sum(Ei)
E_tot = E_tot.reshape(len(xrange),len(yrange)).T 

#mylevels = np.arange(min(V),max(V), 1000)

plt.figure()
plt.gcf().set_size_inches(16, 12)
plt.title('Contour Plot of the Electric Potentials\nbetween two charges', size = 30)
plt.xlabel('Horizontal Axis x (m)', size = 30)
plt.ylabel('Vertivcal Axis y (m)', size = 30)
plt.contourf(xrange, yrange, V_tot, levels = 15, cmap='gist_heat')
plt.xlim(min(xrange),max(xrange))
plt.ylim(min(yrange),max(yrange))
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
Q = plt.quiver(xrange, yrange, E1, E2, E_tot, width = 0.002, scale = 0.5*10**13)
plt.tick_params(labelsize=15)
plt.quiverkey(Q, X=0.1, Y=-0.055, U=10**14, label='Quiver key, length = 10^14 V/m', labelpos='E')
plt.grid(linewidth=0.2, color = "k")
plt.savefig('efield.png')
#qk = ax.quiverkey(Q, 0.5*d, 0.5*d, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   #coordinates='figure')
