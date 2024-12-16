import scipy as sp
import csv
from scipy.interpolate import interp1d
import math
from scipy import integrate
from distributions import *
from matplotlib import pyplot as plt
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
    n = 3.75
    a = 7.998*math.pi/180
    V = 169.19688
    rho = 1.225
elif case == 1:
    n = -1.5
    a = -9.971*math.pi/180
    V = 127.12
    rho = 1.225

q = 0.5* (V**2) *rho

'''Functions'''
# Distributed Load

taper_ratio = 0.314
c_root = 4.450

def w(x):
    return -1 * (c_root - c_root*(1-taper_ratio) * (x/L)) * q * (lift_distribution(x) * math.cos(a) + drag_distribution(x) * math.sin(a))  - weight_distribution(x)

R_y1, error = sp.integrate.quad(w,0,2.5428)
R_y2, error = sp.integrate.quad(w,2.5428,10.13)
R_y3, error = sp.integrate.quad(w,10.13,14.5)
R_y = R_y1 + R_y2 + R_y3

def V(x):
    if x < 2.5428:
        estimate_v, error_v = sp.integrate.quad(w,0,x)
        V = -1.0 * estimate_v + R_y
    elif x < 10.13:
        estimate_v, error_v = sp.integrate.quad(w,2.5428,x)
        V = -1.0 * (estimate_v + sp.integrate.quad(w,0,2.5428)[0]) + R_y
    elif x < L:
        estimate_v, error_v = sp.integrate.quad(w,10.13,x)
        V = -1.0 * (estimate_v + sp.integrate.quad(w,0,2.5428)[0] + sp.integrate.quad(w,2.5428,10.13)[0]) + R_y
    return V

M_z1, error = sp.integrate.quad(V,0,2.5428)
M_z2, error = sp.integrate.quad(V,2.5428,10.13)
M_z3, error = sp.integrate.quad(V,10.13,14.5)
M_z = M_z1 + M_z2 + M_z3

def M(x):
    if x < 2.5428:
        estimate_m, error_m = sp.integrate.quad(V,0,x)
        M = 1.0 * estimate_m - M_z
    elif x < 10.13:
        estimate_m, error_m = sp.integrate.quad(V,2.5428,x)
        M = 1.0 * estimate_m + sp.integrate.quad(V,0,2.5428)[0] - M_z
    elif x < L:
        estimate_m, error_m = sp.integrate.quad(V,10.13,x)
        M = 1.0 * estimate_m + sp.integrate.quad(V,0,2.5428)[0] + sp.integrate.quad(V,2.5428,10.13)[0] - M_z
    return M

for i in range(round(146)):
    smallw = w(x) 
    wplot.append(smallw)
    xplot.append(x)
    x = x + 0.1

x = 0

for i in range(146):
    V_val = V(x) 
    vplot.append(V_val)
    x = x + 0.1

x = 0

for i in range(146):
    M_val = M(x) 
    mplot.append(M_val)
    x = x + 0.1

with open("plot_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["x", "w [N/m]", "V [N]", "M [Nm]"])  # Header
    for i in range(len(xplot)):
        writer.writerow([xplot[i], wplot[i] if i < len(wplot) else "", vplot[i] if i < len(vplot) else "", mplot[i] if i < len(mplot) else ""])

plt.subplot(131)

plt.plot(xplot,wplot,'r-')
plt.ylabel("Distributed Load[N/m]")
plt.xlabel("z[m]")

plt.subplot(132)
plt.plot(xplot,vplot,'b-')
plt.ylabel("Shear Load[N]")
plt.xlabel("z[m]")
plt.subplot(133)
plt.plot(xplot,mplot,'g-')
plt.ylabel("Moment Load[Nm]")
plt.xlabel("z[m]")

plt.show()
