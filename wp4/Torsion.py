import scipy as sp
from scipy.interpolate import interp1d
import math
from scipy import integrate
from distributions import *
from matplotlib import pyplot as plt
import csv
from constants import *
L = b/2 #probably not correct but should be half wingspan idk what that is tho
case = 1 # We can change the case to be inspected by increasing the number
x = 0
wplot = []
vplot = []
mplot = []
tplot = []
xplot = []

if case == 0:
    n = 1
    a = 7.998*math.pi/180
    V = 169.19688
    rho = 1.225
elif case == 1:
    n = -1
    a = -9.971*math.pi/180
    V = 127.12
    rho = 1.225

q = 0.5* V**2 *rho

'''Functions'''
# Distributed Load

taper_ratio = 0.314
c_root = 4.450


def d(x,a):
    c = get_center_of_pressure(a)
    d = (0.5-c)*(c_root - c_root*(1-taper_ratio)*(x/L))
    return d

def h(x): #moment coefficent plus normal coefficient times quarter chord
    h = (-1.0*n*( lift_distribution(x) * math.cos(a) + drag_distribution(x)* math.sin(a))*0.25 + moment_distribution(x)) * ((c_root - c_root*(1-taper_ratio)*(x/L))**2)*q
    return h

T_x1, error = sp.integrate.quad(h,0,2.5428)
T_x2, error = sp.integrate.quad(h,2.5428,10.12)
T_x3, error = sp.integrate.quad(h,10.14,L)
T_x = T_x1 + T_x2 + T_x3

def t(x):
    if x < 2.5428:
        estimate_t, error_t = sp.integrate.quad(h,0,x)
        T = 1.0 * estimate_t - T_x
    elif x < 10.13:
        estimate_t, error_t = sp.integrate.quad(h,2.5428,x)
        T = 1.0 * estimate_t + T_x1 - T_x
    elif x < L:
        estimate_t, error_t = sp.integrate.quad(h,10.13,x)
        T = 1.0 * estimate_t + T_x1 + T_x2 - T_x
    return T

for i in range(146):
    T_val = t(x) 
    tplot.append(T_val)
    xplot.append(x)
    x = x + 0.1

plt.plot(xplot,tplot,'c-')
plt.ylabel("Torsion [Nm]")
plt.xlabel("z[m]")
plt.show()

with open("Torque.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["x", "T[Nm]"])  # Header
    for i in range(len(xplot)):
        writer.writerow([xplot[i], tplot[i] if i < len(tplot) else ""])
