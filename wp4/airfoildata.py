'''For a given position in the airfoil, spar length is given for c=1'''
import os
import math
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

import csv

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

def sparlength(x_input):
    upper, lower = read_airfoil_data("wp4\A220.csv")
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
    

