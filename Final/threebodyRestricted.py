# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 21:39:51 2024

Author: NadanGuerdoe
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674 * 10**(-11)  # Gravitational constant (m^3/kg/s^2)
MS = 1988400 * 10**24  # Mass of the Sun (kg)
ME = 5.9722 * 10**24  # Mass of Earth (kg)
MJ = 1.89813 * 10**27  # Mass of Jupiter (kg)
AU = 1.49598 * 10**11  # Astronomical Unit (m)
time_conversion = 365.25 * 24 * 3600  # years to seconds

# Initial positions and velocities (in AU)
xE0, yE0 = 1, 0  # Earth position (AU)
xJ0, yJ0 = 5.2, 0  # Jupiter position (AU)
xS0, yS0 = 0, 0  # Sun position (at origin, AU)

# Initial velocities (in AU/year)
vxE0 = 0  # Earth's initial velocity (AU/year)
vyE0 = 2 * np.pi  # Earth's velocity for circular orbit (AU/year)
vxJ0 = 0  # Jupiter's initial velocity (AU/year)
vyJ0 = 2 * np.pi * np.sqrt(xJ0**2 + yJ0**2) / 12  # Jupiter's velocity (AU/year)
vxS0 = 0  # Sun's initial velocity (AU/year)
vyS0 = 0  # Sun's initial velocity (AU/year)

# Time step and total time (in years)
dt = 0.0005  # Time step (years)
t0 = 0  # Start time (years)
tf = 5  # End time (years)

# Time array
t = np.arange(t0, tf, dt)

# Arrays to store the positions and velocities
xE, yE, vxE, vyE = np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t))
xJ, yJ, vxJ, vyJ = np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t))
xS, yS, vxS, vyS = np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t))

# Initial conditions
xE[0], yE[0], vxE[0], vyE[0] = xE0, yE0, vxE0, vyE0
xJ[0], yJ[0], vxJ[0], vyJ[0] = xJ0, yJ0, vxJ0, vyJ0
xS[0], yS[0], vxS[0], vyS[0] = xS0, yS0, vxS0, vyS0

# Small threshold to prevent division by zero
eps = 1e-10

# Simulation loop
for i in range(len(t) - 1):
    # Calculate distances between the bodies
    rE = np.sqrt(xE[i]**2 + yE[i]**2)
    rJ = np.sqrt(xJ[i]**2 + yJ[i]**2)
    rS = np.sqrt(xS[i]**2 + yS[i]**2)
    rEJ = np.sqrt((xE[i] - xJ[i])**2 + (yE[i] - yJ[i])**2)
    rES = np.sqrt((xE[i] - xS[i])**2 + (yE[i] - yS[i])**2)
    rJS = np.sqrt((xJ[i] - xS[i])**2 + (yJ[i] - yS[i])**2)

    # Prevent division by zero
    rE = np.clip(rE, eps, None)
    rJ = np.clip(rJ, eps, None)
    rS = np.clip(rS, eps, None)
    rEJ = np.clip(rEJ, eps, None)
    rES = np.clip(rES, eps, None)
    rJS = np.clip(rJS, eps, None)

    # Gravitational forces
    FgES = -G * MS * ME / rES**3 * np.array([xE[i] - xS[i], yE[i] - yS[i]])
    FgJS = -G * MS * MJ / rJS**3 * np.array([xJ[i] - xS[i], yJ[i] - yS[i]])
    FgSJ = -G * MJ * MS / rEJ**3 * np.array([xS[i] - xJ[i], yS[i] - yJ[i]])
    FgSJupiter = -G * MJ * ME / rEJ**3 * np.array([xJ[i] - xE[i], yJ[i] - yE[i]])

    # Update accelerations for each body
    aE = (FgES + FgSJ) / ME
    aJ = (FgES + FgSJupiter) / MJ
    aS = (FgES + FgJS) / MS

    # Update velocities and positions
    vxE[i + 1] = vxE[i] + aE[0] * dt
    vyE[i + 1] = vyE[i] + aE[1] * dt
    xE[i + 1] = xE[i] + vxE[i + 1] * dt
    yE[i + 1] = yE[i] + vyE[i + 1] * dt

    vxJ[i + 1] = vxJ[i] + aJ[0] * dt
    vyJ[i + 1] = vyJ[i] + aJ[1] * dt
    xJ[i + 1] = xJ[i] + vxJ[i + 1] * dt
    yJ[i + 1] = yJ[i] + vyJ[i + 1] * dt

    vxS[i + 1] = vxS[i] + aS[0] * dt
    vyS[i + 1] = vyS[i] + aS[1] * dt
    xS[i + 1] = xS[i] + vxS[i + 1] * dt
    yS[i + 1] = yS[i] + vyS[i + 1] * dt

# Plot the trajectories
plt.figure(figsize=(8, 8))
#plt.plot(xE, yE, label="Earth")
plt.plot(xJ, yJ, label="Jupiter")
plt.plot(xS, yS, label="Sun", color='yellow')

plt.scatter(xS[0]/AU, yS[0]/AU, color='red', zorder=5)  # Sun initial position
#plt.scatter(xE[0], yE[0], color='blue', zorder=5)  # Earth initial position
plt.scatter(xJ[0]/AU, yJ[0]/AU, color='green', zorder=5)  # Jupiter initial position

plt.xlabel('X (AU)')
plt.ylabel('Y (AU)')
plt.legend()
plt.grid(True)
plt.title('Three-Body Simulation with a Moving Sun')
plt.show()