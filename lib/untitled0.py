# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 17:49:22 2014

@author: Morgen
"""

class Kangaroo(object):#creating a class called Kangaroo
    def__init__(self, contents=None):
        #first parameter of a method is called self
        #second parameter is contents
        ##default value is None
        if contents == None:
            contents=[]
        self.pouch_contents=contents
        #this way every Kangaroo that has default value, will get a 
        #reference to a diff list
        #attribute is pouch_contents
    def put_in_pouch(self,thing):
        #to take an object of any type and add it to the pouch_contents
        self.pouch_contents.append(thing)
        
    def_str_(self)# special method to return a string representation
        #will also return the contents of the pouch
        m= [object._str_(self) + 'the pouch contents:']
        for obj in self.pouch_contents:
            s='    ' + object._str_(obj)
            m.append(s)
        return '\n'.join(t)
        
        
#testing the code by creating two Kangaroo objects, and assigning them to 
#variables        
kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch('cell phone')
kanga.put_in_pouch('lip gloss')
kanga.put_in_pouch(roo)

print kanga
print ''

print roo
    
        