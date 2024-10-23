# -*- coding: utf-8 -*-
"""
Mini Assignment
"""

import numpy as np, matplotlib.pyplot as plt, pandas as pd

file = 'fismflux20020824.dat'

df = pd.read_csv(file)

dataList = df.iloc[:,0][55][22::].split()
x = np.arange(0, len(dataList))

data = []

for i in dataList:
    data.append(float(i))

plt.plot(x, data)
plt.title('EUV Spectrum vs Functional Index Number of List')
plt.ylabel('EUV Spectrum $\\frac{W}{m^{2}/nm}$', size = 10)
plt.xlabel('Functional Index Number')
plt.grid()
