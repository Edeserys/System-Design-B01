"""Landing Gear Sizing"""
# Import Libraries
# Clear Console
# Constants
# Methods
# Parameters
# Number of Main Gear Struts
# Wheel Pressure
    # 1) Inflation Pressure
    # 2) Static Loads
        # 8% on Nose Gear
        # 92% on Main Gear
# Print Tires' Dimensions

# Import Libraries:
import os
import constants as WP1
import numpy as np
import random

# Clear Console:
os.system('cls')

# Constants:
g = WP1.g # m/s^2

# Parameters:
MTOM = WP1.MTOW_avg # kg
MTOW = g * MTOM # N
N_mw = np.ceil(MTOW/120000 /4) * 4 # Number of Main Gear Wheels 
N_nw = 2 # Number of Nose Gear Wheels
LCN = 62 # Load Classification Number for tarmac

# Number of Main Gear Struts:
N_str = 0
if N_mw <= 12:
    N_str = 2
else:
    rnd = random.randint(0,1) # In theory it is not random, but this case will not be investigated
    if rnd == 0:
        N_str = 3
    else:
        N_str = 4

# Wheel Pressure:
# 1) Inflation Pressure:
p = 430*np.log(LCN) - 680 
# 2) Static Loads:
p_nw = 0.08 * MTOM/N_nw # 8%*p on Nose Gear 
p_mw = 0.92 * MTOM/N_mw # 92%*p on Main Gears

# Print Tires' Dimensions based on Inflation Pressure and Static Load:
print(f"Mean Wheels: \n1) Inflation Pressure: {p} kPa \n2) Static Load: {p_mw} kg/cm^2")
print(f"3) Tire Diametre = 0.9144 m, Tire Width = 0.254 m\n")
print(f"Nose Wheels: \n1) Inflation Pressure: {p} kPa \n2) Static Load: {p_nw} kg/cm^2")
print(f"3) Tire Diametre = 0.4572 m, Tire Width = 0.1080 m")
