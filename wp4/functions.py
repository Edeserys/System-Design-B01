import os
import math
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

'''Modules'''
from scipy import integrate
import scipy as sp
from wp4.distributions import *
from wp4.main import *
import math
import matplotlib as plt

'''Functions'''
# Distributed Load
taper_ratio = 0.314
c_root = 4.450
w = n * (lift_distribution * math.cos(a) + drag_distribution* math.sin(a))  + weight_distribution * (n-1) * g






