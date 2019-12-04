"""
Mubinjon Satymov
Ex. 8.4 
Calculating the motion of a nonlinear pendulum.
Using Runge-Kutta method to solve ODE and animating the outcome plots.
"""
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

# Constants
g = 9.81
l = 0.1
theta0 = 179
omega0 = 0.0
t0=0.0
tmax=100
h = 1e-2

def f(r, t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = - (g / l) * np.sin(theta)
    return np.array([ftheta, fomega], float)


# Using fourth-order Runge-Kutta
tpoints = np.arange(t0, tmax, h)
points = []
# omegapoints = []
r = np.array([theta0, omega0], float)
for t in tpoints:
    points.append(r[0])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4) / 6

#Animating motion of the pendulum
fig = plt.figure(figsize=(5,5))
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))

pend = plt.Circle((0.1,0.1), 0.06, facecolor='red')

def init():
    pend.center = (0.1,0.1)
    ax.add_patch(pend)
    return pend,

def animate(i):
    x = l*np.cos(points[i]-90)
    y = l*np.sin(points[i]-90)
    pend.center = (x, y)
    return pend,

anim = animation.FuncAnimation(fig, animate,
init_func=init,frames=360,interval=20,blit=True)
anim.save('pendulum.mp4')
