#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math as mt

class VectorCartesiano:
    def __init__(self,x,y,z): #Inicializamos la clase.
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)
        self.Vector=[x,y,z] #Definir el vector nos ayudará posteriormente a seleccionar una única coordenada.
        self.magnitud=np.sqrt((self.x)**2+(self.y)**2+(self.z)**2)

    def __mul__(self,mult): #Sobrecargamos el producto, para el producto punto.
        nx=self.x*mult.x 
        ny=self.y*mult.y
        nz=self.z*mult.z
        return nx+ny+nz
    
    def Cruz(self,x2,y2,z2): #Creamos un método para el producto cruz.
        a = np.array([self.x,self.y,self.z])  
        b = np.array([x2,y2,z2])  
        return np.cross(a,b)
    
    def __getitem__(self,index): #Sobrecarcagamos para seleccionar una única coordenada.
        return self.Vector[index]
    
    def __add__(self,op): #Sobrecargamos la suma.
        nx=self.x+op.x #Sumamos coordenada a coordenada.
        ny=self.y+op.y
        nz=self.z+op.z
        return VectorCartesiano(nx,ny,nz)
    
    def __sub__(self,op): #Sobrecargamos la resta.
        nx=self.x-op.x #Restamos coordenada a coordenada.
        ny=self.y-op.y
        nz=self.z-op.z
        return VectorCartesiano(nx,ny,nz)
    
    def __eq__(self,mult):  #Sobrecargamos ==.
        if self.x==mult.x and self.y==mult.y and self.z==mult.z:
            return True
        else:
            return False     
    
    def Cart_to_esf(self): #Transformamos de cartesianas a esféricas.
        r=np.sqrt((self.x)**2+(self.y)**2+(self.z)**2)
        theta=mt.acos(self.z/r)
        if self.x==0:
            phi=np.pi/2
        else:
            phi=mt.atan(self.y/self.x)
        nv=[r, theta, phi]
        print(nv)
    
    def Print(self): 
        #Imprimimos el vector
        print(f"[{self.x},{self.y},{self.z}]")


# In[2]:


class VectorPolar(VectorCartesiano): #Heredamos de la clase VectorCartesiano.
    def __init__(self,r,theta,phi): #Inicializamos la clase.
            
        if r>0 and 0<=theta<=np.pi and 0<=phi<=2*np.pi: #Nos aseguramos que los valores estén en los rangos adecuados.
            
            self.r=float(r)
            self.theta=float(theta)
            self.phi=float(phi)
            x=float(self.r*mt.sin(self.theta)*mt.cos(self.phi))
            y=float(self.r*mt.sin(self.theta)*mt.sin(self.phi))
            z=float(self.r*mt.cos(self.phi))

            VectorCartesiano.__init__(self,x,y,z)
        else:
            print("Ingrese valores en los rangos adecuados.")
            
    def Esf_to_cart(self): #Transformamos de esféricas a cartesianas.
        x=self.r*mt.sin(self.theta)*mt.cos(self.phi)
        y=self.r*mt.sin(self.theta)*mt.sin(self.phi)
        z=self.r*mt.cos(self.theta)
        nv=[x,y,z]
        print(nv)


# In[ ]:




