# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:06:21 2024

@author: natha
"""

import math, numpy as np, matplotlib.pyplot as plt

a = -1
dx = 0.1
startX = -2
endX = 2
x = np.arange(startX, endX + dx, dx)

def f(x):
    return 2 + 0.75*np.tanh(2*x)

def cdiff(f, x, h = dx):
    return (f(x + h) - f(x - h))/(2*h)

plt.gcf().set_size_inches(16, 12)
plt.plot(x, cdiff(f,x))
plt.title('Central differencing method for Derivatives\n between {} and {}'.format(startX, endX), size = 30)
plt.xlabel('Domain x', size = 30)
plt.ylabel('df/dx', size = 30)
plt.grid()
plt.savefig('CentralDiffGraph_dx01')























