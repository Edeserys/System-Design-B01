''' Assumptions and other values provided in manual'''

import math
from constants import *
from tlars import *

# Assumptions:
AR = 10
WettedR = 6
BR = 7 # Bypass Ratio [1-15]
Wetted_Area = 2000 # m^2
CF_Equi = 0.0031 # page 105
phi = 0.97 # page 106
psi = 0.0075 # page 106
E_spec = 44 # MJ/kg


t_E = 20 * 60 # s
R_div = 300 * 1000 # m

C_LFL = 0.45 # pg 133 landing field length coefficient


# Aerodynamic characteristics
C_D0_CR = WettedR * CF_Equi
e_CR = 1/(AR * pi * psi + 1/phi)
L_over_D_CR = 1/2 * math.sqrt(pi * AR * e_CR / C_D0_CR)
c_dividedby_v = 0.024

# Sea Level
rho_0 = 1.225 # kg/m^3
T_0 = 288.15 # K
p_0 = 101325 # Pa

# Takeoff
delta_f = 35

C_D0_TO = C_D0_CR+0.0013*delta_f
e_TO = e_CR+.0026*delta_f
C_L_TO = 1.9
h2 = 15.24 # m 50ft

rho_TO = rho_0
T_TO = T_0
p_TO = p_0
L_TO = 1296 # m takeoff field length

# Climb
beta_cl = 0.95
CR = 7.62
cGrad = 1.8/100
T_cl = 240.7
p_cl = 39355
rho_cl = 0.5696

# Cruise
beta_cr = 0.95
C_L_CR = 1.7
T_CR = 218.808 # K, ISA 
a_CR = math.sqrt(gamma * R * T_CR)
V_CR = M * a_CR
p_CR = 23842
rho_CR = 0.3796

# Landing
delta_f = 20

C_D0_L = C_D0_CR+0.0013*delta_f
e_L = e_CR+.0026*delta_f


landing_field_length= 1210 #m
rho_L = rho_0
beta_L = 0.7533 # fuel mass fraction - loiter
C_L_L = 2.6
V_app = 70


# CS 25.119
e_CS25119 = e_CR+0.0026*35
CD0_CS25119 = C_D0_CR+0.0013*35
c_gradCS25119 = 4.8/100
# CS 25.121a
e_CS25121a = e_CR+0.0026*15
CD0_CS25121a = C_D0_CR+0.0013*15
c_gradCS25121a = 0.3/100
# CS 25.121b
e_CS25121b = e_CR+0.0026*15
CD0_CS25121b = C_D0_CR+0.0013*15
c_gradCS25121b = 3.6/100
# CS 25.121c
e_CS25121c = e_CR+0.0026*0
CD0_CS25121c = C_D0_CR+0.0013*0
c_gradCS25121c = 1.8/100
# CS 25.121d
e_CS25121d = e_CR+0.0026*35
CD0_CS25121d = C_D0_CR+0.0013*35
c_gradCS25121d = 3.15/100