"""Calculate Mass Fractions"""
# Import Libraries
# Set Constants
# Top-Level Aircraft Requirements:
    # Not Full Fuel Data
    # Full Fuel Data
# Assumptions
# Flying Parameters
# Drag
# Thrust
# Mass Estimation:
    # Ranges
    # Masses
    # Mass Fractions

# Import Libraries:
import math

# Constants:
pi = math.pi
euler = math.e
gamma = 1.4 
R = 287
g = 9.81 # m/s^2

# TLARs:
# 1) Not Full Fuel
max_payload = 9302 # kg
M = 0.77 
alt_CR_ft = 35000 # ft
alt_CR = alt_CR_ft * 0.3048 # m
dist_TO = 1296 # m.
dist_L =  1210 # m
Design_R = 2019 * 1000 # m 
Design_payload = 7200 # kg

# 2) Full Fuel
max_MTOW_R = 2574 * 1000 # m 
maxMTOW_payload = 6355 # kg
ZeroPayload_R = 2963 * 1000 # m

# Assumptions:
AR = 10
WettedR = 6
BR = 7 # Bypass Ratio [1-15]
Wetted_Area = 2000 # m^2
CF_Equi = 0.0031 # page 105
phi = 0.97 # page 106
psi = 0.0075 # page 106
E_spec = 44 # MJ/kg
T_CR = 218.808 # K, ISA 
a_CR = math.sqrt(gamma * R * T_CR)
t_E = 20 * 60 # s
R_div = 300 * 1000 # m
C_L_CR = 1.7
C_L_TO = 1.9
C_L_L = 2.6

# Parameters:
f_con = 0.05
V_CR = M * a_CR # m/s

# Drag:
C_D0_CR = WettedR * CF_Equi
e_CR = 1/(AR * pi * psi + 1/phi)
L_over_D_CR = 1/2 * math.sqrt(pi * AR * e_CR / C_D0_CR)

# Thrust:
TSFC = 22 * BR**(-0.19) 
eta_j = V_CR / (TSFC * E_spec)

# Mass estimation:
R_lost = 1/0.7 * L_over_D_CR * (alt_CR + V_CR**2/(2*g)) # m
R_nom_zero = ZeroPayload_R
R_nom_design = Design_R
R_eq_zero = (R_nom_zero + R_lost) * (1 + f_con) + 1.2 * R_div + t_E * V_CR
R_eq_design = (R_nom_design + R_lost) * (1 + f_con) + 1.2 * R_div + t_E * V_CR
f_FuelMass = 1 - euler**(-R_eq_design/(eta_j * E_spec*10**6/g * L_over_D_CR))
print(f_FuelMass)
R_aux_zero = R_eq_zero - R_nom_zero
R_aux_design = R_eq_design - R_nom_design

# Masses:
OE_Mass = maxMTOW_payload * (euler**((max_MTOW_R+R_aux_design)/(eta_j * L_over_D_CR * E_spec * 10**6/g))-1) / ((euler**((ZeroPayload_R+R_aux_zero)/(eta_j * L_over_D_CR * E_spec * 10**6/g))-euler**((max_MTOW_R+R_aux_design)/(eta_j * L_over_D_CR * E_spec * 10**6/g))))
Fuel_Mass = OE_Mass * (euler**((max_MTOW_R+R_aux_design)/(eta_j * L_over_D_CR * E_spec * 10**6/g))-1) + max_payload*(euler**((max_MTOW_R+R_aux_design)/(eta_j * L_over_D_CR * E_spec * 10**6/g)))
#Fuel_Mass = OE_Mass * (euler**((ZeroPayload_R+R_aux)/(eta_j * L_over_D_CR * E_spec * 10**6/g))-1)
MTOW = maxMTOW_payload + Fuel_Mass + OE_Mass

# Mass Fractions:
f_FuelMass = Fuel_Mass / MTOW
f_OEMass = OE_Mass / MTOW
f_payload = maxMTOW_payload / MTOW

print("Fuel Mass Fraction: " + f"{f_FuelMass:.3f}" + "\nOperational Empty Mass Fraction: " + f"{f_OEMass:.3f}" + "\nPayload Mass Fraction: " + f"{f_payload:.3f}")
print("\nOperational Empty Weight:", OE_Mass, "kg")
print("Maximum Take-Off Weight:", MTOW, "kg")
