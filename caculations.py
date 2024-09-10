import math
import matplotlib.pyplot as plt
import numpy as np
from assumptions import *
from constants import *
from tlars import *



loadings = np.linspace(1/1000, 1, 1000)
loadings_without0 = np.arange(1500, 9000, 100)
cl_landing = 2.6

#Landing limited
landing_field_length_ws= landing_field_length*1.225*cl_landing/0.94/2/0.45

speed_approach = 70
speed_approach_ws = (speed_approach/1.23)**2*1.225*2.6/0.94/2

#Cruise wing loading
cruise_ws =[((0.95/0.19548)*(((0.0232*0.5*0.37597*(0.77*296.71**2))/(0.95*i))
                             +((0.95*i)/(math.pi*8*0.802*0.5*0.37597*(0.77*296.71**2))))) for i in loadings_without0]




speeed_approach_list = [speed_approach_ws for i in range(len(loadings))]
landing_field_length_list = [landing_field_length_ws for i in range(len(loadings))]




#Take off
def getAlphaT(WS):
    #Velocity and mach

    V2 = math.sqrt(WS*2/rho_TO/C_L_TO)
    M = V2/math.sqrt(gamma*R*T_TO)

    #Local variables
    Tt = T_TO*(1+(gamma-1)/gamma*M**2)
    thetaT = Tt/T_0

    pT = p_TO*(1+(gamma-1)/2*M**2)**(gamma/(gamma-1))
    deltaT = pT/p_0
    if BR > 0 and BR < 5 and thetaT < 1.07:
        alphaT= deltaT
    elif BR >= 5 and BR < 10 and thetaT >= 1.07:
        alphaT = deltaT*(1-2.1*(thetaT-1.07)/thetaT)
    elif BR >= 5 and BR <15 and thetaT < 1.07:
        alphaT = deltaT*(1-(0.43+0.014*BR)*math.sqrt(M))
    elif BR >= 5 and BR < 15 and thetaT >= 1.07:
        alphaT = deltaT*(1-(0.43+0.014*BR)*math.sqrt(M)-3*(thetaT-1.07)/(1.5+M))
    else: print("Error in alphaT, check BR and thetaT")

    return alphaT

kT = 0.85 
take = np.zeros(len(loadings_without0))
for i in range(len(loadings_without0)):
    WS = loadings_without0[i]
    take[i] = 1.15*getAlphaT(WS)*math.sqrt(WS/(L_TO*kT*rho_TO*g*math.pi*AR*e_TO))


def calculations(TOP,loading):
    result = [i/(TOP*1*1.9) for i in loading]
    return result
    #assume sea level takeofftakeoff
    # taken from raymer

#Plot
plt.title("Matching Diagram")
plt.xlabel("W/S -[N/m2]")
plt.ylabel("T/W - [N/N]")
plt.plot(speeed_approach_list, loadings)
plt.plot(landing_field_length_list, loadings )
plt.plot(loadings_without0,cruise_ws)

plt.plot(loadings_without0,take)
plt.legend(["Approach Speed", "Landing Field Length", "Cruise", "Field length limited Take Off "])
plt.show()