import os
import math
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

"""Finding Critical Mach Number"""
# Import Libraries
# Constants
# Initialise Method
# Parameters
# Initial Conditions
# Store Variables for 2 Graphs
# Mach-to-Pressure-Coefficient Graphs
    # 1) First Graph Loop (0<=M<=0.9)
    # 2) Second Graph Loop (0.3<=M<=0.9)
# Finding the Critical Point
# Printing the Critical Point
# Plotting Graphs

# Import Libraries
import wp1.mass_estimation 
import math
import os
import matplotlib.pyplot as plt
from constants import *

os.system('cls')

# Constants:


# Method for Finding Points of Graph 
# for Critical Pressure Coefficient (C_p_crit):
def Find_C_p_crit(M_inf):
    return 2 / (gamma * M_inf**2) * (((1+((gamma-1)/2)*M_inf**2)/(1+((gamma-1)/2)))**(gamma/(gamma-1))-1)

# Parameters:
dM = 0.002

# Initial Conditions:
C_p0_min = -0.974
M_0 = 0
M_inf=M_0+0.3
C_p_crit = Find_C_p_crit(M_inf)

# Store Variables:
M_0tab = [M_0]
C_p0tab = [C_p0_min]
M_crittab = [M_inf]
C_p_crittab = [C_p_crit]

# Mach-to-Pressure-Coefficients Graphs:
# 1) Loop for First Graph 0<=M<=0.9:
while M_0 < 0.9:
    M_0 += dM
    C_p_min = C_p0_min / math.sqrt(1-M_0**2)

    M_0tab.append(M_0)
    C_p0tab.append(C_p_min)

# 2) Loop for Second Graph 0.3<=M<=0.9:
while M_inf < 0.9:
    M_inf += dM
    C_p_crit = Find_C_p_crit(M_inf)

    M_crittab.append(M_inf)
    C_p_crittab.append(C_p_crit)
    
# Finding Critical Point:
crit_point = [] 
j = 0
for i in range(len(C_p0tab)):
        # Cannot compare the two graphs since Graph 2 is undefined for M<0.3
        if M_0tab[i] < 0.3:
            continue
        if C_p0tab[i] < C_p_crittab[j]:
            crit_point.append(M_0tab[i])
            crit_point.append(C_p0tab[i])
            break
        j += 1

# Print Critical Point:
print(f"Airfoil Critical Point: \nM_crit = {round(crit_point[0],3)} \nC_p_crit = {round(crit_point[1],3)}")

print("\nWing:")
print(f"M_crit = {round(crit_point[0]/math.cos(math.radians(24)),3)}")

# Plotting Code:
plt.plot(M_0tab, C_p0tab)
plt.plot(M_crittab, C_p_crittab)
plt.plot(crit_point[0],crit_point[1],'r*')
plt.grid(True)
plt.xlabel("Freestream Mach Number, M")
plt.ylabel("Pressure Coefficient, C_p")

plt.show()
