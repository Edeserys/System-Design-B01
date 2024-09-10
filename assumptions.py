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