"""Stringer Properties"""
# Import Libraries
# Clear Console
# Parameters
# Methods
    # Chord Length
    # Skin Properties - Length and Thickness
    # Thickness of the Stringer
    # Centroid
    # Area Moment of Inertia (Ixx)
    # Column Buckling
    # Thickness-to-Length Ratio (t/b)
    # Skin Buckling
# Print Results

# Import Libraries
import os
import math
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)
import numpy as np
import matplotlib.pyplot as plt


import wp5.yld as yld
from cases import *
import wp4.areaMoments as am
import wp4.deflections as defl
import constants

# Clear Console:
os.system('cls')

# Constants:
nu = constants.nu
c_r = constants.C_R #m
c_t = constants.C_T #m
E = constants.E #Pa
b = constants.b #m

# Parameters:
t, c = casesWP4(0)
k_c = 7
n_ribs = 10
b_spar = b / 2 / n_ribs #m





# Methods:
# The Method takes the y-Span Position (y)
# The Method gives the Chord Length (c) at a certain y_Span (y)
def c_y(y):
    return (1-y/(b/2))*c_r + y/(b/2)*c_t

# The Method takes the case number and the y-Span
# The Method gives the Length of the Skin
def skinProperties(case, y):
    if case == 0:
        t_skin = 0.008 #m
        b_skin = 0.2509/(20/4) * c_y(y) #m 
    elif case == 1:
        t_skin = 0.004 #m
        b_skin = 0.1/(35/10)* c_y(y) #m
    else: 
        t_skin = 0.002 #m
        b_skin = 0.0625/(50/16)  * c_y(y) #m
    return b_skin, t_skin

# The Method takes the Length of a Stringer (L_str)
# The Method gives the Thickness of a Stringer (t_str)
def dimensions(L_str):
    t_str = L_str - math.sqrt(L_str**2 - 500*10**-6)
    return t_str

# The Method takes as arguments the stringer and skin thicknesses (t1, t2 and t_skin) and lengths (L1, L2, L_skin)
# The Method gives the centroid's y-Location (y_avg)
def Centroid(t1, L1, t2, L2, t_skin, L_skin):
    A1 = t1 * L1
    A2 = t2 * L2
    A_skin = t_skin * L_skin
    y_avg = ((t_skin+L1/2)*A1 + (t_skin+t2/2)*A2 + ((t_skin/2)*A_skin))/(A1+A2+A_skin)
    return y_avg

# The Method takes as arguments the stringer and skin thicknesses (t1, t2 and t_skin) and lengths (L1, L2, L_skin)
# The Method gives the Area Moment of Inertia (Ixx)
def Ixx(L1):
    t1 = dimensions(L1)
    t2 = t1
    L2 = L1-t1
    L_skin, t_skin = skinProperties(0, 0)
    A1 = t1 * L1 
    A2 = t2 * L2
    A_skin = t_skin * L_skin
    y_avg = Centroid(t1, L1, t2, L2, t_skin, L_skin)
    Ixx = 1/12*t1*L1**3 + 1/12*L2*t2**3 + 1/12*L_skin*t_skin**3 + A1*(t_skin+L1/2-y_avg)**2 + A2*(t_skin+t2/2-y_avg)**2 + A_skin*(t_skin/2-y_avg)**2
    return Ixx

# The Method takes the clamping coefficient (K), Elastic Modulus (E), Length (L) and Area (A)
# The Method gives the Critical Column Buckling Stress (sigma_cr)
def columnBuckling(L1, K, E, L, A):
    t1 = dimensions(L1)
    sigma_cr = (K*math.pi**2*E*Ixx(L1))/(L**2*A) 
    return sigma_cr

# The Method takes the thickness (t) and the length (L)

# The Method takes the skin buckling coefficient (k_c), the Elastic Modulus (E), the skin thickness (t) and the length (L)
# The Method gives the Critical Skin Buckling Stress (sigma_cr)
def skinBuckling(k_c, E, t_skin, b_skin, nu=1/3):
    sigma_cr = (math.pi**2 * k_c * E) / (12+(1-nu**2)) * (t_skin/b_skin)**2
    return sigma_cr


# Print Area Moment of Inertia (Ixx) and Critical Column and Skin Buckling Stress:
print(f"{Ixx(40*10**-3)*10**16} mm^4") 
b_skin, t_skin = skinProperties(2, np.linspace(0, b/2, 146))
# print(f"{columnBuckling(40*10**-3, 4, E, b/(2*n_ribs), 500*10**-6+b_skin*t_skin)*10**-6} [MPa]")
# print(f"{skinBuckling(k_c, E, t_skin, b_skin)*10**-6} [MPa]")

M = defl.M
Ixx1 = am.Ixx1
D_total = am.D_total
h1 = am.h1

stress = yld.yieldCalc(M, Ixx1, -(D_total-h1))

safety = yld.safetyFactor(stress, skinBuckling(k_c, E, t_skin, b_skin))
# safety[-1]=0
# safety[-2]=0

plt.plot(np.linspace(0, b/2, 146),  yld.safetyFactor(stress, skinBuckling(k_c, E, t_skin, b_skin)), label="Stress")
plt.plot(np.linspace(0, b/2, 146), yld.safetyFactor(stress, columnBuckling(40*10**-3, 4, E, b/(2*n_ribs), 500*10**-6+b_skin*t_skin)), label="Stress")
plt.ylim(0, 15)
plt.show()