import os
import math
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from scipy.interpolate import interp1d
from wp4.get_distribution import f_L,f_D,f_M,f_W

'''Distributions'''
lift_distribution = f_L
weight_distribution = f_W
drag_distribution = f_D
moment_distribution = f_M

'''Constants'''
n_max = 3.65
n_min = -1.5
g = 9.81
q = 0.5 * (169.19688 ** 2)

'''alpha calculations'''
def a(V,h,n):
    W = 36994*9.81
    S = 85.75
    T_0 = 288.15
    g_0 = 9.80665
    p_0 = 101325
    h_0 = 0
    R = 287
    rho_0 = 1.225
    e = 2.718281828
    if h <=11000:
        T = -0.0065*(h-h_0) + T_0
        p = (p_0)*(T/T_0)**(-g_0/(-0.0065*R))
        rho = p/(R*T)
        p_rel = p/p_0*100
        rho_rel = rho/rho_0*100
        T_c = T - 273.15
    elif h <=20000:
        h1 = 11000
        T1 = -0.0065*(h1-h_0) + T_0
        T = T1
        p = ((p_0)*(T1/T_0)**(-g_0/(-0.0065*R)))*(e**(-g_0*(h-h1)/(R*T)))
        rho = p/(R*T)
    elif h <= 32000:
        h1 = 11000
        h2 = 20000
        T1 = -0.0065*(h1-h_0) + T_0
        T = 0.001*(h-h2) + T1
        p = ((p_0)*(T1/T_0)**(-g_0/(-0.0065*R)))*(e**(-g_0*(h2-h1)/(R*T1)))*((T/T1)**(-g_0/(0.001*R)))
        rho = p/(R*T)
    elif h <= 47000:
        h1 = 11000
        h2 = 20000
        h3 = 32000
        T1 = -0.0065*(h1-h_0) + T_0
        T2 = 0.001*(h3-h2) + T1
        T = 0.0028*(h-h3) + T2
        p = ((p_0)*(T1/T_0)**(-g_0/(-0.0065*R)))*(e**(-g_0*(h2-h1)/(R*T1)))*((T2/T1)**(-g_0/(0.001*R)))*((T/T2)**(-g_0/(0.0028*R)))
        rho = p/(R*T)
    elif h <= 51000:
        h1 = 11000
        h2 = 20000
        h3 = 32000
        h4 = 47000
        T1 = -0.0065*(h1-h_0) + T_0
        T2 = 0.001*(h3-h2) + T1
        T = 0.0028*(h4-h3) + T2
        p = ((p_0)*(T1/T_0)**(-g_0/(-0.0065*R)))*(e**(-g_0*(h2-h1)/(R*T1)))*((T2/T1)**(-g_0/(0.001*R)))*((T/T2)**(-g_0/(0.0028*R)))*(e**(-g_0*(h-h4)/(R*T)))
        rho = p/(R*T)
    elif h <= 71000:
        h1 = 11000
        h2 = 20000
        h3 = 32000
        h4 = 47000
        h5 = 51000
        T1 = -0.0065*(h1-h_0) + T_0
        T2 = 0.001*(h3-h2) + T1
        T3 = 0.0028*(h4-h3) + T2
        T = -0.0028*(h-h5) + T3
        p = ((p_0)*(T1/T_0)**(-g_0/(-0.0065*R)))*(e**(-g_0*(h2-h1)/(R*T1)))*((T2/T1)**(-g_0/(0.001*R)))*((T3/T2)**(-g_0/(0.0028*R)))*(e**(-g_0*(h5-h4)/(R*T3)))*((T/T3)**(-g_0/(-0.0028*R)))
        rho = p/(R*T)
    elif h <= 86000:
        h1 = 11000
        h2 = 20000
        h3 = 32000
        h4 = 47000
        h5 = 51000
        h6 = 71000
        T1 = -0.0065*(h1-h_0) + T_0
        T2 = 0.001*(h3-h2) + T1
        T3 = 0.0028*(h4-h3) + T2
        T4 = -0.0028*(h6-h5) + T3
        T = -0.002*(h-h6) +T4
        p = ((p_0)*(T1/T_0)**(-g_0/(-0.0065*R)))*(e**(-g_0*(h2-h1)/(R*T1)))*((T2/T1)**(-g_0/(0.001*R)))*((T3/T2)**(-g_0/(0.0028*R)))*(e**(-g_0*(h5-h4)/(R*T3)))*((T4/T3)**(-g_0/(-0.0028*R)))*((T/T4)**(-g_0/(-0.002*R)))
        rho = p/(R*T)
    C_l = 2*n*W/(rho*(V**2)*S)
    return C_l    

C_l_1 = a(169.19688,0,3.75) # Top right corner MTOW Sea level
C_l_2 = a(112.82,0,3.75) # Top left corner MTOW Sea level
C_l_3 = a(127.12,0,-1.5) # Bottom right MTOW Sea level
C_l_4 = a(71.36,0,-1.5) # Bottom left MTOW Sea Level

print(C_l_1,C_l_2,C_l_3,C_l_4)

import os
import numpy as np

os.system('cls')

# Define the angles of attack (AoA) and corresponding center of pressure positions
angles_of_attack = np.array([0.000, 1.000, 3.000, 4.000, 5.000, 6.000, 7.000, 8.000, 
                              9.000, 10.000, 11.000, 12.000, 13.000, 14.000, 15.000])
center_of_pressure = np.array([0.3085, 0.2823, 0.2651, 0.2602, 0.2510, 0.2472, 0.2448, 
                                0.2421, 0.2419, 0.2411, 0.2403, 0.2388, 0.2375, 0.2347, 0.2276])

# Create the interpolation function
def get_center_of_pressure(angle):
    """
    Returns the center of pressure for a given angle of attack
    using interpolation.

    Parameters:
    angle (float): Angle of attack in degrees.

    Returns:
    float: Center of pressure corresponding to the given angle of attack.
    """
    # Create an interpolating function
    interpolating_function = interp1d(angles_of_attack, center_of_pressure, kind='linear', fill_value="extrapolate")
    
    # Return the interpolated value
    return interpolating_function(angle)


        
