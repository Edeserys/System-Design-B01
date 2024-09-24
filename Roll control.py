import math
import matplotlib.pyplot as plt
import numpy as np
from SYSTEM-Design-B01.WP1.mass_estimation import *
from constants.constants import *





c_lda = (c_root/2*y_aileronend**2 - (c_root*(1-taper_ratio)*y_aileronend**3)/(3*b/2)- (c_root/2*y_aileronstart**2 - (c_root*(1-taper_ratio)*y_aileronstart**3)/(3*b/2)))*(2*C_la*tau)/(S_ref*b)

c_lp = -(4*(C_la +C_D0_CR))/(S_ref*b**2)* (c_root/3*(b/2)**3 - (c_root*(1-taper_ratio)*(b/2)**4)/(4*b/2))

P = -(c_lda)/(c_lp)*da_max*(2*V_CR/b)

dt = bank_angle/P

print(dt)
