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
   # 1) Masses with ADSEE I Book Method
   # 2) Masses with Regression Analysis
   # 3) Average Masses
# Print and Check Results

# Import Libraries:
import math
import os

os.system('cls')

# Constants:
from constants import *

def check_Mass_Fractions(f_OE, f_Fuel, f_payload):
   print("\nMessages:")
   if (f_OE > 0.6):
      print("Operational Empty Mass is way too high!")
   elif (0.5 <= f_OE <= 0.6):
      print("Fuel Mass is within the bounds of 50 and 60 percent.")
   elif (f_OE < 0.6):
      print("Operational Empty Mass is way too little!")

   if (f_Fuel > 0.3):
      print("Fuel Mass is way too high!")
   elif (0.2 <= f_Fuel <= 0.3):
      print("Fuel Mass is within the bounds of 20 and 30 percent.")
   elif (f_Fuel < 0.3):
      print("Fuel Mass is way too little!")

   if (f_payload > 0.3):
      print("Payload Mass is way too high!")
   elif (0.1 <= f_payload <= 0.3):
      print("Payload Mass is within the bounds of 10 and 30 percent.")
   elif (f_payload < 0.3):
      print("Payload Mass is way too little!")

def print_Results(OE, f_OE, payload, f_payload, Fuel, f_Fuel, MTOW):
   print("Operational Empty Mass:", OE, "kg -", f"{f_OE:.3f}")
   print("Design Payload Mass:", payload , "kg -", f"{f_payload:.3f}")
   print("Fuel Mass:", f"{Fuel:.3f}", "kg -", f"{f_Fuel:.3f}")
   print("Maximum Take-Off Weight:", f"{MTOW:.3f}", "kg")

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
from assumptions import *

# Parameters:
f_con = 0.05
V_CR = M * a_CR # m/
OE_Mass_avg = 21034 # kg
MTOW_avg = 36994 # kg

# Drag:
#Moved to assumptions.py

# Thrust:
TSFC = 22 * BR**(-0.19) 
eta_j = V_CR / (TSFC * E_spec)

# Mass estimation:
R_lost = 1/0.7 * L_over_D_CR * (alt_CR + V_CR**2/(2*g)) # m
R_nom_zero = ZeroPayload_R
R_nom_design = Design_R
R_eq_zero = (R_nom_zero + R_lost) * (1 + f_con) + 1.2 * R_div + t_E * V_CR
R_eq_design = (R_nom_design + R_lost) * (1 + f_con) + 1.2 * R_div + t_E * V_CR
R_aux_zero = R_eq_zero - R_nom_zero
R_aux_design = R_eq_design - R_nom_design

# 1) Masses with ADSEE Method:
print("1) Masses with ADSEE I Book Method:")
OE_Mass = maxMTOW_payload * (euler**((max_MTOW_R+R_aux_design)/(eta_j * L_over_D_CR * E_spec * 10**6/g))-1) / ((euler**((ZeroPayload_R+R_aux_zero)/(eta_j * L_over_D_CR * E_spec * 10**6/g))-euler**((max_MTOW_R+R_aux_design)/(eta_j * L_over_D_CR * E_spec * 10**6/g))))
Fuel_Mass = OE_Mass * (euler**((max_MTOW_R+R_aux_design)/(eta_j * L_over_D_CR * E_spec * 10**6/g))-1) + max_payload*(euler**((max_MTOW_R+R_aux_design)/(eta_j * L_over_D_CR * E_spec * 10**6/g)))
MTOW = maxMTOW_payload + Fuel_Mass + OE_Mass

# Mass Fractions:
f_FuelMass = Fuel_Mass / MTOW
f_OEMass = OE_Mass / MTOW
f_payload = maxMTOW_payload / MTOW

# Print and Check Results:
print_Results(OE_Mass, f_OEMass, maxMTOW_payload, f_payload, Fuel_Mass, f_FuelMass, MTOW)
check_Mass_Fractions(f_OEMass, f_FuelMass, f_payload)


# 2) Masses with Regression Analysis:
print("\n2) Regression Analysis:")
MTOW_reg = 2.6154 * maxMTOW_payload + 12273
OE_Mass_reg = 1.8508 * maxMTOW_payload + 3846.9
Fuel_Mass_reg = MTOW_reg - (maxMTOW_payload + OE_Mass_reg)

# Mass Fractions:
f_OE_reg = OE_Mass_reg / MTOW_reg
f_Fuel_reg = Fuel_Mass_reg / MTOW_reg
f_payload_reg = maxMTOW_payload / MTOW_reg

# Print and Check Results:
print_Results(OE_Mass_reg, f_OE_reg, maxMTOW_payload, f_payload_reg, Fuel_Mass_reg, f_Fuel_reg, MTOW_reg)
check_Mass_Fractions(f_OE_reg, f_Fuel_reg, f_payload_reg)


# 3) Average Masses:
print("\n3) Average Masses:")
Fuel_Mass_avg = MTOW_avg - (maxMTOW_payload + OE_Mass_avg)

# Mass Fractions:
f_OE_avg = OE_Mass_avg / MTOW_avg
f_Fuel_avg = Fuel_Mass_avg / MTOW_avg
f_payload_avg = maxMTOW_payload / MTOW_avg

# Print and Check Results:
print_Results(OE_Mass_avg, f_OE_avg, maxMTOW_payload, f_payload_avg, Fuel_Mass_avg, f_Fuel_avg, MTOW_avg)
check_Mass_Fractions(f_OE_avg, f_Fuel_avg, f_payload_avg)
