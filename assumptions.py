import math
from constants import pi, euler, gamma, R, g
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

# Aerodynamic characteristics
C_D0_CR = WettedR * CF_Equi
e_CR = 1/(AR * pi * psi + 1/phi)
L_over_D_CR = 1/2 * math.sqrt(pi * AR * e_CR / C_D0_CR)

# Sea Level
rho_0 = 1.225 # kg/m^3
T_0 = 288.15 # K
p_0 = 101325 # Pa
# Takeoff
e_TO = e_CR
rho_TO = rho_0
T_TO = T_0
p_TO = p_0
L_TO = 1296 # m takeoff field length

# Landing
landing_field_length= 1210 #m