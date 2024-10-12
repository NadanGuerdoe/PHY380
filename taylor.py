# -*- coding: utf-8 -*-
import numpy as np, sympy as smp, matplotlib.pyplot as plt

a = 0 # Centered value
n = 4 # n terms of taylor expansion

givenEstValue = 5

ymin = -8 # minimum y value for the plot
ymax = 8 # maximum y value for the plot

rangeX = np.arange(-10, 10, 0.1) # list of inputs

x = smp.symbols('x') # sympy symbol initialization
f = smp.sin(x) # function initialization
g = smp.lambdify(x, f, 'numpy') # Converting the sympy functional format to numpy

taylorTerms = [] # empty set of calculated n terms

i = -1 

plt.plot(rangeX, g(rangeX)) # plotting the given function underneath expanded taylor series

# While loop for calculating thee nth term in the series and appending that term to a list defined as taylorTerms
# and plotting the terms individually each loop

while i < n:
    if n == 0:
        t = f.subs(x, a)
        taylorTerms.append(t)
        taylorEq = sum(taylorTerms)
    else:
        t = (f.subs(x, a)/(smp.factorial(i+1)))*(x - a)**(i+1)
        taylorTerms.append(t)
        taylorEq = sum(taylorTerms)
        rangeY = t.subs(x, rangeX)
        dfdx = smp.diff(f,x)
        f = dfdx
        
    F = []
    for j in rangeX:
            F.append(taylorEq.subs(x,j))
            
    plt.ylim(ymin, ymax)      
    plt.plot(rangeX, F)
    
    i += 1
    
plt.axvline(x=givenEstValue, color='r', linestyle='--')
plt.title('n = {} Order Taylor Expansion for the function \n{} Centered at {}'.format(n, f, a))

plt.grid()

print('The function {} evaluated at x = {} for the {} Taylor Term:'.format(f,givenEstValue, n), taylorEq.subs(x,givenEstValue).evalf())

'''
~~ Output ~~

The function cos(x) evaluated at x = 5 for the 4 Taylor Term:  -15.8333333333333
'''