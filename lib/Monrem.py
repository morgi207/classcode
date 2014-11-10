# -*- coding: utf-8 -*-
"""
Created on Fri Nov 07 17:30:13 2014

@author: Morgen
"""
#code for Stull, ques 8.21-8.24

#A21
#use equation 8.29
a1=0.017/60
import numpy as np
a2=0.0714#/dbz
times=np.array([10,15,4,1,25,5])#time in minutes
dbz=np.array([15,30,43,50,18,10])
top=[]
top=a2*dbz
part=[]
part=10**top
Rainrate=[]
Rainrate=part*a1#in mm/min
rainfallamounts=[]
rainfallamounts=Rainrate*times
forhour=60*rainfallamounts
forhourtotal=sum(forhour)
print('the rainfall in mm is approximately')
print forhourtotal

#A22 use equation 8.32
radialv=np.array([-110,-85,-60,-20,90,65,40,30])#radial velocity in m/s
lambd=10**(-1)#in metres
array=[]
array=2*radialv
deltav=array/lambd
print ('Doppler shift in -s')
print deltav

#23 use equation 8.36a
#a negative reading means coming towards the radar
Mrmaxdbl=50 #in m/s
vel=np.array([26,28,30,35,20,25,55,-26,-28,-30,-20])

for x in range (0,10):
   false=[]  
   dbl=[]    
   if vel[x] < 50:
      thevalone=vel-Mrmaxdbl
      false.append(thevalone)
      if vel[x] > 50:
           theval=vel+Mrmaxdbl
           dbl.append(theval)
           
                       
           print dbl
           print false
            
            
# question A24 ues 8.35a diagram
maxr=200
Arange=np.array([205,210,250,300,350,400,230,240,390,410])
appear=Arange-maxr
print ('The ranges that the the radar would display in km are')
print appear            

            
        

#