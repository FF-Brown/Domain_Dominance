# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 01:46:39 2020

@author: Nathan
"""


import Player as pl
from Creature import Attack, Creature 
import logging
logger = logging.getLogger("dd")
logger.setLevel(logging.INFO)
fh = logging.FileHandler("./playerTest.log")
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt =  "%Y-%m-%d %H:%M")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
if not logger.handlers:
    logger.addHandler(fh)
    logger.addHandler(ch)


def testPlayer1():
    test = pl.Player(1, r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Docs\TestDeck.csv")
    assert test.coin == 0, "Should be 0"
    assert len(test.field) == 3, "Should be 3"
    print("Player1: All tests passed")
    
def testPlayer2():
    test = pl.Player(2, r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Docs\TestDeck2.csv")
    assert test.coin == 0, "Should be 0"
    assert len(test.field) == 3, "Should be 3"
    print("Player2: All tests passed")

def testGetGuardian():
    print("\nTest msg: Choose 'Elder Fire Dragon' as guardian.\n") 
    test = pl.Player(1, r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Docs\TestDeck.csv")
    assert test.field[1].guardian == True, "Should be True" 
    assert test.field[1].health == 80, "Should be 80" 
    print("getGuardian(): All tests passed") 
    
def testUpdateCreatureInfo():
    """Built to test King Fire Dragon's implementation""" 
    test = pl.Player(1, r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Docs\TestDeck.csv")
    assert test.field[2].getCreatureTypes == True, "Should be True" 
    test.updateCreatureInfo() 
    print(test.field[2].creatureTypes)
    # assert test.field[2].creatureTypes == ["Fire", "Dragon", "Fire", "Dragon", "Fire", "Dragon"], 'Should be ["Fire", "Dragon", "Fire", "Dragon", "Fire", "Dragon"]'
    result = test.field[2].modAttack(Attack("Fire", 5))
    assert result.dmg == 7, "Should be 7"
    print("updateCreatureInfo(): All tests passed") 
    
def testChooseCreature():
    test = pl.Player(1, r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Docs\TestDeck.csv")
    print("Test msg: Choose Dragonling (0).")    
    test.field[0].resetAP() 
    attacker = test.chooseCreature()
    # print(attacker) 
    assert attacker.name == test.field[0].name, "Should be Dragonling" 
    # print("Check log to verify that correct creature was selected.") 
    print("Test passed.") 
    
def testChooseTarget():
    test = pl.Player(1, r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Docs\TestDeck.csv")
    test2 = pl.Player(2, r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Docs\TestDeck2.csv")
    print("Test msg: Choose Fire Golem") 
    target = test.chooseTarget(test2)
    assert isinstance(target, Creature), "Should be a Creature"
    assert target.name == "Fire Golem", "Should be 'Fire Golem'"
    print("chooseTarget() tests passed.") 
    
def testBuffOutgoing():
    test = pl.Player(1, r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Docs\TestDeck.csv")
    test.upkeep() 
    atk = Attack(tipo=["Fire"],dmg=3, energyCost=2)
    attacks = []
    attacks.append(atk) 
    
    test.buffOutgoing(test.field[0], attacks)
    
    assert attacks[0].dmg == 1, "Should be 1dmg now"
    print("Energy cost: ", attacks[0].energyCost) 
    # This test no longer accurate. Dragonling updates energyCost when attacking, not when buffing.
    # assert attacks[0].energyCost == 1, "Should be 1 energy now"
    print(attacks) 
    try:
        assert attacks[1].dmg == 2, "Should have an additional 2dmg attack now" 
    except:
        print("No attack appended.") 
    else:
        print("buffOutgoing() all tests passed.") 
        
def testDivideAttack():
    test = pl.Player(1, r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Docs\TestDeck.csv")
    test2 = pl.Player(2, r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Docs\TestDeck2.csv")
    atk = Attack(tipo=["Fire"], dmg=5, energyCost=3, targets=3, divisible=True) 
    
    temp = test.divideAttack(atk, test2)
    
    print() 
    print(temp) 
    
            
    
if __name__ == '__main__':
    logger.info('~~~~~~~~~~~~')
    # testPlayer1()
    # testPlayer2()
    # testGetGuardian() 
    # testUpdateCreatureInfo() 
    # testChooseCreature()
    # testChooseTarget()
    # testBuffOutgoing()
    testDivideAttack()
    
    
    