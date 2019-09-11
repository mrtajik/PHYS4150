#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Part a
import numpy as np
x=float(input("How far planet X  away in light years= "))
v=float(input("Relativistic speed of a spaceship V= "))
t0=x*v
print("For observer on Earth spaceship would reach planet X in ",t0,"light years")


# In[13]:


#Part 
import numpy as np
x=10 #distance
v=.99 #speed
t0=x*v
t=(t0)/(np.sqrt(1-(v**2)))
print("Passenger on board ship would reach planet X in ",t,"light years")


# In[ ]:




