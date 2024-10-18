# -*- coding: utf-8 -*-
"""
zeros.py Computational Physics
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as smp

minX = 1
maxX = 4
dx = 100
tol = 1.0e-5
guess = 4

x = smp.symbols('x')
f = smp.tanh(x) - 0.5*x

NRrange = np.linspace(minX, maxX, dx)


def bisectionMethod(g,n0,nf,tol,i):
    
    midPoint = (n0 + nf)/2
    
   #breakpoint()
    
    if np.abs(f.subs(x, midPoint)) - tol > 0:
        
        
        i += 1
        
        if f.subs(x,n0)*f.subs(x,midPoint) < 0:
            return bisectionMethod(g,n0,midPoint,tol,i)
        elif f.subs(x,nf)*f.subs(x,midPoint) < 0:
            return bisectionMethod(g,midPoint,nf,tol,i)
        else:
            print('End points show evidence of no roots')
            

    return print('Bisection Method: f = {}\nmin x = {}, max x = {}, tolerance = {}, {} iterations\nSolution x = {}\n'.format(f, minX, maxX, tol, i, midPoint))
    
    
bisectionMethod(f, minX, maxX, tol, 0)
    

def NRMethod(g,guess,tol,i):
    dfdx = smp.diff(g,x)
    #breakpoint()
    while abs(g.subs(x, guess)) - tol > 0:
        newdfdx = dfdx.subs(x, guess).evalf()
        new_guess = guess - (g.subs(x,guess).evalf()/newdfdx)
        #breakpoint()
        i += 1
        return NRMethod(g,new_guess,tol,i)
    print('Newton-Raphson Method: f = {}\nFinal value: {}, {} iterations'.format(g,guess,i))
    
bisectionMethod(f, minX, maxX, tol, 0)
NRMethod(f,guess,tol,0)

'''
~~~~Output~~~~
Bisection Method: f = -0.5*x + tanh(x)
min x = 1, max x = 4, tolerance = 1e-05, 15 iterations
Solution x = 1.9150238037109375

Newton-Raphson Method: f = -0.5*x + tanh(x)
Final value: 1.91500825266946, 3 iterations
'''