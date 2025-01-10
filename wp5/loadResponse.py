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

import wp5.stress as stress
import wp5.buckling as buckling
import cases

def safetyFactor(sigma_app, sigmaCrit):
    # Calculate the safety factor
    safe_sigma_app = np.where(sigma_app == 0, 1, sigma_app)
    return np.abs(sigmaCrit/(np.where(sigma_app == 0, 1, sigma_app)))

sparDistances = am.sparDistancesResult

t,c = cases.casesWP4(0)

E = 72.4 *10**9
stress_buckling1= stress.stressM(defl.V, defl.T, defl.M, am.Ixx1, am.J1, am.h1, t, am.L)
stress_buckling2= stress.stressM(defl.V2, defl.T2, defl.M2, am.Ixx1, am.J1, am.h1, t, am.L)

'''Buckling'''
skin_stress1 = stress.equivalentStress(stress_buckling1[0], stress_buckling1[1])
skin_stress2 = stress.equivalentStress(stress_buckling2[0], stress_buckling2[1])

web_stress1 = stress.stressM(defl.V, defl.T, defl.M, am.Ixx1, am.J1, am.h1, t, am.L, False)[1]
web_stress2 = stress.stressM(defl.V2, defl.T2, defl.M2, am.Ixx1, am.J1, am.h1, t, am.L, False)[1]

column_stress1 = np.abs(stress.stressM(defl.V, defl.T, defl.M, am.Ixx1, am.J1, am.h1, t, am.L, False)[0])
column_stress2 = np.abs(stress.stressM(defl.V2, defl.T2, defl.M2, am.Ixx1, am.J1, am.h1, t, am.L, False)[0])



skin_buckling= buckling.skinBuckling(buckling.k_s, E, t, buckling.L_skin)

web_buckling= buckling.skinBuckling(buckling.k_s, E, t, am.h1)

column_buckling= buckling.columnBuckling(.0002, 4, E, sparDistances, 500*10**-6)

safetySkin = safetyFactor(skin_stress1, skin_buckling)
safetySkin2 = safetyFactor(skin_stress2, skin_buckling)

safetyWeb = safetyFactor(web_stress1, web_buckling)
safetyWeb2 = safetyFactor(web_stress2, web_buckling)

safetyColumn = safetyFactor(column_stress1, column_buckling)
safetyColumn2 = safetyFactor(column_stress2, column_buckling)


'''Tension'''
sigma_eq1 = stress.equivalentStress(stress_buckling1[0], stress_buckling1[1])
sigma_eq2 = stress.equivalentStress(stress_buckling2[0], stress_buckling2[1])


# [n=3.75]
plt.plot(np.linspace(0,29.28/2, 146), skin_stress2, label="Skin Stress", color='blue')
plt.plot(np.linspace(0,29.28/2, 146), web_stress2, label="Web Stress", color='green')
plt.plot(np.linspace(0,29.28/2, 146), column_stress2, label="Column Stress", color='red')
plt.ylabel("Stress [Pa]", fontsize=12)
plt.xlabel("Span-Wise position [m]", fontsize=12)
plt.legend()
plt.show()

plt.plot(np.linspace(0,29.28/2, 146), safetySkin2, label="Skin Safety Factor", color='blue')
plt.plot(np.linspace(0,29.28/2, 146), safetyWeb2, label="Web Safety Factor", color='green')
plt.plot(np.linspace(0,29.28/2, 146), safetyColumn2, label="Column Safety Factor", color='red')
plt.plot(np.linspace(0,29.28/2, 146), [1]*146, label="Safety Margin", color='orange')
plt.ylabel("Safety Factor", fontsize=12)
plt.xlabel("Span-Wise position [m]", fontsize=12)
plt.ylim(0,30)
plt.legend()
plt.show()




# plt.subplot(1, 2, 1)
# plt.plot(np.linspace(0,29.28/2, 146), sigma_eq2, label="Yield Stress", color='blue')
# plt.xlabel("Span-Wise position [m]", fontsize=12)
# plt.ylabel("Tensile stress", fontsize=12)
# plt.legend()
# plt.show()


# # plt.subplot(1, 2, 2)
# plt.plot(np.linspace(0,29.28/2, 146), safetyFactor(sigma_eq2,450*10**6), label="Yield Safety Factor", color='blue')
# plt.plot(np.linspace(0,29.28/2, 146), [1]*146, label="Safety Margin", color='orange')
# plt.xlabel("Span-Wise position [m]", fontsize=12)
# plt.ylabel("Safety Factor", fontsize=12)
# plt.ylim(0,15)
# plt.legend()


# plt.tight_layout()
# plt.show()