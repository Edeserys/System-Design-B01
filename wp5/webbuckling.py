import numpy as np
import matplotlib.pyplot as plt
import csv
import math

def read_airfoil_data(filename):
    upper = {}
    lower = {}
    with open(filename, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            x = float(row[0])
            y = float(row[1])
            if y >= 0:
                if x in upper:
                    upper[x].append(y)
                else:
                    upper[x] = [y]
            else:
                if x in lower:
                    lower[x].append(y)
                else:
                    lower[x] = [y]
    return upper, lower

def read_Torque_data(filename):
    with open(filename, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        T = []
        for row in reader:
            T.append(float(row[1]))

    return np.array(T)

def sparlength(x_input):
    upper, lower = read_airfoil_data('A220.csv')
    if x_input < .1 or x_input > .85:
        return "Error: X position out of bounds. Please enter a value between 0.1 and 0.85."
    try:
        closest_x_upper = min([k for k in upper.keys() if k >= x_input], key=lambda k: k - x_input, default=None)
        closest_x_lower = min([k for k in lower.keys() if k >= x_input], key=lambda k: k - x_input, default=None)
        if closest_x_upper is not None and closest_x_lower is not None:
            y_values_upper = upper[closest_x_upper]
            y_values_lower = lower[closest_x_lower]
            upper = max(y_values_upper)
            lower = min(y_values_lower)
        else:
            print("Error: Could not find closest X positions.")
        return upper - lower
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


T1 = read_Torque_data('TorquePos.csv')       #read data for positive torque
T2 = read_Torque_data ('TorqueNeg.csv')     #read data for negative torque
V = read_Torque_data ('shearforce.csv')     #read data for shear force   
As = read_Torque_data('As.csv')             #read data for enclosed area

# Parameters 
ks = 9.5        # Stiffness parameter
E = 72.4e9      # Elastic modulus (Pa)
nu = 0.33       # Poisson's ratio
t = 0.008       # Thickness (m)
kv = 1.5        # factor relating maximum to average shear stress
t_r = 0.008     # rear spar thickness
t_f = 0.008     # front spar thickness
case = 1       # we select the torque case, 1 being positive, 2 being negative
sp1 = 0.2       # percentage of chord position of front spar
sp2 = 0.7       # percentage of chord position of rear spar

h1c = sparlength(sp1)       
h2c = sparlength(sp2)


ch = -0.2045*np.linspace(0,29.28/2, 146)+4.45   
h_f = h1c*ch                     # Front spar height 
h_r = h2c*ch                     # Rear spar height
b = h_f

#torque based on the case
if case==1:
    T = T1
if case==2:
    T = T2
# Critical stress calculation
tau_cr = (math.pi**2 * ks * E) / (12 * (1 - nu**2)) * (t / b)**2


# average shear stress calculation
tau_ave = V / (h_f * t_f + t_r * h_r)

# maximum stress calculation
tau_big = kv * tau_ave
tau_max = tau_big + T/(2*As)        #include shear flow due to torsion

print (tau_cr)
print (tau_max)
