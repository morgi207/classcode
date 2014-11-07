# -*- coding: utf-8 -*-
"""
Created on Sun Nov 02 21:05:23 2014

@author: Morgen
"""
#variables
Pr=1.5848931925e-9 #in watts
R=1*10**5#returned energy in m
b=14255#dimensionless equipment factor
Pt=750000 ##the transmitted poweer in watts
R1=2.17*10**(-10)#for nexraad
a3=.300#in m/hr
a4=.014# in m/h
Z1=1 #in mm^6/m^3
Ksquared=0.93# for liquid drops
La=1.0#attenuation equals zero
Ksquareds=0.208
num=2000
# uses the radar equation and the idea that Z=#*RR^# to find the precipitation
#rate. Uses stull, equation 8.23

def thepreciprate(Pr,R,b,Pt,R1,a3,La,a4,Z1,Ksquared):
    rrpower=Pr/Pt
    atmoseffect=Ksquared/La
    rangeinversesquare=(R1/R)**2
    Z=(rrpower*Z1)/(b*atmoseffect*rangeinversesquare)
    RR=(Z/a3)**(0.714)
    return RR
 #function to find the snowfall rate
#uses Stull 8.23 and Z=2000*RR^2
def thesnowrate(Pr,R,b,Pt,R1,num,La,Z1,Ksquareds):
    rrpower=Pr/Pt
    atmoseffect=Ksquareds/La
    rangeinversesquare=(R1/R)**2
    Z=(rrpower*Z1)/(b*atmoseffect*rangeinversesquare)
    snowrate=(Z/num)**(1/2)
    return snowrate
   
rainfallrate=thepreciprate(Pr,R,b,Pt,R1,a3,La,a4,Z1,Ksquared)
print ("The rainfallrate is")       
print rainfallrate
   
snowfall=thesnowrate(Pr,R,b,Pt,R1,a3,a4,Z1,Ksquareds)
print ("The snowfall rate is")
print snowfall 

atten=3   
attenfacdiff=thepreciprate(Pr,R,b,Pt,R1,a3,atten,a4,Z1,Ksquared)
print("the rainfall rate when attenuation is 3 dbz")
print attenfacdiff
   
print("The rainfall rate appears to decrease signifigantly with a higher attenuation")
print("This is because higher attenuation accounts for losses by absorption and scattering")
print("The snowfall rate appears to be a much lower rate, possibly because it is hard for the radar to pick it up")