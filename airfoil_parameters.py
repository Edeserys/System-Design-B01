"""Airfoil Selection"""
# Import Libraries
# Calculate thickness-to-chord ratio boundaries

# Import Libraries:
import math
import WP1
import os

os.system('cls')

# Constants:
g = WP1.g
gamma = WP1.gamma

# Aircraft Parameters:
M_CR = WP1.M
C_L_CR_max = WP1.C_L_CR
C_f_avg = WP1.CF_Equi
MTOW = WP1.MTOW_avg # kg
V = WP1.V_CR # m/s
p_CR = 23842.3 # Pa
rho_CR = 0.3796 # kg/m^3

# Wing Parameters:
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

# Loading and Mass Parameters:
W_TO_over_S_w = 5684.396 # N/m^2
f_landing_mass = 0.7533 # 0% fuel left
f_mass_begin_CR = f_landing_mass + (1-f_landing_mass) * 0.91 # 91% fuel left
f_mass_end_CR = f_landing_mass + (1-f_landing_mass) * 0.05 # 5% fuel left

# Airfoil Selection Constraints
# 1) Thickness-to-Chord Ratio:
print("Thickness-to-Chord Ratio: ")
C_L_alpha_0 = 2/(1.4 * p_CR * M_CR**2) * W_TO_over_S_w
t_over_c_max_formula = (math.cos(sweep_c_over_2)**3 * (0.935 - (M_CR + 0.03) * math.cos(sweep_c_over_2)) - 0.115 * C_L_alpha_0**1.5)/(math.cos(sweep_c_over_2)**2) # <=
print("Constraint 1: ", t_over_c_max_formula)
t_over_c_max_graph = 0.28
print(t_over_c_max_graph)
t_over_c_min = 0.09
print(t_over_c_min)

t_over_c_max = min(t_over_c_max_formula, t_over_c_max_graph)
print(t_over_c_max)

q = 1/2 * rho_CR * V**2
C_L_des = 1.1 / q * (1/2 * (MTOW*f_mass_begin_CR*g / S_w + MTOW*f_mass_end_CR*g / S_w))
print(C_L_des)

C_l_des = q * C_L_des / (1/2*rho_CR*(V*math.cos(sweep_c_over_4))**2)
print(C_l_des)
