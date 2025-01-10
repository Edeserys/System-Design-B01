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

k_s = 9.5
k_c = 15

#spar properties
sparDistances = am.sparDistancesResult


L_skin = am.ch*2/(c-1)
t_skin = t




# Methods:
# The Method takes the Length of a Stringer (L_str)
# The Method gives the Thickness of a Stringer (t_str)
def dimensions(L_str):

    t_str = L_str - math.sqrt(L_str**2 + 500*10**-6)
    return t_str
print(dimensions(0.15))
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
    A1 = t1 * L1 
    A2 = t2 * L2
    A_skin = t_skin * L_skin
    y_avg = Centroid(t1, L1, t2, L2, t_skin, L_skin)
    Ixx = 1/12*t1*L1**3 + 1/12*L2*t2**3 + 1/12*L_skin*t_skin**3 + A1*(t_skin+L1/2-y_avg)**2 + A2*(t_skin+t2/2-y_avg)**2 + A_skin*(t_skin/2-y_avg)**2
    return Ixx

# The Method takes the clamping coefficient (K), Elastic Modulus (E), Length (L) and Area (A)
# The Method gives the Critical Column Buckling Stress (sigma_cr)
def columnBuckling(L1, K, E, L, A):
    sigma_cr = (K*math.pi**2*E*Ixx(L1))/(L**2*A) *3
    return sigma_cr


# The Method takes the skin buckling coefficient (k_c), the Elastic Modulus (E), the skin thickness (t) and the length (L)
# The Method gives the Critical Skin Buckling Stress (sigma_cr)
def skinBuckling(k_c, E, t_skin, b_skin, nu=1/3):
    sigma_cr = (math.pi**2 * k_c * E) / (12+(1-nu**2)) * (2*t_skin/b_skin)**2
    return sigma_cr



