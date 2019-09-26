"""
Mubinjon Satymov

Exercise 2.4
    
A spaceship travels from Earth in a straight line at relativistic speed v to 
another planet x light years away. Write a program to ask the user for the 
value of x and the speed v as a fraction of the speed of light c, then print 
out the time in years that the spaceship takes to reach its destination (a) in 
the rest frame of an observer on Earth and (b) as perceived by a passenger on 
board the ship. Use your program to calculate the answers for a planet 10 light
years away with v = 0.99c..

Solution:
Part a:For observer on Earth we use:
    t=x/v; where 
    x-How far planet X  away in light years;
    v=Relativistic speed of a spaceship;

Part b: For a passenger on board the ship we use:
    t0=(t)*((1-v^2)^(0.5)); where 
    t-time dialation; 
    t=x/v;  
    x=10; 
    v=0.99;
"""
#Part a
import numpy as np
x=float(input("How far planet X  away in light years= "))
v=float(input("Relativistic speed of a spaceship v= "))
t=x/v
print("For observer on Earth spaceship would reach planet X in {:.2f} light years".format(t))

#Part b 
x=10  #distance
v=.99 #speed
t=x/v
t0=t*(np.sqrt(1-(v**2)))
print("Passenger on board ship would reach planet X in {:.2f} light years".format(t0))