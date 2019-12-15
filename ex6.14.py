"""
Mubinjon Satymov
Exercise 6.14: Linear and Nonlinear Equations

"""
import numpy as np
import scipy.constants as const
import matplotlib.pyplot as plt

E = np.linspace(0.05, 19.95, 100)
w = 1e-9  # width of quantum well in nm
V = 20    # well depth in eV
num = ((w ** 2)*((const.electron_mass)))/const.electron_volt
dem=(2*((const.hbar/const.electron_volt)**2))
c=num/dem
accuracy = 0.001  


def f(e):  #First function
    return np.tan(np.sqrt(c * e))


def g(e):  #Second function
    return np.sqrt((V - e) / e)


def h(e):  #Third function
    return (-np.sqrt(e / (V - e)))

y1 = f(E)
y2 = g(E)
y3 = h(E)
plt.plot(E,y1,E,y2,E,y3)
plt.title("Graph of the Functions Part A")
plt.show()

#Bisection Method
def f1(x):
    return f(x) - g(x)


def f2(x):
    return f(x) - h(x)


def roots(f, x1, x2, accuracy):

    def midpoint(x, y):
        return (x + y) / 2

    def sign(x, y):
        if (x < 0 and y < 0) or (x > 0 and y > 0):
            return True
        else:
            return False
        
    while abs(x1 - x2) > accuracy:
        x = midpoint(x1, x2)
        if sign(f(x1), f(x)):
            x1 = x
        elif sign(f(x), f(x2)):
            x2 = x
        elif abs(x) < accuracy:
            return x
    
    return midpoint(x1, x2)

plt.plot(E, y1, 'o',E, y2, 'ko',E, y3, 'ro')
plt.title("Graph of the Bisection Method")
plt.show()


print("Different Energy(in eV) levels with accuracy of 0.001 eV")
print('E0 = ', roots(f1, 0.02, 0.75, accuracy))
print('E1 = ', roots(f2, 1, 1.5, accuracy))
print('E2 = ', roots(f1, 2.5, 4.5, accuracy))
print('E3 = ', roots(f2, 5, 6, accuracy))
print('E4 = ', roots(f1, 7.5, 9, accuracy))
print('E5 = ', roots(f2, 10, 12, accuracy))


f,axes=plt.subplots(1,2,figsize=(12,4))
axes[0].plot(E, y1,E, y2,E, y3)        
axes[0].set_title('Graph of Part A')  
axes[1].plot(E, y1, 'o',E, y2, 'ko',E, y3, 'ro') 
axes[1].set_title('Graph of the Bisectional Method')
plt.show()