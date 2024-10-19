"""Longitudinal CG Position"""
# Import Libraries
# Clear Console
# Constants
# Methods
    # 1) 2D Array --> Mass x Position (M_i*X_i)
    # 2) 2D Array --> x-position (X_j)
    # 3) Separate for readability
# Parameters
# Selection of Engines
    # 1) Fuselage-Mounted
    # 2) Wing-Mounted
# Subgroups, Mass Groups = 2D arrays
    # 1) Adjust X_i for Choice of Engines
    # 2) Compute M_i*X_i 
# Groups, Take-Off Groups = 2D arrays
    # 1) Compute M_j and M_j*X_j
    # 2) Compute X_j
# Find x_LEMAC and x_TEMAC
# Find x_{C.G._{max}} and x_{C.G._{min}}

# Import Libraries:
import os
import WP1
import numpy as np
import random

# Clear Console:
os.system('cls')

# Constants:
g = WP1.g # m/s^2

# The Method takes a 2D array
# The Method fills values in the column M_i*X_i 
def Mi_times_Xi(CG):
    rows = CG.shape[0]
    for i in range(rows):
        CG[i, 3] = round(float(CG[i,1]) * float(CG[i,2]), 6)

# The Method takes a 2D array
# The Method fills values in the column of the x-position of the C.G. (X_j) 
def X_j(CG):
    rows = CG.shape[0]
    for j in range(rows):
        CG[j,2] = round(float(CG[j,3]) / float(CG[j,1]), 3)

# The Method separates different sections of the code for better readability
def Separate():
    print("---------------------------------------------------")

# Parameters:
MAC = 3.197 # m

# Selection of Fuselage-Mounted Engines or Wing-Mounted Engines
sw = True
while sw:
    print("Select by writing 1 or 2 if the Engines will be mounted to the: \n1. Fuselage \n2. Wings")
    choice = int(input("Choice: ")) 
    if choice == 1:
        Wing_Group_Components = ["Wing"]
        sw = False
    elif choice == 2:
        Wing_Group_Components = ["Wing"]
        Wing_Group_Components.append("Nacelle")
        Wing_Group_Components.append("Propulsion")
        sw = False
    else:
        Separate()
        continue
Separate()


# Subgroups 2D Array:
# Subgroup Name, Mass (m_i), x-position of C.G. (x_i), m_i*x_i  
CG_SubGroups = np.array([["Wing", 0.103, 1.2788, 0],
                         ["Empennage", 0.029, 28.548, 0],
                         ["Fuselage", 0.122, 12.688, 0],
                         ["Nacelle", 0.015, -1, 0],
                         ["Propulsion", 0.085, -1, 0],
                         ["Fixed Equipment", 0.164, 12.688, 0]]
                         )
rows_Sub = CG_SubGroups.shape[0]

# Choice of x-position of Nacelle and Propulsion based on the Engines:
if choice == 1:
    CG_SubGroups[3,2] = 21.8916
    CG_SubGroups[4,2] = 21.8916
elif choice == 2:
    CG_SubGroups[3,2] = 0.97175
    CG_SubGroups[4,2] = 0.97175

# Calculation of m_i*x_i:
Mi_times_Xi(CG_SubGroups)



# Groups 2D Array:
# Group Name, Mass (m_j), x-position of C.G. (x_j), m_j*x_j
CG_Groups = np.array([["Fuselage", 0.0, 0.0, 0.0], 
                      ["Wing", 0.0, 0.0, 0.0]]
                      )

# Calculation of Mass (m_j) and m_j*x_j:                    
for i in range(rows_Sub):
    if CG_SubGroups[i,0] in Wing_Group_Components:
        CG_Groups[1,1] = float(CG_Groups[1,1]) + float(CG_SubGroups[i,1])
        CG_Groups[1,3] = float(CG_Groups[1,3]) + float(CG_SubGroups[i,3])
    else:
        CG_Groups[0,1] = float(CG_Groups[0,1]) + float(CG_SubGroups[i,1])
        CG_Groups[0,3] = float(CG_Groups[0,3]) + float(CG_SubGroups[i,3])

# Calculation of x_j:
X_j(CG_Groups)

CG_wing_rel = 0.25 # at the quarter-chord point (c/4); must be between 0.15*MAC and 0.3*MAC

R_Wing_to_Fus_Mass = float(CG_Groups[1,1])/float(CG_Groups[0,1])
x_LEMAC = round(float(CG_Groups[0,2]) + MAC * ((float(CG_Groups[1,2]) / MAC * R_Wing_to_Fus_Mass)-CG_wing_rel*(1+R_Wing_to_Fus_Mass)),3)
x_TEMAC = x_LEMAC + MAC
print(f"x_LEMAC = {x_LEMAC} [m] \nx_TEMAC = {x_TEMAC} [m]")
Separate()


# Based on the x-position of the Leading Edge Mean Aerodynamic Chord (x_LEMAC)
# x_OEW, x_payload, x_fuel can be predicted, but they should be 0.15*MAC and 0.3*MAC:

# Mass Groups 2D Array:
# Type of Mass, Mass (M_i), x-position of C.G. (X_i), M_i*X_i 
CG_Aircraft_Components = np.array([["Operational Empty Mass", 0.56857, -1, 0],
                                  ["Payload Mass", 0.2514, -1, 0],
                                  ["Fuel", 0.2596, -1, 0]]
                                  )

# Choice of x-position of Components' C.G. based on x_LEMAC:
if choice == 1:
    CG_Aircraft_Components[:,2] = [15.9, 15.4, 16.1] 
elif choice == 2:
    CG_Aircraft_Components[:,2] = [14.5, 13.8, 14.8]               

# Calculation of M_i*X_i:
Mi_times_Xi(CG_Aircraft_Components)

# Take-Off Mass Groups 2D Array:
# Take-Off Condition, Mass M_j, x-position of C.G. (X_j), M_j*X_j
CG_Take_Offs = np.array([["OEW + payload", 0, 0, 0],
                         ["OEW + payload + fuel", 0, 0, 0],
                         ["OEW + fuel", 0, 0, 0]]
                         )

# Calculation of Mass M_j and M_j*X_j:
for i in range(CG_Take_Offs.shape[0]):
    if "OEW" in str(CG_Take_Offs[i,0]):
        CG_Take_Offs[i,1] = float(CG_Take_Offs[i,1]) + float(CG_Aircraft_Components[0,1])
        CG_Take_Offs[i,3] = float(CG_Take_Offs[i,3]) + float(CG_Aircraft_Components[0,3])
    if "payload" in str(CG_Take_Offs[i,0]):
        CG_Take_Offs[i,1] = float(CG_Take_Offs[i,1]) + float(CG_Aircraft_Components[1,1])
        CG_Take_Offs[i,3] = float(CG_Take_Offs[i,3]) + float(CG_Aircraft_Components[1,3])
    if "fuel" in str(CG_Take_Offs[i,0]):
        CG_Take_Offs[i,1] = float(CG_Take_Offs[i,1]) + float(CG_Aircraft_Components[2,1])
        CG_Take_Offs[i,3] = float(CG_Take_Offs[i,3]) + float(CG_Aircraft_Components[2,3])

# Calculation of X_j:
X_j(CG_Take_Offs)



# Find foremost (min) and aftmost (max) C.G. x-position:
aft_CG = float(CG_Take_Offs[0,2])
fore_CG = float(CG_Take_Offs[0,2])
for j in range(CG_Take_Offs.shape[0]):
    if float(CG_Take_Offs[j,2]) >= aft_CG:
        aft_CG = float(CG_Take_Offs[j,2])
    if float(CG_Take_Offs[j,2]) <= fore_CG:
        fore_CG = float(CG_Take_Offs[j,2])

print(f"Foremost position of C.G.: X_C.G._max = {fore_CG} [m] \nAftmost position of C.G.: X_C.G._min = {aft_CG} [m]")
