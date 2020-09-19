# -*- coding: utf-8 -*-
"""
Created on Sun May 10 19:43:37 2020

@author: Nathan
"""

from Creature import Attack 
from Dragons import Dragonling, EFDragon 
from Golems import SpGolem, CGolem 

def testAddEnergy():
    test = SpGolem()
    assert test.energy == 0, "Should be 0"
    test.addEnergy()
    assert test.energy == 2, "Should be 2"
    
    test = Dragonling()
    assert test.energy == 0, "Should be 0"
    test.addEnergy()
    assert test.energy == 1, "Should be 1"
    
    print("addEnergy(): All tests passed.")
    
def testTakeDmg():
    punch = Attack("Physical", 3)
    test = EFDragon() 
    preHealth = test.health 
    test.takeDmg(punch)
    assert test.health == preHealth - 3, "Should be" + str(preHealth - 3)
    print("takeDmg(): Dragon test passed") 
    test = SpGolem() 
    preHealth = test.health 
    test.takeDmg(punch)
    assert test.health == preHealth - 3, "Should be" + str(preHealth - 3)
    print("takeDmg(): Golem test passed") 

def testSetElement():
    print("Test msg: Choose 'Fire' first")
    test = Dragonling() 
    assert test.name == "Fire Dragonling", "Should be Fire Dragonling"
    assert test.attacks[0].tipo == "Fire", "Should be Fire" 
    
    print("Test msg: Choose 'Water' here")
    test = CGolem() 
    assert test.name == "Water Golem", "Should be Water Golem"
    assert test.attacks[0].tipo == "Water", "Should be Water" 
    print("setElement(): All tests passed") 

def testModAttack():
    test = EFDragon() 
    testAtk = Attack("Fire", 3)
    temp = test.modAttack(testAtk) 
    assert temp.dmg == 5, "Should be 5"
    
    testAtk = Attack("Fire", 3, 2, 1) 
    temp = test.modAttack(testAtk) 
    assert temp.dmg == 5, "Should be 5"
    assert temp.tipo == "Fire", "Should be 'Fire'"
    assert temp.energyCost == 2, "Should be 2"
    assert temp.targets == 1, "Should be 1" 

    test2 = Dragonling() 
    testAtk = Attack(test2.element, 2, 2) 
    temp = test2.modAttack(testAtk) 
    assert temp.dmg == 1, "Should be 1"
    assert temp.energyCost == 1, "Should be 1" 
    
    testAtk = Attack("Dragon", 4, 4)
    temp2 = test2.modAttack(testAtk)
    assert temp2.dmg == 2, "Should be 2"
    assert temp2.energyCost == 2, "Should be 2" 
    
    print("modAttack(): All tests passed.") 
    


if __name__ == '__main__':
    # testSetElement() 
    # testAddEnergy() 
    # testModAttack() 
    testTakeDmg()

