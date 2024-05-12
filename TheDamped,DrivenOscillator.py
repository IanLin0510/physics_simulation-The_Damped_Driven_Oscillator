#!/usr/bin/env python
# coding: utf-8

# In[1]:

#simulate the motion
from vpython import *
#creat
dict={'angular_frequency':[],'time':[],'b.pos':[],'amplitude':[]}
scene=canvas(width=900,length=600,center=vec(0.5,0,0),range=1.1, background=color.black)
block=box(pos=vector(0.25,0,0), size=vector(0.1,0.1,0.15), color=color.purple)
table=box(pos=vector(0.5,-0.05,0), size=vector(3,0.01,2), color=color.white, make_trail=False,texture='data:image/jpeg;base64,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')
wall=box(pos=vector(0,0.01,0), size=vector(0.01,0.5,0.5), color=color.red, make_trail=False)
spring=helix(pos=vector(0,0,0), axis=block.pos-vec(0,0,0), radius=0.05,color=color.green)
L=block.pos#stretched length
Lhat=hat(L)#give a direction
L0=1#unstretched length
s=mag(L)-L0#the displacement of the spring from equilibrium
dt=0.01#time interval
t=0#initial time
k=1.5#spring constant
m=0.02#mass
mu=0.3#the velocity of oscillator
g=9.8#gravity
pblock=m*vector(0.1,0,0)#block of momentum
fm=8#constant
gama=0.2#constant
B=2*gama*m#constant
wshm=(k/m)**(1/2)#angular velocity of SHM
wd=0#initial angular velocity of driving force
dw=0.01#interval of angular velocity of driving force
block.v = vector(0, 0, 0)#set the block.v
#creat x-t plot
gd = graph(title="plot", width=600, height=450, xtitle="t(s)", ytitle="x(m)", align = 'left')
xt = gcurve(graph=gd, color=color.blue)
#creat amplitude-t plot
gda = graph(title="amplitude-wd", width=600, height=450, xtitle="wd", ytitle="amplitude(m)", align = 'left')
xta = gcurve(graph=gda, color=color.green)
while 0<=wd<2.2:
    rate(100)#Halts computations until 1.0(frequency/seconds) after the previous call to rate()
    A=(fm/m)/((((wshm**2)-(wd**2))**2)+((B*wd)/m)**2)**(1/2) #calculate amplitude
    dict['amplitude'].append(A)
    count=0
    dict['angular_frequency'].append(wd)
    wd=wd+dw#refresh the angular velocity of driving force
    if count<1:#counter
        rate(100)#Halts computations until 1.0(frequency/seconds) after the previous call to rate()
        Fspring=-k*s*Lhat#spring force
        phat=hat(pblock)#give a direction
        Fsliding=-mu*m*g*phat#driving force
        pblock=pblock+(Fspring+Fsliding)*dt#momentum of block
        block.pos=block.pos+pblock*dt/m#x=p*t/m
        dict['b.pos'].append(block.pos.x)
        spring.axis=block.pos-vec(0,0,0)#give a direction
        L=block.pos#stretched length
        Lhat=hat(L)#give a direction
        s=mag(L)-L0#change of length
        #make plot
        xt.plot(pos=(t,block.pos.x-1))
        xta.plot(pos=(wd,A))
        dict['time'].append(t)
        t=t+dt#refresh the time
        count=count+1
while 10>wd>=2.2:
    A=(fm/m)/((((wshm**2)-(wd**2))**2)+((B*wd)/m)**2)**(1/2)#amplitude
    dict['amplitude'].append(A)
    count=0
    dict['angular_frequency'].append(wd)
    wd=wd+dw#refresh the angular velocity of driving force
    if count<1:#counter
        rate(50)#Halts computations until 1.0(frequency/seconds) after the previous call to rate()
        Fspring=-k*s*Lhat#spring force
        phat=hat(pblock)#given a direction
        Fsliding=-1*phat#driving force
        pblock=pblock+(Fspring)*dt#momentum of block
        block.pos=block.pos+pblock*dt/m#x=p*t/m
        dict['b.pos'].append(block.pos.x)
        spring.axis=block.pos-vec(0,0,0)#give a direction
        L=block.pos#stretched length
        Lhat=hat(L)#given a direction
        s=mag(L)-L0#change of length
        #make plot
        xt.plot(pos=(t,block.pos.x-1))
        xta.plot(pos=(wd,A))
        dict['time'].append(t)
        t=t+dt#refresh the time    
        count=count+1





# In[2]:
#process data

import pandas as pd
angular_frequency=list(map(float, dict['angular_frequency']))
time=list(map(float,dict['time']))
amplitude=list(map(float,dict['amplitude']))
b_pos=list(map(float,dict['b.pos']))


# In[3]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.Series(b_pos)


# In[4]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.Series(angular_frequency)


# In[5]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.Series(time)


# In[6]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.Series(amplitude)


# In[7]:


import matplotlib.pyplot as plt
import numpy as np


# In[8]:

#plot the graph
plt.plot(time,b_pos, color='blue')
plt.title('x-t',loc='center')
plt.xlabel('time(s)',{'fontsize':12,'color':'black'})
plt.ylabel('position of block(m)',{'fontsize':12,'color':'black'})


# In[9]:


plt.plot(angular_frequency,amplitude, color='red')
plt.title('amplitude-angular frequency of driving force',loc='center')
plt.xlabel('angular frequency of driving force(rad/s)',{'fontsize':12,'color':'black'})
plt.ylabel('amplitude(m)',{'fontsize':12,'color':'black'})


# In[10]:


max(dict['amplitude'])


# In[11]:


test=(k/m)**(1/2)
test


# In[12]:


print((dict['amplitude'])[866],(dict['angular_frequency'])[866])
#結論:切的不夠小 產生誤差

