import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

def stressM(V,T,M,I,J,h1,t,L, skin=True):
    # Calculate shear stress depending on skin or spar
    if skin == True:
        tauShear = V/I*h1/4*t*L/2
    else:
        tauShear = V/I*(h1/4*t*L/2+(h1**2*3/8*t))    
    
    tau = tauShear + (T/J)*h1/2 #shear contribution + torque
    
    sigma = M*h1/2/I

    return sigma, tau

def equivalentStress(sigma, tau):
    return ((sigma/2)**2 + tau**2)**0.5