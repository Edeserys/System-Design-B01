"""Stringer Dimensions"""
# Import Libraries
# Clear Console
# Parameters
# Methods
    # Centroid
    # Area Moment of Inertia (Ixx)
    # Column Buckling
# 

# Import Libraries
import os
import math

# Clear Console:
os.system('cls')

# Parameters:

# Methods:
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
def Ixx(t1, L1, t2, L2, t_skin, L_skin):
    A1 = t1 * L1 
    A2 = t2 * L2
    A_skin = t_skin * L_skin
    y_avg = Centroid(t1, L1, t2, L2, t_skin, L_skin)
    Ixx = 1/12*t1*L1**3 + 1/12*L2*t2**3 + 1/12*L_skin*t_skin**3 + A1*(t_skin+L1/2-y_avg)**2 + A2*(t_skin+t2/2-y_avg)**2 + A_skin*(t_skin/2-y_avg)**2
    return Ixx

# The Method takes the clamping coefficient (K), Elastic Modulus (E), Length (L) and Area (A)
# The Method gives the Critical Buckling Stress (sigma_cr)
def columnbuckling(K,E,L,A):
   Ixx = Ixx(t1, L1, t2, L2,t_skin,L_skin)
   sigma_cr = (K*math.pi**2*E*Ixx)/(L**2*A) 
   return sigma_cr
