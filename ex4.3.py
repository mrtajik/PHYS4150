"""
Mubinjon Satymov

Exercise 4.3: Calculating derivatives

a)  Write a program that defines a function f(x) returning the value x(x−1), 
then calculates the derivative of the function at the point x = 1 using the 
formula above with δ = 1e−2. Calculate the true value of the same derivative 
analytically and compare with the answer your program gives. 
The two will not agree perfectly. Why not?

b)  Repeat the calculation for δ =1e−4, 1e−6, 1e−8, 1e−10, 1e−12, and 1e−14. 
You should see that the accuracy of the calculation initially gets better as δ
gets smaller, but then gets worse again. Plot your result as a function of δ.
Why is this?

Solution:
    General formula to calculate derivative 
    (df/dx)=lim((f(x+δ)-f(x)))/(δ)
    where δ approaches 0;
    
Q/A:    Part a) 
        Analytical and numerical derivative would not agree because for 
        numerical calculation value of "n" cannot be Zero. If we start from
        Zero the compiler would show us an error, since devision by Zero not 
        allowed;
        
        Part b)
        Since there floating point limitation in Python the smallest value
        of "δ" started approaching Zero for df/dx. As we can see from graph 
        from it is "safer" if we limit the values of "δ" from 1e-4 to 1e-12;
"""
#Part a:
import matplotlib.pyplot as plt
import numpy as np
def f(x):     #defining function f(x)=x*(x-1);
    f=x*(x-1)
    return f
x=1          #Declaring value of x;
n=1e-2       #n represent "δ";
e=(f(x+n)-f(x))/n #evaluating derivative; 
print("Part A:\nat x=1 and δ=1e-2, \nValue of df/dx=",e)

#Part b:
n=[1e-2,1e-4,1e-6,1e-8,1e-10,1e-12,1e-14]
ans=[]     #Creating empty array 
for k in n: 
    e=f(1+k)-f(1)
    ans.append(e/k)  #Assigning to array values of "e/k";
plt.plot(np.log10(n),ans)  #Plotting in semilog scale;
plt.title('Part B:Error Distribution Graph')
plt.xlabel('Value of "δ" in Logarithmic Scale')
plt.ylabel('Value of Evaluated Function')
plt.show()