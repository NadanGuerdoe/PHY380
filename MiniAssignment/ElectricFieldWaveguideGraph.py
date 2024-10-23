# -*- coding: utf-8 -*-
"""
Mini Assignment
"""
import numpy as np, matplotlib.pyplot as plt

dx = 0.1
A = 10
a = 2
k = 0.4

x = np.arange(0, 20, dx)
f = A*np.cos(np.pi*x/a)*np.exp(-k*x)

plt.title("Electric Field along a Waveguide")
plt.xlabel("Position x (m)")
plt.ylabel("Electric Field E (V/m)")
plt.plot(x, f)
plt.grid()
plt.show()


