# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 11:28:54 2014

@author: Morgen
"""
#constants for the formula
Ksquared=0.93#for rain or liquid
La=1.0#the atmospheric effects
b=10**4.55
rone=2.17*10**(-10)#in km for Nexrad
atmsphereff=Ksquared/La

#function to compute the power formula 8.23
def power(range,dbz,transmitP,ksquared,b,rone,atmsphereff):
    zoverz1=10**(dbz/10)
    rangeinverse=rone**2/range**2
    power1=b*atmsphereff
    power2=rangeinverse*power1*zoverz1*transmitP
    
    print ("The Power in watts is")    
    print power2
#call to the function to give thepower    
thepower=power(20,40,750000,Ksquared,b,rone,atmsphereff)   
 