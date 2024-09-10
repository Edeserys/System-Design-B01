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


cruise_ws =[((0.95/0.19548)*(((0.0232*0.5*0.37597*(0.77*296.71**2))/(0.95*i))
                             +((0.95*i)/(math.pi*8*0.802*0.5*0.37597*(0.77*296.71**2))))) for i in loadings_without0]
print(cruise_ws)

take_off_ws = [(1.15*(((101325*(1+0.2*(((((0.95*j*2/0.60776/(((1/1.13)**2)*1.9))**0.5)/(1.4*287*(288.15))))))**(1.4/0.4)/101000)*
                       (1-(0.43+0.014*7)*(((((0.95*j*2/0.60776/(((1/1.13)**2)*1.9))**0.5)/(1.4*287*(288.15))**0.5))**0.5))))
                *((j)/(1296*9.81*3.141592*5*0.841*1.225*0.85))**0.5+4*11/1296) for j in loadings_without0]

speeed_approach_list = [speed_approach_ws for i in range(len(loadings))]
landing_field_length_list = [landing_field_length_ws for i in range(len(loadings))]
plt.title("Matching Diagram")
plt.xlabel("W/S -[N/m2]")
plt.ylabel("T/W - [N/N]")
take = [1.15*0.19548*math.sqrt(i/(1296*0.85*1.225*9.81*math.pi*10*0.87))
        for i in loadings_without0]
def calculations(TOP,loading):
    result = [i/(TOP*1*1.9) for i in loading]
    return result
    #assume sea level takeofftakeoff
    # taken from raymer
print(calculations(100,loadings_without0))
plt.plot(speeed_approach_list, loadings)
plt.plot(landing_field_length_list, loadings )
plt.plot(loadings_without0,cruise_ws)
plt.plot(loadings_without0,take_off_ws)
print(take)
plt.plot(loadings_without0,take)

plt.show()