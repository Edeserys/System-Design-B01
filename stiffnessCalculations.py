from constants import *
import numpy as np
import scipy as sp
from scipy import interpolate


def q(x):
    return x
def d(x):
    return np.sqrt(2-x**2)
def h(x):
    return q(x)/(c*d(x))
c = 10
estimate1,error1 = sp.integrate.quad(h,0,1)
estimate2,error2 = sp.integrate.quad(lambda x: q(x)/(c*d(x)),0,1)