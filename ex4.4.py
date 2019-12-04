"""
Mubinjon Satymov

Exercise 4.4: Calculating integrals

     I=sqrt(1-x^2)dx
     where lower limit=-1 and upper limit=1
     
a)  Write a program to evaluate the integral above with N = 100 and compare the
result with the exact value. The two will not agree very well, because N = 100 
is not a sufficiently large number of slices.

b)  Increase the value of N to get a more accurate value for the integral. If 
we require that the program runs in about one second or less, how accurate a 
value can you get?

Solution:
    We will use the Riemann definition of the integral:
        I=lim(Sum(h*yk));
        where
        k=1 to N;
        N approaches infinity;
        yk=sqrt(1-xk^2);
        xk=-1+h*k;
        
Q/A: By increasing the number(N) of rectangles we get less error in evaluation
of integral. However we should remember that bigger "N" can take some to 
evaluate.        
"""        
#Part a)
import numpy as np
def f(x):     #defining function sqrt(1-x^2);
    f=np.sqrt(1-(x**2))
    return f
a=-1; b=1    #limits of the integral;
N=100        #Number of rectangles under the curve;
h=(a-b)/N    #Width of the rectangles;
I=0
for i in range(N):    #loop to calculate all area of all rectangles;
    I=f(b+h*i)*h +I
    i=i+1
print("Part A:\nValue of Integral when N=100, I=",abs(I))

#Part b)
N=10000      #Number of rectangles;
h=(a-b)/N    #Width of the rectangles;
I=0
for i in range(N):    #loop to calculate all area of all rectangles;
    I=f(b+h*i)*h +I
    i=i+1
err=abs(((abs(I)-(np.pi/2))/(np.pi/2))*100)
print("\nPart B:\nValue of Integral when N=10000 I=",abs(I),"\nAccuracy % Error {:.4f}".format(err))