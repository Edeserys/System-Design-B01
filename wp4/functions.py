'''Modules'''
from scipy import integrate
import scipy as sp
from distributions import *
from main import *
import math
import matplotlib as plt

'''Functions'''
# Distributed Load
taper_ratio = 0.314
c_root = 4.450
w = n * (lift_distribution * math.cos(a) + drag_distribution* math.sin(a))  + weight_distribution * (n-1) * g






