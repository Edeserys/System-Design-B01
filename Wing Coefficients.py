"""Lift Distribution"""
# Import Libraries
# Clear Console
# Parameters
# Store Variables
# Define Methods
# Read Files
# Compute Curves 
    # File 1 - alpha = 0 [deg]
    # File 2 - alpha = 10 [deg]
# Find Desired Lift Coefficient (CLd)
# Desired Angle of Attack (alpha_d)

# Import Libraries:
import os
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Clear Console:
os.system('cls')

# Parameters:
b = 29.28 #m
c_r = 4.45 #m
c_t = 1.406 #m
rho = 1.225 #kg/m^3
V = 10 #m/s
q = 1/2 * rho * V**2

# Store Variables:
ylst = []
Cllst = []
Cdlst = []
Cmlst = []
ytab = []
ftab = []
gtab = []
htab = []
for i in range(61):
    ytab.append(i/4)

# Define Methods:
# The Method takes data points
# The Method plots Cl, Cd, Cm graphs with respect to y-span
def ComputeCurves(data):
    # Initialise Lists for each New Pair
    ftab = []
    gtab = []
    htab = []
    ylst = data[:, 0]
    Cllst = data[:, 3]
    Cdlst = data[:, 5] # ICd
    Cmlst = data[:, 7] # CmGeom
    
    # Print the Extracted Data for Verification:
    print("y-span:", ylst)
    print("Cl:", Cllst)
    print("Cd:", Cdlst)
    print("Cm:", Cmlst)

    # 1) f(y) = Cl(y):
    # Parameters:
    f = func(ylst, Cllst)
    #print(f(10))

    # Extrapolated Function:
    Extrapolated_f_values(f, ftab)

    # Plot:
    plt.subplot(311)
    plt.plot(ytab, ftab)
    plt.plot(ylst, Cllst)

    # 2) g(y) = Cd(y):
    g = func(ylst, Cdlst)

    # Extrapolated Function:
    Extrapolated_f_values(g, gtab)

    # Plot:
    plt.subplot(312)
    plt.plot(ytab, gtab)
    plt.plot(ylst, Cdlst)

    # 3) h(y) = Cm(y):
    # Parameters:
    h = func(ylst, Cmlst)

    # Extrapolated Function:
    Extrapolated_f_values(h, htab)

    # Plot:
    plt.subplot(313)
    plt.plot(ytab, htab)
    plt.plot(ylst, Cmlst)
    plt.show()
    return f, g, h

# The Method takes a List of y-Span Values (ylst) and a List of Coefficient Values (Lift, Drag, Moment) (Clst)
# The Method returns the Interpolated Function C(y)
def func(ylst, Clst):
    func = sp.interpolate.interp1d(ylst, Clst, kind = 'linear', fill_value = "extrapolate")
    return func

# The Method takes the Interpolated function (func = C(y))
# The Method gives a List of Function Values at equally spaced y-Span Values (delta y = 0.25)
def Extrapolated_f_values(func, functab):
    for i in range(61):
        functab.append(func(i/4))

# The Method takes the y-Span Position (y)
# The Method gives the Chord Length (c) at a certain y_Span (y)
def c_y(y):
    return (1-y/(b/2))*c_r + y/(b/2)*c_t


# The following 5 Methods compute Lift Coefficients, the Lift, Drag and Moment at a certain y-Span point
# Each Coefficient Function depends on the Angle of Attack (alpha = 0 or 10 [deg])

# The Method takes a certain y-Span (y) and a Lift Coefficient Function (f = Cl(y))
# The Method gives the Lift Coefficient (CL_y) at the chosen y_Span (y)
# 1)
def f_CL_y(y, f):
    return f(y)
# 2)
# The Method takes a certain y-Span (y), the Desired Lift Coefficient (CLd), and the Lift Coefficient Functions at alpha = 0 and 10 [deg] (f0 and f10)
# The Method gives the Desired Lift Coefficient (CLd_y) at the chosen y_Span (y)
def desired_CL(y, CLd, f0, f10):
    CLd_y = f_CL_y(y, f0) + (CLd - CL0)/(CL10 - CL0) * (f_CL_y(y, f10) - f_CL_y(y, f0))
    return CLd_y
# 3)
# The Method takes a certain y-Span (y) and a Lift Coefficient Function (func = Cl(y))
# The Method gives the Lift (L_y) at the chosen y_Span (y)
def f_L(y, f):
    L_y = f(y) * q * c_y(y)
    return L_y
# 4)
# The Method takes a certain y-Span (y) and a Drag Coefficient Function (func = Cd(y))
# The Method gives the Drag (D_y) at the chosen y_Span (y)
def f_D(y, g):
    D_y = g(y) * q * c_y(y)
    return D_y
# 5)
# The Method takes a certain y-Span (y) and a Moment Coefficient Function (func = Cm(y))
# The Method gives the Moment (M_y) at the chosen y_Span (y)
def f_M(y, h):
    M_y = h(y) * q * c_y(y)**2
    return M_y

# Read Files:
file_path1 = 'C:\\Users\AsusPro\Documents\TU Delft\BSc\Year 2\Q2\Systems Design\WP4\MainWing a0.txt'
file_path2 = 'C:\\Users\AsusPro\Documents\TU Delft\BSc\Year 2\Q2\Systems Design\WP4\MainWing a10.txt'

with open(file_path1, 'r') as file1:
    data1 = np.genfromtxt(file_path1, skip_header = 40, skip_footer = 1029)
with open(file_path2, 'r') as file2:
    data2 = np.genfromtxt(file_path2, skip_header = 40, skip_footer = 1029)
#print("Data1: ", data1[:, 7])
#print("Data2: ", data2[:, 7])

# Compute Curves for alpha = 0 and 10 [deg]:
# File 1, alpha = 0 [deg]:
print("File 1: ")
f0, g0, h0 = ComputeCurves(data1)
#print(f_L(9.4537, f0))
#print(f_D(9.4537, g0))
#print(f_M(9.4537, h0))

# File 2, alpha = 10 [deg]:
print("File 2:")
f10, g10, h10 = ComputeCurves(data2)
#print(f_L(9.4537, f10))
#print(f_D(9.4537, g10))
#print(f_M(9.4537, h10))

# Find Desired Lift Coefficient (CLd):
CL0 = 0.216104
CL10 = 1.074117
CLd = 1.5 # change later!
#print(desired_CL(9.4537, CLd, f0, f10))

# Desired Angle of Attack (alpha_d): 
alpha_d = (CLd - CL0)/(CL10 - CL0)*10 # [deg]
print(alpha_d)
