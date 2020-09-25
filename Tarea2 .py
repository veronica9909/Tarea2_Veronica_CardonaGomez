#!/usr/bin/env python
# coding: utf-8

# # 1.

# In[1]:


from Vector import *


# # 2.

# In[2]:


a=VectorPolar(3,np.pi,2*np.pi)
b=VectorPolar(1,np.pi,2*np.pi)
a.magnitud #Probamos magnitud.


# In[3]:


a.Esf_to_cart() #Probamos transformación.


# # 3.

# In[4]:


a=VectorCartesiano(1.5,0,2.4)
b=VectorCartesiano(0,1,9)
c=VectorCartesiano(4.2,0.05,0)


# In[5]:


a.Cart_to_esf() #Transformamos a esféricas *a*.


# In[6]:


b.Cart_to_esf() #Transformamos a esféricas *b*.


# In[7]:


c.Cart_to_esf() #Transformamos a esféricas *c*.


# In[8]:


a*b #Producto punto a y b.


# In[9]:


a*c #Producto punto a y c.


# In[10]:


b*c #Producto punto b y c.


# In[11]:


a.Cruz(0,1,9) #Producto cruz a y b.


# In[12]:


a.Cruz(4.2,0.05,0) #Producto cruz a y c.


# In[13]:


b.Cruz(4.2,0.05,0) #Producto cruz b y c.


# In[14]:


ang_ab=(a*b)/(a.magnitud*b.magnitud) #Ángulo entre a y b.
ang_ac=(a*c)/(a.magnitud*c.magnitud) #Ángulo entre a y c.
ang_bc=(b*c)/(b.magnitud*c.magnitud) #Ángulo entre b y c.

print("El ángulo entre a y b es: %f, El ángulo entre a y c es: %f, El ángulo entre b y c es: %f."%(ang_ab,ang_ac,ang_bc))


# In[ ]:




