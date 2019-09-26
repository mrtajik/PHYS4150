"""
Mubinjon Satymov

Exercise 2.1
 
Another ball dropped from a tower a ball is dropped from a tower of height h 
with initial velocity zero. Write a program that asks the user to enter the 
height in meters of the tower and then calculates and prints the time the ball 
takes until it hits the ground, ignoring air resistance. Use your program to 
calculate the time for a ball dropped from a 100 m high tower.

Solution:
General formula to calculate:
    s=0.5*g*(t^2)
    To calculate time we use t=((2*s)/(g))^(0.5)
"""
import numpy as np
import scipy.constants as const
import astropy.units as unit
g=const.g                           #declaring constant "g" in SI
s=float(input("Enter hight of the building: "))                    
t=(np.sqrt((2*s)/(g)))              #Calculating value of "t"
t1=t*unit.s                         #Adding SI unit(second) to value of t
print("It takes {:.2f} until the ball hits the ground".format(t1))
#For H=100 we just enter value of H to our program