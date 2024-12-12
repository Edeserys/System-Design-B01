"""Stringer Dimensions"""
# Import Libraries
# Clear Console
# Parameters
# Methods
    # Centroid
    # Area Moment of Inertia (Ixx)
    # Column Buckling
    # Thickness-to-Length Ratio
    # Skin Buckling

# Import Libraries
import os
import math

# Clear Console:
os.system('cls')

# Parameters:
case = 0
b = 29.28 #m
c_r = 4.45 #m
c_t = 1.406 #m
nu = 1/3 
k_c = 7


# Methods:
# The Method takes the y-Span Position (y)
# The Method gives the Chord Length (c) at a certain y_Span (y)
def c_y(y):
    return (1-y/(b/2))*c_r + y/(b/2)*c_t

# The Method takes the case number and the y-Span
# The Method gives the Length of the Skin
def skinProperties(case, y):
    if case == 0:
        t_skin = 8
        L_skin = 0.2509 * 1000 * c_y(y)
    elif case == 1:
        t_skin = 4
        L_skin = 0.1 * 1000 * c_y(y)
    else: 
        t_skin = 2
        L_skin = 0.0625 * 1000 * c_y(y)
    return L_skin, t_skin

# The Method takes the Length of a Stringer (L_str)
# The Method gives the Thickness of a Stringer (t_str)
def dimensions(L_str):
    t_str = L_str - math.sqrt(L_str**2-500)
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
# The Method gives the Critical Buckling Stress (sigma_cr)
def columnBuckling(L1, K, E, L, A):
    t1 = dimensions(L1)
    t2 = t1
    L2 = L1-t1
    L_skin, t_skin = skinProperties(0, 0)
    sigma_cr = (K*math.pi**2*E*Ixx(L1))/(L**2*A) 
    return sigma_cr

# The Method takes the thickness (t) and the length (L)
# The Method gives the thickness-to-length ratio (t/b)
def t_over_b(t, L):
    t_over_b = t/L
    return t_over_b

# The Method takes the skin buckling coefficient (k_c), the Elastic Modulus (E), the skin thickness (t) and the length (L)
# The Method gives the critical buckling stress (sigma_cr)
def skinBuckling(k_c, E, t_skin, L_skin):
    sigma_cr = (math.pi**2 * k_c * E) / (12+(1-nu**2)) * t_over_b(t_skin, L_skin)**2
    return sigma_cr

print(f"{Ixx(40)} mm^4") 
L_skin, t_skin = skinProperties(0, 0)
print(f"{columnBuckling(40, 4, 72.4*1000, b/2*1000, 500+L_skin*t_skin)} [MPa]" )
