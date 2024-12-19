import os
import math
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

import math
import matplotlib.pyplot as plt
import numpy as np
from wp1.mass_estimation import *
from constants import *


c_root = C_R


c_lda = (c_root/2*y_aileronend**2 - (c_root*(1-taper_ratio)*y_aileronend**3)/(3*b/2)- (c_root/2*y_aileronstart**2 - (c_root*(1-taper_ratio)*y_aileronstart**3)/(3*b/2)))*(2*C_la*tau)/(S_ref_ail*b)

c_lp = -(4*(C_la +c_d0))/(S_ref_ail*b**2)* (c_root/3*(b/2)**3 - (c_root*(1-taper_ratio)*(b/2)**4)/(4*b/2))

P = -(c_lda)/(c_lp)*da_max*(2*V_CR/b)

dt = bank_angle/P

print('dt',dt)
print('Aileron start and end',y_aileronstart, y_aileronend)
print('Aileron span, chord and surface area',b_aileron,c_aileronavg,S_aileron)
