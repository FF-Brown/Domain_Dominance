# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 01:46:39 2020

@author: Nathan
"""


# import Player as pl
# from Creature import Attack 
from ..Player import Player as pl
from ..Creature import Attack

def testPlayer1():
    test = pl.Player(1, r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Documents\TestDeck.csv")
    assert test.coin == 0, "Should be 0"
    assert len(test.field) == 3, "Should be 3"
    print("Player1: All tests passed")
    
def testPlayer2():
    test = pl.Player(2, r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Documents\TestDeck2.csv")
    assert test.coin == 0, "Should be 0"
    assert len(test.field) == 3, "Should be 3"
    print("Player2: All tests passed")

def testGetGuardian():
    print("\nTest msg: Choose 'Elder Fire Dragon' as guardian.\n") 
    test = pl.Player(1, r"..\Documents\TestDeck.csv")
    assert test.field[1].guardian == True, "Should be True" 
    assert test.field[1].health == 80, "Should be 80" 
    print("getGuardian(): All tests passed") 
    
def testUpdateCreatureInfo():
    """Built to test King Fire Dragon's implementation""" 
    test = pl.Player(1, r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Documents\TestDeck.csv")
    assert test.field[2].getCreatureTypes == True, "Should be True" 
    test.updateCreatureInfo() 
    print(test.field[2].creatureTypes)
    # assert test.field[2].creatureTypes == ["Fire", "Dragon", "Fire", "Dragon", "Fire", "Dragon"], 'Should be ["Fire", "Dragon", "Fire", "Dragon", "Fire", "Dragon"]'
    result = test.field[2].modAttack(Attack("Fire", 5))
    assert result.dmg == 7, "Should be 7"
    print("updateCreatureInfo(): All tests passed") 
    
if __name__ == '__main__':
    # testPlayer1()
    # testPlayer2()
    #testGetGuardian() 
    testUpdateCreatureInfo() 
    
    
    
    
    