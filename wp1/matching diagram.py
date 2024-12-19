import os
import math
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

import math
import matplotlib.pyplot as plt
import numpy as np
from constants import *


def getAlphaT(WS, p, T, rho, C_L, cruise=False):
    #Velocity and mach
    if cruise==True:
        V2 = V_CR
        M2 = M
    else:
        V2 = math.sqrt(WS*2/rho/C_L)
        M2 = V2/math.sqrt(gamma*R*T)

    #Local variables
    Tt = T*(1+(gamma-1)/gamma*M2**2)
    thetaT = Tt/T_0

    pT = p*(1+(gamma-1)/gamma*M2**2)**(gamma/(gamma-1))
    deltaT = pT/p_0
  

    if BR > 0 and BR < 5 and thetaT < 1.07:
        alphaT= deltaT
    elif BR >= 5 and BR < 10 and thetaT >= 1.07:
        alphaT = deltaT*(1-2.1*(thetaT-1.07)/thetaT)
    elif BR >= 5 and BR <15 and thetaT < 1.07:
        alphaT = deltaT*(1-(0.43+0.014*BR)*math.sqrt(M2))
    elif BR >= 5 and BR < 15 and thetaT >= 1.07:
        alphaT = deltaT*(1-(0.43+0.014*BR)*math.sqrt(M2)-3*(thetaT-1.07)/(1.5+M2))
    else: print("Error in alphaT, check BR and thetaT")

    return alphaT

loadings = np.linspace(1/1000, 1, 1000)
loadings_without0 = np.arange(1500, 9000, 10)


#Landing limited
landing_field_length_ws= 1/beta_L*landing_field_length*rho_L*C_L_L/2/C_LFL
landing_field_length = [landing_field_length_ws for i in range(len(loadings))]

#Approach speed
speed_approach_ws = (V_app/1.23)**2*rho_L*C_L_L/2/beta_L
speeed_approach_list = [speed_approach_ws for i in range(len(loadings))]

#Cruise wing loading
cruise = np.zeros(len(loadings_without0))
for i in range(len(loadings_without0)):
    WS = loadings_without0[i]
    cruise[i] = beta_cr/getAlphaT(WS, p_CR, T_CR, rho_CR, C_L_CR, cruise=True)*(C_D0_CR*0.5*rho_CR*V_CR**2/(beta_cr*WS)+beta_cr*WS/(math.pi*AR*e_CR*0.5*rho_CR*V_CR**2))
    # cruise[i] = cruisef(getAlphaT(WS, p_CR, T_CR, rho_CR, C_L_CR, cruise=True), e_CR, beta_cr, C_L_CR, WS)


#Take off
kT = 0.85 #Not much clue, should check this out
takeoff = np.zeros(len(loadings_without0))
for i in range(len(loadings_without0)):
    WS = loadings_without0[i]
    takeoff[i] = 1.15*getAlphaT(WS, p_TO, T_TO, rho_TO, C_L_TO)*math.sqrt(WS/(L_TO*kT*rho_TO*g*math.pi*AR*e_TO))+4*h2/L_TO

# Climb gradient
def climbgradient(oswald, beta,engines,C_L, c_Grad):
    result = np.zeros(len(loadings_without0))
    for i in range(len(loadings_without0)):
        WS = loadings_without0[i]
        result[i] = 2/engines*beta/getAlphaT(WS, p_TO, T_TO, rho_TO, C_L)*(c_Grad+2*C_L/(math.pi*10*oswald))
    return result

def designPoint(WS, oswald, beta, engines, C_L, c_Grad):
    return 2/engines*beta/getAlphaT(WS, p_TO, T_TO, rho_TO, C_L)*(c_Grad+2*C_L/(math.pi*10*oswald))

climbgradient_CS25119 = climbgradient(oswald=e_CS25119,beta=beta_cl,engines=2,C_L=C_L_L, c_Grad=c_gradCS25119)
climbgradient_CS25121a = climbgradient(oswald=e_CS25121a,beta=beta_cl,engines=1,C_L=C_L_TO, c_Grad=c_gradCS25121a)
climbgradient_CS25121b = climbgradient(oswald=e_CS25121b,beta=beta_cl,engines=1,C_L=C_L_TO, c_Grad=c_gradCS25121b)
climbgradient_CS25121c = climbgradient(oswald=e_CS25121c,beta=beta_cl,engines=1,C_L=C_L_CR, c_Grad=c_gradCS25121c)
climbgradient_CS25121d = climbgradient(oswald=e_CS25121d,beta=beta_cl,engines=1,C_L=C_L_L, c_Grad=c_gradCS25121d)

ans = designPoint(WS=landing_field_length_ws, oswald=e_CS25121d,beta=beta_cl,engines=1,C_L=C_L_L, c_Grad=c_gradCS25121d)
# Climb rate
climbrate = np.zeros(len(loadings_without0))
for i in range(len(loadings_without0)):
    WS = loadings_without0[i]
    climbrate[i] = beta_cl/getAlphaT(WS,p_cl, T_cl, rho_cl, C_L_TO)*math.sqrt((CR**2*rho_cl/(beta_cl*WS*2)*math.sqrt(C_D0_TO*pi*AR*e_TO)+4*C_D0_TO/(pi*AR*e_TO)))
# OEI
climbrateOEI = np.zeros(len(loadings_without0))
# for i in range(len(loadings_without0)):
#     WS = loadings_without0[i]
#     climbrateOEI[i] = 2*beta_cl/getAlphaT(WS,p_TO, T_TO, rho_TO, C_L_TO)*math.sqrt((CR**2*rho_cl/(beta_cl*WS*2)*math.sqrt(C_D0_TO*pi*AR*e_TO)+4*C_D0_TO/(pi*AR*e_TO)))
#Plot
plt.title("Matching Diagram")
plt.xlabel("W/S -[N/m2]")
plt.ylabel("T/W - [N/N]")
plt.plot(speeed_approach_list, loadings)
plt.plot(landing_field_length, loadings )
plt.plot(loadings_without0,cruise)
plt.plot(loadings_without0,takeoff)
plt.plot(loadings_without0,climbgradient_CS25119)
plt.plot(loadings_without0,climbgradient_CS25121a)
plt.plot(loadings_without0,climbgradient_CS25121b)
plt.plot(loadings_without0,climbgradient_CS25121c)
plt.plot(loadings_without0,climbgradient_CS25121d)
plt.plot(loadings_without0,climbrate)
plt.plot(landing_field_length_ws, ans, 'ro')

#Design Points
plt.plot(4855.1, 0.35801, marker='o')
plt.plot(5058.8, 0.34359, marker='o')
plt.plot(4585.4, 0.37871, marker='o')
plt.plot(5288.6, 0.34307, marker='o')
plt.plot(3785.3, 0.3036, marker='o')
plt.plot(4111.5, 0.2703, marker='o')
plt.plot(4806.2, 0.3044, marker='o')
plt.plot(4975.0,0.38192, marker='o')
plt.title("Matching Diagram", fontsize=14)

print(ans)
print(landing_field_length_ws)
# plt.plot(loadings_without0,climbrateOEI)
plt.legend([
    "Approach Speed", 
    "Landing Field Length", 
    "Cruise", 
    "Take Off Field Length", 
    "Climb Gradient CS25.119", 
    "Climb Gradient CS25.121A", 
    "Climb Gradient CS25.121B", 
    "Climb Gradient CS25.121C", 
    "Climb Gradient CS25.121D", 
    "Climb Rate", 
    "Design Point", 
    "DP Embraer E170", 
    "DP Embraer E175", 
    "DP CRJ700", 
    "DP CRJ900", 
    "DP F28-2000", 
    "DP F28-3000", 
    "DP MRJ70", 
    "DP ARJ21 700"
], loc='upper right', fontsize=13)

plt.show()

