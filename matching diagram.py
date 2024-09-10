import math
import matplotlib.pyplot as plt
import numpy as np
from assumptions import *
from constants import *
from tlars import *

def getAlphaT(WS, p, T, rho, C_L):
    #Velocity and mach
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
loadings_without0 = np.arange(1500, 9000, 100)


#Landing limited
landing_field_length_ws= 1/beta_L*landing_field_length*rho_L*C_L_L/2/C_LFL
landing_field_length = [landing_field_length_ws for i in range(len(loadings))]

#Approach speed
speed_approach_ws = (V_app/1.23)**2*rho_L*C_L_L//2
speeed_approach_list = [speed_approach_ws for i in range(len(loadings))]

#Cruise wing loading
cruise = np.zeros(len(loadings_without0))
for i in range(len(loadings_without0)):
    WS = loadings_without0[i]
    cruise[i] = beta_cr/getAlphaT(WS, p_CR, T_CR, rho_CR, C_L_CR)*(C_D0_CR*0.5*rho_CR*V_CR**2/(beta_cr*WS)+beta_cr*WS/(math.pi*AR*e_CR*0.5*rho_CR*V_CR**2))
    


#Take off
kT = 0.85 #Not much clue, should check this out
takeoff = np.zeros(len(loadings_without0))
for i in range(len(loadings_without0)):
    WS = loadings_without0[i]
    takeoff[i] = 1.15*getAlphaT(WS, p_TO, T_TO, rho_TO, C_L_TO)*math.sqrt(WS/(L_TO*kT*rho_TO*g*math.pi*AR*e_TO))+4*h2/L_TO

# Climb gradient
def climbgradient(oswald, beta,engines,C_L):
    result = np.zeros(len(loadings_without0))
    for i in range(len(loadings_without0)):
        WS = loadings_without0[i]
        V = math.sqrt(WS*2/rho_TO/C_L_TO)
        result[i] = 2/engines*beta/getAlphaT(WS, p_TO, T_TO, rho_TO, C_L)*(CR/V+2*C_L/(math.pi*10*oswald))
    return result

climbgradient_takeoff = climbgradient(oswald=e_TO,beta=beta_cl,engines=2,C_L=C_L_TO)
climbgradient_takeoff_1OEI = climbgradient(oswald=e_TO,beta=beta_cl,engines=1,C_L=C_L_TO)
climbgradient_cruise = climbgradient(oswald=e_CR,beta=beta_cr,engines=2,C_L=C_L_CR)
climbgradient_cruise_1OEI = climbgradient(oswald=e_CR,beta=beta_cr,engines=1,C_L=C_L_CR)
climbgradient_landing = climbgradient(oswald=e_L,beta=beta_L,engines=2,C_L=C_L_L)
climbgradient_landing_1OEI = climbgradient(oswald=e_L,beta=beta_L,engines=1,C_L=C_L_L)

# Climb rate
climbrate = np.zeros(len(loadings_without0))
for i in range(len(loadings_without0)):
    WS = loadings_without0[i]
    climbrate[i] = beta_cl/getAlphaT(WS,p_TO, T_TO, rho_TO, C_L_TO)*math.sqrt((CR**2*rho_TO/(beta_cl*WS*2)*math.sqrt(C_D0_TO*pi*AR*e_TO)+4*C_D0_TO/(pi*AR*e_TO)))


#Plot
plt.title("Matching Diagram")
plt.xlabel("W/S -[N/m2]")
plt.ylabel("T/W - [N/N]")
plt.plot(speeed_approach_list, loadings)
plt.plot(landing_field_length, loadings )
plt.plot(loadings_without0,cruise)
plt.plot(loadings_without0,takeoff)
plt.plot(loadings_without0,climbgradient_takeoff)
plt.plot(loadings_without0,climbgradient_takeoff_1OEI)
plt.plot(loadings_without0,climbgradient_cruise)
plt.plot(loadings_without0,climbgradient_cruise_1OEI)
plt.plot(loadings_without0,climbgradient_landing)
plt.plot(loadings_without0,climbgradient_landing_1OEI)
plt.plot(loadings_without0,climbrate)
plt.legend(["Approach Speed", "Landing Field Length", "Cruise", "Take Off Field Length", "Climb Gradient Takeoff", "Climb Gradient Takeoff OEI", "Climb Gradient Cruise", "Climb Gradient Cruise OEI", "Climb Gradient Landing", "Climb Gradient Landing OEI", "Climb Rate"])
plt.show()
