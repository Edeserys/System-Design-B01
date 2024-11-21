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

# The Method takes data points.
# The Method plots Cl, Cd, Cm graphs with respect to y-span. 
def ComputeCurves(data):
    # Initialise Lists for each new Pair
    ftab = []
    gtab = []
    htab = []
    ylst = data[:, 0]
    Cllst = data[:, 3]
    Cdlst = data[:, 5]  # ICd
    Cmlst = data[:, 7]  # CmGeom
    
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

def func(ylst, Clst):
    print(len(ylst))
    print(len(Clst))
    func = sp.interpolate.interp1d(ylst, Clst, kind = 'linear', fill_value = "extrapolate")
    return func

def Extrapolated_f_values(func, functab):
    for i in range(61):
        functab.append(func(i/4))

def c_y(y):
    return (1-y/(b/2))*c_r + y/(b/2)*c_t

def f_L(y):
    L_y = f(y) * q * c_y(y)
    return L_y

def f_D(y):
    D_y = g(y) * q * c_y(y)
    return D_y

def f_M(y):
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


# File 1:
print("File 1:")
f, g, h = ComputeCurves(data1)
#print(f_L(9.4537))
#print(f_D(9.4537))
#print(f_M(9.4537))

# File 2:
print("File 2:")
f, g, h = ComputeCurves(data2)
#print(f_L(9.4537))
#print(f_D(9.4537))
#print(f_M(9.4537))
