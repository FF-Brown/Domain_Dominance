# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:53:00 2020

@author: Nathan
"""


# import Dragons as sc
from ..Dragons import *

def testEFDragon():
    test = sc.EFDragon()
    assert test.name == "Elder Fire Dragon", "Should be Elder Fire Dragon"
    assert test.element == "Fire", "Should be Fire"
    assert test.tipo == "Dragon", "Should be Dragon"
    assert test.health == 70, "Should be 70"
    assert test.ability == "+2 Fire Attacks\n-2 Fire Damage\n+1 Attack/Rage\nFor every 5 damage taken +1 Rage\nFor every 5 health healed -1 Rage\nGuardian +10 Health\n", "Incorrect ability."
    assert test.attacks[0].tipo == "Fire", "Should be Fire"
    assert test.attacks[0].dmg == 3, "Should be 3"
    assert test.isAlive() == True, "Should be True"
    print(test)
    print("EFDragon: All tests passed.")
        
    
def testKFDragon():
    test = sc.KFDragon()
    assert test.name == "King Fire Dragon", "Should be King Fire Dragon"
    assert test.element == "Fire", "Should be Fire"
    assert test.tipo == "Dragon", "Should be Dragon"
    assert test.health == 60, "Should be 60"
    assert test.ability == "+1 fire damage/other living non-minion fire creature you control\nFor every 5 damage taken +1 Rage\nFor every 5 health healed -1 Rage\nGuardian: Give each other non-minion fire creature you control +1 fire damage/other living non-minion fire creature you control.\n", "Incorrect ability."
    assert test.attacks[0].tipo == "Fire", "Should be Fire"
    assert test.attacks[0].dmg == 3, "Should be 3"
    assert test.attacks[1].tipo == "Fire", "Should be Fire"
    assert test.attacks[1].dmg == 9, "Should be 9"
    assert test.isAlive() == True, "Should be True"
    print("KFDragon: All tests passed.")

def testDragonling():
    test = sc.Dragonling()
    assert test.name == "Dragonling", "Should be Elder Fire Dragon"
    assert test.element == "void", "Should be void"
    assert test.tipo == "Dragon", "Should be Dragon"
    assert test.health == 40, "Should be 40"
    assert test.ability == "(Fire/Ice/Water) and dragon attacks cost 2E less for this creature (cannot cost less than 1E) and do 2 less damage (cannot do less than 1 damage)\n", "Incorrect ability."
    assert test.attacks[0].tipo == "void", "Should be void"
    assert test.attacks[0].dmg == 2, "Should be 2"
    assert test.isAlive() == True, "Should be True"
    print("Dragonling: All tests passed.")

def testPrints():
    test1 = sc.EFDragon()
    test2 = sc.KFDragon()
    test3 = sc.Dragonling()
    print(test1)
    print(test2)
    print(test3)
    
    
testPrints()
testEFDragon()
testKFDragon()
testDragonling()
