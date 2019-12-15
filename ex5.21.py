import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc

#Charges in C 
q1, q2=1,-1

#Distance between charges
r = 0.1

def Phi(q,r):  #Potential Function
    return q/(4*np.pi*sc.epsilon_0*r)

print("Total potential is:",(Phi(q1, r)+Phi(q2,r)))
print("We can see that total potential is Zero\n"
      "Which is correct since according to the\n"
      "formula Total Potential=(kpcos(theta))/(r^2\n"
      ",where k=(4*pi*epsilon0).\n"
      "When we have Dipole theta=90 and cos(90)=0")

#Matrix of 100x100 created, which represents different coordinates
n = 100
total_phi= np.zeros([n,n])
x=np.linspace(-.5, .5, num = n)
y=x

#Calculating Total potential for every point
xp=[-0.05,0.05]
yp=[0,0]
for i in range (n):
    for j in range(n):
        r1= np.sqrt((x[i] - xp[0])**2+(y[j]-yp[0])**2)
        r2= np.sqrt((x[i] - xp[1])**2+(y[j]-yp[1])**2)
        qpos= Phi(q1,r1)
        qneg= Phi(q2,r2)
        total_phi[i][j]=qpos+qneg


map=plt.imshow(total_phi)
map.set_cmap("Greys")
plt.title("Total Potential Density Plot")
plt.show()

#Plotting Electral Potential
dx=np.ones([n,n])
dy=np.ones([n,n])

for i in range (0,n-1,5 ):
   for j in range(0,n-1,5):
       dx[i][j]=(total_phi[i+1][j]-total_phi[i-1][j])/(n)
       dy[i][j]=(total_phi[i][j+1]-total_phi[i][j-1])/(n)
       plt.arrow(x[i],y[j],1e-9*dx[i][j], 1e-9*dy[i][j],  )
       plt.xlim(-1,1)
       plt.ylim(-1,1)
plt.title("Visualiation of the field")
plt.show()
 