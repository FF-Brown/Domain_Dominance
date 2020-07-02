# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:23:57 2020

@author: Nathan
"""

# import pytest 

import Player as pl
from Creature import Attack

def testTakeDmg(p1, p2):
    punch = Attack("Physical", 3)
    preHealth = p1.field[0].health 
    p1.field[0].takeDmg(punch)
    assert p1.field[0].health == preHealth - 3, "Should be" + str(preHealth - 3)
    print("takeDmg(): Test passed") 
    
def testUseAttack(p1, p2):
    fireAttack = Attack("Fire", 3) 
    returnedAttack = p1.field[1].useAttack(0)
    assert str(returnedAttack) == str(fireAttack), "Should be '3 points Fire damage'" 
    print("useAttack(): Test passed") 

# @pytest.mark.skip(reason="Cannot test input-based functions") 
def testGetAttack(p1,p2): 
    print("Test message: Should only accept\n1 through #of attacks, and should return\n1 less than user input.")
    result = p1.field[2].getAttack()
    print("Returned ", result) 



p1 = pl.Player(r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Documents\TestDeck.csv")
p2 = pl.Player(r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Documents\TestDeck2.csv")


print(p1.getCards())
print(p2.getCards()) 
testTakeDmg(p1, p2)
testUseAttack(p1, p2) 
testGetAttack(p1, p2) 
