import numpy as np
import matplotlib.pyplot as plt
from  wp4.areaMoments import *
from constants import *





def read_Moment_data(filename):
    with open(filename, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        y = []
        M = []
        for row in reader:
            y.append(float(row[0]))
            M.append(float(row[3]))

    return np.array(y), np.array(M)

def read_Moment_data2(filename):
    with open(filename, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        y = []
        M = []
        for row in reader:
            y.append(float(row[0]))
            M.append(float(row[3]))

    return np.array(y), np.array(M)


def read_Torque_data(filename):
    with open(filename, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        T = []
        for row in reader:
            T.append(float(row[1]))

    return np.array(T)


Ixx1 = Ixx(h1, h2, L, t)
J1 = J(h1, h2, L, t)


y_vals, M = read_Moment_data('wp4/momentPos.csv')
y_vals, M2 = read_Moment_data2('wp4/momentNeg.csv')
T = read_Torque_data('wp4/TorquePos.csv')
T2 = read_Torque_data('wp4/TorqueNeg.csv')




# Deflection v'' and v'
def deflection(M, E, Ixx, dy):  
        deflection = [0]
        d1v = [0]
        d2v = M/(Ixx*E)
        for i in range(len(M)-1):
             d1v.append((d1v[i]+dy*d2v[i]))
        for i in range(len(M)-1):
             deflection.append((deflection[i]+dy*d1v[i]))
        return deflection

def twist(T, G, J1, dy):
    theta = [0]
    dtheta = -T/(G*J1)
    for i in range(len(M)-1):
        theta.append((theta[i]+dy*dtheta[i]))
    return np.array(theta)*180/np.pi

print(deflection(M, E, Ixx1, 29.28/2/146)[-1])
print(twist(M, E, Ixx1, 29.28/2/146)[-1])



# # # plt.subplot(1, 2, 1)
# # # plt.title("Deflection")
# plt.plot(np.linspace(0,29.28/2,146), deflection(M, E, Ixx1, 29.28/2/146), label="Deflection [n=3.75] down")
# plt.plot(np.linspace(0,29.28/2,146), deflection(M2, E, Ixx1, 29.28/2/146), label="Deflection [n=-1.5] down")
# plt.xlabel("Span-Wise position [m]", fontsize=12)
# plt.ylabel("Vertical deflection [m]", fontsize=12)
# plt.legend()

# plt.tight_layout()
# plt.show()
# # # plt.subplot(1, 2, 2)
# # # plt.title("Twist")
# plt.xlabel("Span-Wise position [m]", fontsize=12)
# plt.ylabel("Angular deflection [deg]", fontsize=12)
# plt.plot(np.linspace(0,29.28/2,146), twist(T, G, J1, 29.28/2/146), label="Twist [n=3.75] CW")
# plt.plot(np.linspace(0,29.28/2,146), twist(T2, G, J1, 29.28/2/146), label="Twist [n=-1.5] CW")
# plt.legend()

# plt.tight_layout()
# plt.show()

