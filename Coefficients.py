"""Lift Distribution"""
# Import Libraries
# Clear Console
# Read Files
# 

# Import Libraries:
import os
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Store Variables:
ylst = []
Cllst = []
Cdlst = []
Cmlst = []

# The Method takes data points.
# The Method gives y-span, lift (Cl), drag (Cd) and moment (Cm) coefficients. 
def ComputeCurves(data):
    ylst = data1[:, 0]
    Cllst = data1[:, 3]
    Cdlst = data1[:, 5]  # ICd
    Cmlst = data1[:, 7]  # CmGeom
    
    # Print the Extracted Data for Verification:
    print("y-span:", ylst)
    print("Cl:", Cllst)
    print("Cd:", Cdlst)
    print("Cm:", Cmlst)
    return ylst, Cllst, Cdlst, Cmlst

# Clear Console:
os.system('cls')

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
ylst, Cllst, Cdlst, Cmlst = ComputeCurves(data1)

# 1) Cl(y):
# 1) Cl(y):
# Parameters:
f = sp.interpolate.interp1d(ylst, Cllst, kind='linear', fill_value = "extrapolate")
#print(f(10))

# Store Variables:
ytab = []
ftab = []

# Extrapolated Function:
for i in range(31):
    ytab.append(i/2)
    ftab.append(f(i/2))

# Plot:
plt.subplot(311)
plt.plot(ytab, ftab)
plt.plot(ylst, Cllst)

# 2) Cd(y):
# Parameters:
g = sp.interpolate.interp1d(ylst, Cdlst, kind='linear', fill_value = "extrapolate")

# Store Variables:
ytab = []
gtab = []

# Extrapolated Function:
for i in range(31):
    ytab.append(i/2)
    gtab.append(g(i/2))

# Plot:
plt.subplot(312)
plt.plot(ytab, gtab)
plt.plot(ylst, Cdlst)

# 3) Cm(y):
# Parameters:
h = sp.interpolate.interp1d(ylst, Cmlst, kind='linear', fill_value = "extrapolate")

# Store Variables:
ytab = []
htab = []

# Extrapolated Function:
for i in range(61):
    ytab.append(i/4)
    htab.append(h(i/4))

# Plot:
plt.subplot(313)
plt.plot(ytab, htab)
plt.plot(ylst, Cmlst)
plt.show()



# File 2:
print("File 2:")
ylst, Cllst, Cdlst, Cmlst = ComputeCurves(data2)

# 1) Cl(y):
# Parameters:
f = sp.interpolate.interp1d(ylst, Cllst, kind='linear', fill_value = "extrapolate")
#print(f(10))

# Store Variables:
ytab = []
ftab = []

# Extrapolated Function:
for i in range(31):
    ytab.append(i/2)
    ftab.append(f(i/2))

# Plot:
plt.subplot(311)
plt.plot(ytab, ftab)
plt.plot(ylst, Cllst)

# 2) Cd(y):
# Parameters:
g = sp.interpolate.interp1d(ylst, Cdlst, kind='linear', fill_value = "extrapolate")

# Store Variables:
ytab = []
gtab = []

# Extrapolated Function:
for i in range(31):
    ytab.append(i/2)
    gtab.append(g(i/2))

# Plot:
plt.subplot(312)
plt.plot(ytab, gtab)
plt.plot(ylst, Cdlst)

# 3) Cm(y):
# Parameters:
h = sp.interpolate.interp1d(ylst, Cmlst, kind='linear', fill_value = "extrapolate")

# Store Variables:
ytab = []
htab = []

# Extrapolated Function:
for i in range(61):
    ytab.append(i/4)
    htab.append(h(i/4))

# Plot:
plt.subplot(313)
plt.plot(ytab, htab)
plt.plot(ylst, Cmlst)
plt.show()
