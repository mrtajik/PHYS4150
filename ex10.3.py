import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 100        #Number of itteration(or particles)
i = 2          #x coordinate
j = 2          #y coordinate
L = 6          #Boundaries of X and Y coordinates

xpoints=[]
ypoints=[]

for k in range(N): # Walking logic with random position
    xpoints.append(i)
    ypoints.append(j)
    random = np.random.randint(1,5)
    if (random ==1):       #Right
        i +=1
        if (i==L):
            i-=1
    elif(random == 2):     #Left
        i -=1
        if(i==0):
            i+=1
    elif(random == 3):     #Up
        j += 1
        if (j==L):
            j-=1
    elif(random == 4):     #Down
        j -=1
        if (j==0):
            j+=1
   
    


fig = plt.figure(figsize=(6,7))
ax = plt.axes(xlim=(-1, 6), ylim=(-1,6))
ax.set_xlabel('X')
ax.set_ylabel('Y')
fig.suptitle('Brownian Motion', fontsize=14)
dot=plt.Circle((2,2),radius=.09,facecolor='blue')

def init():
    dot.center = (2, 2)
    ax.add_patch(dot)
    return dot,

def animate(k):
    x = xpoints[k]
    y = ypoints[k]
    
    dot.center = (x, y)
    return dot,

anim = animation.FuncAnimation(fig, animate,
init_func=init,frames=30,interval=50,blit=True)
plt.show()
