#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import matplotlib.pyplot as plt
a=np.linspace(0,2*np.pi,num=100)
x=2*np.cos(a)+np.cos(2*a)
y=2*np.sin(a)-np.sin(2*a)
plt.plot(x,y)
plt.show()


# In[11]:


import numpy as np
import matplotlib.pyplot as plt
a=np.linspace(0,10*np.pi,num=100)
r=a**2
x1=r*np.cos(a)
y1=r*np.sin(a)
plt.plot(x1,y1)
plt.show()


# In[12]:


import numpy as np
import matplotlib.pyplot as plt
a=np.linspace(0,10*np.pi,num=100000)
r=(np.exp(np.cos(a)))-2*np.cos(4*a)+(np.sin(a/12))**5
x2=r*np.cos(a)
y2=r*np.sin(a)
plt.plot(x2,y2)
plt.show()


# In[14]:


f,axes=plt.subplots(1,3,figsize=(14,6))
axes[0].plot(x,y)
axes[1].plot(x1,y1)
axes[2].plot(x2,y2)


# In[ ]:




