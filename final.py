"""
Mubinjon Satymov
Phys 4150
Final Project
Numerical Approach to find Phonon Drag in free standing 2D material(MoS2),
embedded in a microcavity.
"""
import numpy as np
import scipy.constants as cons
import matplotlib.pyplot as plt

#Constants:
Mp=(7e-5)*cons.electron_mass #Effictive mass of polariton
s=4      #Degenaracy factor of polariton
Ti=300 #Intial temprature
Tf=270 #Final  temrature
deltaT= np.linspace(1,300) #delta T
theta=2*np.pi
beta=cons.electron_mass*cons.Boltzmann
n=1e+14   #Concentration of polaritons
p1=cons.hbar*np.sqrt(np.pi*n) #polariton momentum upper limit
tdebye=262.3   #Debye temprature for MoS2
wdebye=(cons.Boltzmann*tdebye)/(cons.hbar) #Debye cutoff frequency for MoS2
k=3.5 #Thermal Conductivity for MoS2 3.5 W/mK at room temperature
p2=(cons.hbar*wdebye)/4 #phonon momentum upper limit
q=p2
M=3.12  #hydrostatic deformation potential in eV
cs=7.93*10**3 # speed of sound in MoS2
constants=(2*np.pi*(s**2))/(4*(cons.hbar**2)*Mp*beta*deltaT)

           
#First intergral  Trapezoidal method of integration
def f(x):   #qdq
    return x*(k)*2*np.pi #no dependence on angle, result*2pi
N = 10000
h = (q-0)/N
s = 0.5*f(0) + 0.5*f(q)
for k in range(1,N):
    s += f(0+k*h)
First=s

#Second integral using Simpson's Rule     
def simps(f,a,b,N): 
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S


Second=simps(lambda x : x,0,p1,1000)*2*np.pi #p1dp1
Third=simps(lambda x : x,0,p1,1000)*2*np.pi*M #p2dp2

psi=np.random.random(1)    #Random distribution function of quasiparticles
omega=np.random.random(1)  #Random distribution function of quasiparticles
sinh=1
epsilon_prime=cs*(np.sqrt(Second**2+First**2+2*Second*First*np.cos(np.pi/10))-Second)


#Turning sine hyperbolis into exponential
exp=epsilon_prime/(2*deltaT*cons.Boltzmann)

sigma=psi*omega/(sinh)                 
alpha=constants*First*Second*Third*M

beta=alpha*sigma
plt.semilogy(deltaT,beta)
plt.title('Graph T vs Drag')
plt.xlabel('Temp in K')
plt.ylabel('Semilog Scale of Phonon Drag')
plt.show()