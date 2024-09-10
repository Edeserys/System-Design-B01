import math
import matplotlib.pyplot as plt
import numpy as np



loadings = np.linspace(1/1000, 1, 1000)
loadings_without0 = np.arange(1500, 9000, 100)
cl_landing = 2.6

landing_field_length= 1210 #m
landing_field_length_ws= landing_field_length*1.225*cl_landing/0.94/2/0.45

speed_approach = 70
speed_approach_ws = (speed_approach/1.23)**2*1.225*2.6/0.94/2








take_off_ws = [(1.15*(((101325*(1+0.2*(((((0.95*j*2/0.60776/(((1/1.13)**2)*1.9))**0.5)/(1.4*287*(288.15))))))**(1.4/0.4)/101000)*
                       (1-(0.43+0.014*7)*(((((0.95*j*2/0.60776/(((1/1.13)**2)*1.9))**0.5)/(1.4*287*(288.15))**0.5))**0.5))))
                *((j)/(1296*9.81*3.141592*5*0.841*1.225*0.85))**0.5+4*11/1296) for j in loadings_without0]

speeed_approach_list = [speed_approach_ws for i in range(len(loadings))]
landing_field_length_list = [landing_field_length_ws for i in range(len(loadings))]
plt.title("Matching Diagram")
plt.xlabel("W/S -[N/m2]")
plt.ylabel("T/W - [N/N]")

oswald = 0.87
c_dividedby_v = 0.024
c_l=1.9
c_d_0 = c_l**2/(math.pi/10/oswald)


rho_TO = 1.225
C_L_TO = 1.9
T_TO = 288.15
p_0 = 101325
BR = 7
T_0 = 288.15
p_TO = 101325
gamma = 1.4
R = 287
WS = loadings_without0

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




def climbgradient(alpha, delta_f, oswald, c_d_0, c_dividedby_v,beta,deployed,engines,cl):
    new_oswald =oswald+.0026*delta_f
    new_c_d_0 = c_d_0+0.0013*delta_f+0.0175*(deployed)

    result = 2/engines*beta/alpha*(c_dividedby_v+2*cl/(math.pi*10*new_oswald))

    return result

def cruise(alpha, oswald,beta,cl,ws):
    result = beta/alpha*(((cl**2)/(math.pi*10*oswald)*(0.5*0.379597*(0.77*296.71)**2)/(beta*ws)+(ws*beta)/(math.pi*10*oswald*0.5*0.379597*(0.77*296.71)**2)))
    return result
loading_list = []
cruise_list = []

for i in range(75):
    loading = 1500+100*i
    value = cruise(getAlphaT(loading),0.85,0.95,1.7,loading)
    loading_list.append(loading)
    cruise_list.append(value)
plt.plot(loading_list,cruise_list)


loading_list = []
climbgradient_list = []



for j in range(1):
    for r in range(2):
        for i in range(75):
            loading = 1500+100*i
            value=climbgradient(getAlphaT(loading),35,0.85,c_d_0,c_dividedby_v,0.94,r,(j+2),2.6)
            loading_list.append(loading)
            climbgradient_list.append(value)

        plt.plot(loading_list,climbgradient_list)
        loading_list.clear()
        climbgradient_list.clear()

for j in range(1):
    for r in range(2):
        for i in range(75):
            loading = 1500+100*i
            value=climbgradient(getAlphaT(loading),15,0.85,c_d_0,c_dividedby_v,0.94,r,(j+2),1.9)
            loading_list.append(loading)
            climbgradient_list.append(value)

        plt.plot(loading_list,climbgradient_list)
        loading_list.clear()
        climbgradient_list.clear()

for j in range(1):
    for r in range(2):
        for i in range(75):
            loading = 1500+100*i
            value=climbgradient(getAlphaT(loading),35,0.85,c_d_0,c_dividedby_v,1,r,(j+2),1.7)
            loading_list.append(loading)
            climbgradient_list.append(value)

        plt.plot(loading_list,climbgradient_list)
        loading_list.clear()
        climbgradient_list.clear()
#given data
CR = 7.62       #climb rate
h = 7315.2      #altitude req
DELTAT = 0
beta = 0.95
CD0 = 0.018
e = 0.8
AR = 10         #aspect ratio
Tsl = 288       #sea level temp
a = -0.0065     #alt lapse rate
Psl = 101325    #sea level pressure
R = 287
g = 9.80065
gamma = 1.4
B = 7


#calculate standard values
T = Tsl + a*h
P = Psl*pow((1+a*h/Tsl), (-g/a/R))
rho = P/R/T
Cl = math.sqrt(CD0*math.pi*AR*e)          #lift coefficient

WPtab = []
WStab = []

for i in range(75):
    WS = 1500+(i)*100
    V = math.sqrt(WS*2/rho/Cl)           #speed
    m = V/math.sqrt(gamma*R*T)
    Pt = P*pow((1+(gamma-1)/2*(m**2)),(gamma/(gamma-1)))
    deltat = Pt/Psl
    alphat = deltat * (1 - (0.43+0.014*B)*math.sqrt(m))
    WP = (beta/alphat)*(math.sqrt(CR*2*rho*Cl/beta/WS/2)+2*math.sqrt(CD0/math.pi/AR/e))
    WStab.append(WS)
    WPtab.append(WP)

print(T, P, Cl, rho, Pt)
plt.plot(WStab, WPtab)
plt.title('Climb rate requirement diagram')





plt.plot(speeed_approach_list, loadings)
plt.plot(landing_field_length_list, loadings )

plt.plot(loadings_without0,take_off_ws)


plt.show()