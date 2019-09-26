"""
Mubinjon Satymov

Exercise 3.2: Curve plotting
a)  Make a plot of the so-called deltoid curve, which is defined parametrically 
by the equations, x = 2 cos θ + cos 2θ, y = 2 sin θ − sin 2θ, where 0 ≤ θ < 2π. 
Take a set of values of θ between zero and 2π and calculate x and y for each 
from the equations above, then plot y as a function of x.

b)  Taking this approach a step further, one can make a polar plot r = f(θ) 
for some function f by calculating r for a range of values of θ and then 
converting r and θ to Cartesian coordinates using the standard equations 
x = r cos θ, y = r sin θ. Use this method to make a plot of the Galilean 
spiral, r=θ2 for 0 ≤ θ ≤ 10π.

c)  Using the same method, make a polar plot of “Fey’s function”
r = (exp^(cos(theta))-2*cos(4*theta)+sin^5(theta/12) 
in the range 0 ≤ θ ≤ 24π.
"""
#Part a:
import numpy as np
import matplotlib.pyplot as plt
a=np.linspace(0,2*np.pi,num=100) #Creating evenly spaced set of numbers
x=2*np.cos(a)+np.cos(2*a)
y=2*np.sin(a)-np.sin(2*a)
plt.plot(x,y)
plt.show()

#Part b:
a=np.linspace(0,10*np.pi,num=10000) #More set of numbers creates smoother graph
r=a**2
x1=r*np.cos(a)
y1=r*np.sin(a)
plt.plot(x1,y1)
plt.show()

#Part c:
a=np.linspace(0,24*np.pi,num=100000)
r=(np.exp(np.cos(a)))-2*np.cos(4*a)+(np.sin(a/12))**5
x2=r*np.cos(a)
y2=r*np.sin(a)
plt.plot(x2,y2)
plt.show()

#All plots in one screen
f,axes=plt.subplots(1,3,figsize=(18,6))
axes[0].plot(x,y)                    #[0] indicates possition of the 1st plot  
axes[0].set_title('Graph of Part a') #Setting title to the plot
axes[1].plot(x1,y1)                  #[1] indicates possition of the 2nd plot 
axes[1].set_title('Galilean spiral') #Setting title to the plot
axes[2].plot(x2,y2)                  #[2] indicates possition of the 3rd plot 
axes[2].set_title('Fey’s function')  #Setting title to the plot