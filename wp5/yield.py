from wp4.areaMoments import *
from wp4.deflections import *
import numpy as np
from matplotlib import pyplot as plt

def yieldCalc(M, I, D):
    # Calculate the yield stress   
    return M * D / I



def safetyFactor(sigma_y, sigmaYield):
    # Calculate the safety factor
    return sigmaYield / sigma_y

D_total=(D*A1-D2*A2)/(A1-A2)

plt.subplot(1, 2, 1)
plt.title("SF")
plt.plot(np.linspace(0,29.28/2, 146), yieldCalc(M,Ixx(h1,h2,L,t), D_total), label="SF", color='orange')
plt.xlabel("Span-Wise position [m]", fontsize=12)
plt.ylabel("SigmaY", fontsize=12)
plt.legend()


plt.subplot(1, 2, 2)
plt.plot(np.linspace(0,29.28/2, 146), safetyFactor(yieldCalc(M,Ixx(h1,h2,L,t), D_total),450*10**6), label="SF", color='blue')
plt.xlabel("Span-Wise position [m]", fontsize=12)
plt.ylabel("SF", fontsize=12)
plt.ylim(0, 10)
plt.legend()


plt.tight_layout()
plt.show()