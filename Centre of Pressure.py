import os
import numpy as np
from scipy.interpolate import interp1d

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

print(get_center_of_pressure(12.5))
