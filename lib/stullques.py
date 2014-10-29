# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 09:52:31 2014

@author: Morgen
"""
#code to solve question re Roland Stull, 8.10-8.14


from math import pi
import numpy as np

c=3*10^8 #m/s
dtor=np.pi/180#change from degrees to radians
a=71.6*dtor
wavelengths=np.array([.20,.20,.10,.10,.10,.05,.05,.05,.05,.03])
antennad=np.array([8,10,10,5,3,7,5,2,3,1])
rttimes=np.array([2,5,10,25,50,75,100,150,200,300])
prf=np.array([50,100,200,400,600,800,1000,1200,1400,1600])

#ques 10 to find the beamwidth angle in radians
#use equation 8.13
def beamwidth(wavelenght,antenna):
    top=a*wavelenght
    thebeamwidth=top/antenna
        
    return thebeamwidth
       
thebeamwidths=[]    
wave_antenna_pair=zip(wavelengths,antennad)
for wavelengths,antennad in wave_antenna_pair:
        thebeamwidths.append(beamwidth(wavelengths,antennad))

print("the beamwidths angles in radians are")    
print thebeamwidths
    
    #ques 11
print ("the band associated with a, b, are LBands, c,d,e are Sband, h,i are C band and j is X band")
    
 #ques 12
#use equation 8.16
def range(times,c):
    ranges=[]
    ranges=c*np.array(times)/2
    ranges=np.array(ranges)*10^(-6)
    return ranges   
       
roundtrips=[]
roundtrips=range(rttimes,c)
print ("The round-trip travel times in microseconds are")
print roundtrips
    

#ques 13
#use formula 8.17
def maxrange(frequencies,c):
    maxranges=[]
    maxranges=c/(2.*np.array(frequencies))
    return maxranges

themaxrange=[]  
themaxrange=maxrange(prf,c)  

print ("The max ranges in km are")
print themaxrange

#ques 14
#use v=frequency*wavelengths
veloctiy1= []
velocity1=.10*np.array(prf)

print("velocities in m/s for .10m wavelength")
print velocity1

velocity2=[]
velocity2=.05*np.array(prf)
print("velocities in m/s for .05m wavelength")

print velocity2