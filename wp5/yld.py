import os
import math
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)
from constants import *
import wp4.areaMoments as am
import wp4.deflections as defl

import numpy as np
from matplotlib import pyplot as plt

def yieldCalc(M, I, D):
    # Calculate the yield stress   
    return M * D / I


def safetyFactor(sigma_y, sigmaYield):
    # Calculate the safety factor
    return sigmaYield / sigma_y

D_total= am.D_total
h1 = am.h1
Dneg = (D_total-h1)
Ixx1 = am.Ixx1



M = defl.M
M2 = defl.M2



# plt.subplot(1, 2, 1)
# plt.plot(np.linspace(0,29.28/2, 146), yieldCalc(M, Ixx1, D_total), label="[n=3.75]", color='orange')
# plt.plot(np.linspace(0,29.28/2, 146), yieldCalc(M2, Ixx1, Dneg), label="[n=-1]", color='red')
# plt.xlabel("Span-Wise position [m]", fontsize=12)
# plt.ylabel("Tensile stress", fontsize=12)
# plt.legend()



# plt.subplot(1, 2, 2)
# plt.plot(np.linspace(0,29.28/2, 146), safetyFactor(yieldCalc(M, Ixx1, D_total),450*10**6), label="[n=3.75]", color='blue')
# plt.plot(np.linspace(0,29.28/2, 146), safetyFactor(yieldCalc(M2, Ixx1, Dneg),450*10**6), label="[n=-1]", color='red')
# plt.xlabel("Span-Wise position [m]", fontsize=12)
# plt.ylabel("Safety Factor", fontsize=12)
# plt.ylim(0,15)
# plt.legend()


# plt.tight_layout()
# plt.show()