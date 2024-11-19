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

# Clear Console:
os.system('cls')

# Read Files:
file_path1 = 'C:\\Users\AsusPro\Documents\TU Delft\BSc\Year 2\Q2\Systems Design\WP4\MainWing a0.txt'
file_path2 = 'C:\\Users\AsusPro\Documents\TU Delft\BSc\Year 2\Q2\Systems Design\WP4\MainWing a0.txt'

with open(file_path1, 'r') as file1:
    data1 = np.genfromtxt(file_path1, skip_header = 40, skip_footer = 1029)
with open(file_path2, 'r') as file2:
    data2 = np.genfromtxt(file_path2, skip_header = 40, skip_footer = 1029)
#print(data)
    
# Store Variables:
ylst = []
Cllst = []
Cdlst = []
Cmlst = []

y_span2 = []
cl2 = []
cd2 = []
cm2 = []

# 
print("File 1:")
ylst = data1[:, 0]
Cllst = data1[:, 3]
Cdlst = data1[:, 5]  # ICd
Cmlst = data1[:, 7]  # CmGeom

# Print the extracted data for verification
print("y-span:", ylst)
print("Cl:", Cllst)
print("Cd:", Cdlst)
print("Cm:", Cmlst)

print("File 2:")
y_span2.append(data2[:, 0])
cl2.append(data2[:, 3])
cd2.append(data2[:, 5])  # ICd
cm2.append(data2[:, 7])  # CmGeom

# Print the extracted data for verification
print("y-span:", y_span2)
print("Cl:", cl2)
print("Cd:", cd2)
print("Cm:", cm2)

# Cl(y):
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

# Cd(y):
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

# Cm(y):
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
