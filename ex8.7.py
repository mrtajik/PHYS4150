"""
Mubinjon Satymov
Phys 4150
Exercise 8.7: Trajectory with air resistance
"""
import numpy as np 
import matplotlib.pyplot as plt
g = 9.81
R = 0.08  # m
theta_0 = 30 * np.pi / 180  # radians
v_0 = 100                # m/s
rho = 1.22               # kg/m^3
C = 0.47                 # drag coefficient
t0 = 0
tf = 7
N = 10000
h = (tf - t0) / N
c = np.pi * R ** 2 * rho * C / 2
def c_any(m):
    return c / m

def f(r, t, m):
    vx = r[1]
    vy = r[3]
    v = np.sqrt(vx ** 2 + vy ** 2)
    return np.array([vx, - c_any(m) * vx * v,
                  vy, -g - c_any(m) * vy * v], float)


tpoints = np.arange(t0, tf, h)


def path(m):
    xpoints = []
    ypoints = []
    r = np.array([0, v_0 * np.cos(theta_0), 0, v_0 * np.sin(theta_0)], float) #Creating 2D Array;
    for t in tpoints:        #4th order Runge Kutta method;
        xpoints.append(r[0])
        ypoints.append(r[2])
        k1 = h * f(r, t, m)
        k2 = h * f(r + 0.5 * k1, t + 0.5 * h, m)
        k3 = h * f(r + 0.5 * k2, t + 0.5 * h, m)
        k4 = h * f(r + k3, t + h, m)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return np.array(xpoints, float), np.array(ypoints, float)

#Passing different masses to function Path(m)
x1, y1 = path(1)
x2, y2 = path(2)
x3, y3 = path(4)
plt.plot(x1,y1, 'blue')
plt.plot(x2,y2, 'black')
plt.plot(x3,y3, 'green')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('')
plt.show()