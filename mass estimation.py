import math

# Constants:
pi = math.pi
euler = math.e
gamma = 1.4 
R = 287
g = 9.81 # m/s^2

# TLARs:
# 1) Not Full Fuel
max_payload = 9,302 # kg
M = 0.77 
alt_CR_ft = 35000 # ft
alt_CR = alt_CR_ft * 0.3048 # m
dist_TO = 1296 # m
dist_L =  1210 # m
R_nom = 2019*1000 # m 
Design_payload = 7200 # kg

# 2) Full Fuel
max_MTOW = 2574 # km 
maxMTOW_payload = 6355 # kg
ZeroPayload_R = 2963 # km

# Assumptions:
AR = 10
WettedR = 6
BR = 7
Wetted_Area = 2000 
CF_Equi = 0.0031 # page 105
phi = 0.97 # page 106
psi = 0.0075 # page 106
E_spec = 44 # MJ/kg
T_CR = 218.808 # K, ISA 
a_CR = math.sqrt(gamma*R*T_CR)
t_E = 40 * 60 # s
R_div = 250*1000 # m

# Parameters:
f_con = 0.05
V_CR = M*a_CR

# Drag:
C_D0_CR = WettedR * CF_Equi
e_CR = 1/(AR*pi*psi+1/phi)
L_over_D_CR = 1/2 * math.sqrt(pi * AR * e_CR / C_D0_CR)
TSFC = 22*BR**(-0.19) 
eta_j = M*a_CR / (TSFC * E_spec)

# Mass estimation:
R_lost = 1/0.7 * L_over_D_CR * (alt_CR+V_CR**2/(2*g)) # m
R_eq = (R_nom + R_lost)*(1 + f_con) + 1.2 * R_div + t_E * V_CR 
f_FuelMass = 1 - euler**(-R_eq/(eta_j*E_spec*10**6/g*L_over_D_CR))
