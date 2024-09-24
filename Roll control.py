import math
import matplotlib.pyplot as plt
import numpy as np
from assumptions import *
from constants import *
from tlars import *
from mass estimation import *

c_aileron = 0.528
b_aileron = 3.567
y_aileronstart =  0.75*b/2
y_aileronend = y_aileronstart + b_aileron
da_max = 0.5*(da_upmax+da_downmax)


c_lda = (c_root/2*y_aileronend**2 - (c_root*(1-taper_ratio)*y_aileronend**3)/(3*b/2)- (c_root/2*y_aileronstart**2 - (c_root*(1-taper_ratio)*y_aileronstart**3)/(3*b/2)))*(2*C_la*tau)/(S_ref*b)

c_lp = -(4*(C_la +C_D0_CR))/(S_ref*b**2)* (c_root/3*(b/2)**3 - (c_root*(1-taper_ratio)*(b/2)**4)/(4*b/2))

P = -(c_lda)/(c_lp)*da_max*(2*V_CR/b)

dt = bank_angle/P

print(dt)
