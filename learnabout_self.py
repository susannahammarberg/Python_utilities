# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 12:26:00 2017

@author: Sanna
"""

# define class of Bank
class Bank():
    # class Bank has property crisis 
    crisis = True
    # class Bank has a function 'create_atm'
    def create_atm(self): #(self here refers to the name of the Bank class (in my case seb)
        if self.crisis==False:
            print '$$$'
            #yield "$$$Dollarz"
            
            
# create a bank object called seb
seb = Bank()

crisis_seb = seb.crisis

Bank.create_atm(seb)
#same as 
seb.create_atm()

seb.crisis = False
seb.create_atm()