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
from cases import *
from constants import *

# Clear Console:
os.system('cls')

# Parameters:
t, c = casesWP4(0)

c_r = C_R
c_t = C_T #m
k_c = 7
n_ribs = 10



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
        L_skin = 0.2509 * c_y(y) #m 
    elif case == 1:
        t_skin = 0.004 #m
        L_skin = 0.1* c_y(y) #m
    else: 
        t_skin = 0.002 #m
        L_skin = 0.0625  * c_y(y) #m
    return L_skin, t_skin

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
# The Method gives the thickness-to-length ratio (t/b)
def t_over_b(t, L):
    t_over_b = t/L
    return t_over_b

# The Method takes the skin buckling coefficient (k_c), the Elastic Modulus (E), the skin thickness (t) and the length (L)
# The Method gives the Critical Skin Buckling Stress (sigma_cr)
def skinBuckling(k_c, E, t_skin, L_skin):
    sigma_cr = (math.pi**2 * k_c * E) / (12+(1-nu**2)) * t_over_b(t_skin, L_skin)**2
    return sigma_cr


# Print Area Moment of Inertia (Ixx) and Critical Column and Skin Buckling Stress:
print(f"{Ixx(40*10**-3)*10**16} mm^4") 
L_skin, t_skin = skinProperties(2, 0)
print(f"{columnBuckling(40*10**-3, 4, E, b/(2*n_ribs), 500*10**-6+L_skin*t_skin)*10**-6} [MPa]")
print(f"{skinBuckling(k_c, E, t_skin, L_skin)*10**-6} [MPa]")
