"""Airfoil Selection"""
# Import Libraries
# Import and Calculate Parameters:
    # 1) Aircraft Parameters
    # 2) Wing Parameters
    # 3) Loading and Mass Parameters
# Airfoil Selection Constraints Calculation:
    # 1) Mach Number (M)
    # 2) Reynolds Number (Re)
    # 3) Thickness-to-Chord Ratio (t/c)
    # 4) Airfoil Lift Design Coefficient (C_{l_{des}})
# Summary of Constraints

# Import Libraries:
import math
import WP1
import os

os.system('cls')

# Constants:
g = WP1.g
gamma = WP1.gamma
R = WP1.R

# Parameters:
# 1) Aircraft Parameters:
M_CR = WP1.M
C_L_CR_max = WP1.C_L_CR
C_f_avg = WP1.CF_Equi
MTOW = WP1.MTOW_avg # kg
V = WP1.V_CR # m/s

# 2) Wing Parameters:
b = 35.67 # m
c_r = 5.419 # m
taper_ratio = 0.316
c_t = c_r * taper_ratio # m
S_w = 127.2 # m^2
n = 0.50
m = 0.25
sweep_c_over_4_deg = 24 # degrees
sweep_c_over_4 = math.radians(24)
sweep_c_over_2 = math.atan(math.tan(sweep_c_over_4) - (4/WP1.AR)*((n - m) * (1 - taper_ratio)/(1 + taper_ratio)))
sweep_c_over_2_deg = math.degrees(sweep_c_over_2) 
sweep_LE = math.atan(math.tan(sweep_c_over_4)+c_r/(2*b)*(1-taper_ratio))
sweep_LE_deg = math.degrees(sweep_LE)
MAC = 3.887 # m

# 3) Loading and Mass Parameters:
W_TO_over_S_w = 5684.396 # N/m^2
f_landing_mass = 0.7533 # 0% fuel left
f_mass_begin_CR = f_landing_mass + (1-f_landing_mass) * 0.91 # 91% fuel left
f_mass_end_CR = f_landing_mass + (1-f_landing_mass) * 0.05 # 5% fuel left

# Airfoil Selection Constraints
print("Airfoil Selection Constraints:")
# 1) Mach Number:
print("1) Mach Number (M):")
print(f"Mach number at cruise: {M_CR}\n")


# 2) Reynolds Number:
print("2) Reynolds Number (Re):")

# Flow Paramters at 35,000 ft:
p_CR = 23842.3 # Pa
rho_CR = 0.3796 # kg/m^3
mu = 1.3885 * 10 **-5 # N.s/m^2
print(f"Dynamic Viscosity: {round(mu,8)} N.s/m^2")

# Reynolds Number:
c = MAC
Re = rho_CR * V * c / mu
#Re = rho_CR * 0.70343 * math.sqrt(gamma*R*218.81) * c / mu
print(f"Reynolds number: {round(Re/(10**6),3)} x 10^6\n")


# 3) Thickness-to-Chord Ratio:
print("3) Thickness-to-Chord Ratio (t/c):")

# Constraints from Formula:
C_L_alpha_0 = 2/(1.4 * p_CR * M_CR**2) * W_TO_over_S_w
t_over_c_max_formula = (math.cos(sweep_c_over_2)**3 * (0.935 - (M_CR + 0.03) * math.cos(sweep_c_over_2)) - 0.115 * C_L_alpha_0**1.5)/(math.cos(sweep_c_over_2)**2) # <=
print("Constraint 1: ", round(t_over_c_max_formula,3), " max")

# Constraints from Graphs in ADSEE I Reader:
t_over_c_max_graph = 0.28
print("Constraint 2: ", t_over_c_max_graph, " max")
t_over_c_min = 0.09
print("Constraint 3: ", t_over_c_min, " min\n")

# Final Result:
t_over_c_max = min(t_over_c_max_formula, t_over_c_max_graph)


# 4) Airfoil Design Lift Coefficient:
print("4) Airfoild Design Lift Coefficient (C_{l_{des}}):")
q = 1/2 * rho_CR * V**2 # Pa

# Wing Coefficient:
C_L_des = 1.1 / q * (1/2 * (MTOW*f_mass_begin_CR*g / S_w + MTOW*f_mass_end_CR*g / S_w)) 
print("Step 1: Design Lift Wing Coefficient", round(C_L_des,4))

# Airfoil Coefficient:
C_l_des = C_L_des / (math.cos(sweep_LE)**2)
print("Step 2: Design Lift Airfoil Coefficient", round(C_l_des,3), "\n")


# Summary:
print("Constraints:")
print(f"1. M = {M_CR}")
print(f"2. Re = {round(Re/(10**6),3)} x 10^6")
print(f"3. {t_over_c_min} <= t/c <= {t_over_c_max}")
print("4. C_{l_{des}} =", f"{round(C_l_des,3)}")
