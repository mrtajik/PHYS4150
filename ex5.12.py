"""
Mubinjon Satymov

Exercise 5.12: The Stefan–Boltzmann constant
"""
import scipy.constants as cons
import mpmath as math
import numpy as np
def f(x):
    z=np.tan(x)
    der=(math.exp(z))-1
    f=((z**3)*((math.sec(x))**2))/(der)
    return f
N =1000
a =1e-14
b = np.pi/2
h = (b-a)/N
s = 0.5*f(a) + 0.5*f(b)
for k in range(1,N):
    s += f(a+k*h)
integral=h*s
dem=4*(np.pi**2)*(cons.c**2)*(cons.hbar**3)
sigma=(cons.k**4)*integral/dem
print("\nPart B:")
print("Evaluating given integral using Trapezoid Method of integration")
print("To avoid infinity of upper limit of integrand we converted our function")
print("into tan function with limits from 0 to pi/2")
print("Evaluated value of Sigma =",sigma)

print("\nPart C:")
p=((cons.sigma-sigma)/sigma)*100
print("Percentage difference between two Sigmas=",p)
print("This percentage error very small, so we can say that our Sigmas")
print("are the same.")

