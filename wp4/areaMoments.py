import os
import math
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)


import numpy as np
import matplotlib.pyplot as plt
from math import pi
from wp4.airfoildata import *
from cases import *

'''Definition of Geometry'''
# Define the given functions
A= 500*10**-6 #Area of stringer
sp1 = 0.2
sp2 = 0.7

t, c = casesWP4(0) #Thickness and chord length



'''Data Processing'''
h1c = sparlength(sp1)
h2c = sparlength(sp2)


ch = -0.2045*np.linspace(0,29.28/2, 146)+4.45
L = (sp2-sp1)*ch # Base length
h1 = h1c*ch #Big height 
h2 = h2c*ch #Small heigh
D = ((h1-h2)*L/2*((h1-h2)/3+h2) + L*h2**2*0.5 )/(L*h2+0.5*L*(h1-h2)) #Distance from centerline for the outer Area

theta= np.arctan(L/(h1-h2)) 


gamma= h1-h2-t/(np.tan((theta/2)))+t/(np.tan(pi/2-theta/2))
alpha= h2-t-t/np.tan(pi/2-theta/2)

D2 =( 0.5*gamma*(L-2*t)*(gamma/3+alpha) +0.5*(L-2*t)*alpha**2) /((L-2*t)*alpha + 0.5*gamma*(L-2*t))




S = h1+h2+L+np.sqrt((h1-h2)**2+L**2) #length of circulation
As = L*h2+1/2*L*(h1-h2)


A1= L*h2+0.5*L*(h1-h2)
A2= (L-2*t)*alpha + gamma * (L-2*t) * 0.5 
D_total=(D*A1-D2*A2)/(A1-A2)


def Ixx(h1,h2,L,t):
    '''2nd Moment of Area around X axis'''
      

    Ixxxr =  L*1/12*h2**3 + (L*(h2)* (D-h2/2)**2 ) + L*(h1-h2)**3/36 + (0.5*L*(h1-h2))*(D-(h1-2/3*h2))**2 
    - (   (L-2*t)*alpha**3/12 +  alpha * (L-2*t)* (D2-alpha/2)**2 + (L-2*t)/36*gamma**3 + 0.5*gamma*(L-2*t) * (D2-(alpha+gamma/3))**2 )


        
    Ibottomst= c/2*A*D_total**2

    dtop = 0
    for i in range(int(c/2)):
        dtop =+ h2-D_total+i*(h1-h2)*2/c
        Itopst = A*dtop**2

    return Ixxxr + Ibottomst + Itopst



'''Polar Moment of Area for a single cell'''
def J(h1,h2,L,t):
    '''Polar moment using thin wall approximation, provided constant thickness, the line integral becomes s/t'''


    As = 1/2*(h1-h2)*L+h2*L #Enclosed area of a trapezoid

    s = h1+h2+L+np.sqrt((h1-h2)**2+L**2) #Perimeter of the trapezoid: 3 sides + diagonal

    A1= L*h2+0.5*L*(h1-h2)
    A2= (L-2*t)*alpha + gamma * (L-2*t) * 0.5 
    D_total=(D*A1-D2*A2)/(A1-A2)
        
    Ibottomst= c/2*A*D_total**2

    dtop = 0
    for i in range(int(c/2)):
        dtop =+ h2-D_total+i*(h1-h2)*2/c
        Itopst = A*dtop**2
    
    return 4*As**2/(s/t)+2*(Ibottomst+Itopst)

Ixx1 = Ixx(h1,h2,L,t)
J1 = J(h1,h2,L,t)

# # # Plot the functions
# # # plt.figure(figsize=(12, 8))
# # # plt.subplot(1, 2, 1)
# # # plt.title("Span wise 2nd Moment of Area around X axis")
# plt.plot(np.linspace(0,29.28/2, 146), Ixx(h1,h2,L,t), label="Ixx(y)")
# plt.xlabel("Span-Wise position [m]", fontsize=12)
# plt.ylabel("Ixx(y)", fontsize=12)
# plt.legend()

# plt.tight_layout()
# plt.show()
# # # plt.subplot(1, 2, 2)
# # # plt.title("Span wise 2nd Polar Moment of Area")
# plt.plot(np.linspace(0,29.28/2, 146), J(h1,h2,L,t), label="J(y)", color='orange')
# plt.xlabel("Span-Wise position [m]", fontsize=12)
# plt.ylabel("J(y)", fontsize=12)
# plt.legend()


# plt.tight_layout()
# plt.show()