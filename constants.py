''' Assumptions and other values provided in manual'''

import math


#Other constants
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
BR = 12 # Bypass Ratio [1-15]
Wetted_Area = 2000 # m^2
CF_Equi = 0.0031 # page 105
phi = 0.97 # page 106
psi = 0.0075 # page 106
E_spec = 44 # MJ/kg


t_E = 20 * 60 # s
R_div = 300 * 1000 # m

C_LFL = 0.45 # pg 133 landing field length coefficient



# Aerodynamic characteristics
C_D0_CR = 0.0156
e_CR = 0.727
L_over_D_CR = 1/2 * math.sqrt(pi * AR * e_CR / C_D0_CR)
c_dividedby_v = 0.024

# Sea Level
rho_0 = 1.225 # kg/m^3
T_0 = 288.15 # K
p_0 = 101325 # Pa

# Takeoff
delta_f = 24

C_D0_TO = C_D0_CR+0.0013*delta_f
e_TO = e_CR+.0026*delta_f
C_L_TO = 1.48
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
C_L_CR = 0.5745
T_CR = 218.808 # K, ISA 
a_CR = math.sqrt(gamma * R * T_CR)
V_CR = M * a_CR
p_CR = 23842
rho_CR = 0.3796

# Parameters:
f_con = 0.05
OE_Mass_avg = 21034 # kg
MTOW_avg = 36994 # kg

# Landing
delta_f = 40

C_D0_L = C_D0_CR+0.0013*delta_f
e_L = e_CR+.0026*delta_f


landing_field_length= 1210 #m
rho_L = rho_0
beta_L = 0.7533 # fuel mass fraction - loiter
C_L_L = 1.93
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

#Design points
EmbraerE170 = [4855.1, 0.35801]
EmbraerE175 = [5058.8, 0.34359]
CRJ700 = [4585.4, 0.37871]
CRJ900 = [5288.6, 0.34307]
F28_2000 = [3785.3, 0.3036]
F28_3000= [4111.5, 0.2703]
MRJ70 = [4806.2, 0.3044]
ARJ21_700 = [4975.0,0.38192]

# AC Design Point
WS = 5684.396
TW = 0.51929


# Roll control
bank_angle = 45
da_upmax = 24
da_downmax = 18
tau = 0.51
S_ref_ail = 1
b = 35.67
c_root = 5.419
taper_ratio = 0.316
C_la = 0.179
c_d0 = 0.00464

y_aileronstart =  0.8285*b/2
y_aileronend = 0.95*b/2
b_aileron = 2*(y_aileronend - y_aileronstart)
c_aileronavg = 0.3*(c_root*(1-(1-taper_ratio)*y_aileronend/(b/2))+c_root*(1-(1-taper_ratio)*y_aileronstart/(b/2)))/2
S_aileron = c_aileronavg*b_aileron
da_max = 0.5*(da_upmax+da_downmax)
