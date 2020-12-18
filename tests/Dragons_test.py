# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:53:00 2020

@author: Nathan
"""

import Dragons as sc
from Creature import Attack 

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
    
def testModAttacks():
    d1 = sc.EFDragon()
    d2 = sc.KFDragon()
    d3 = sc.Dragonling() 
    attacks = []
    #~~~EFDragon~~~
    #Test 1
    atk = Attack(tipo=["Dragon", "Fire"],dmg=3,energyCost=3) 
    attacks.append(atk) 
    # print(attacks) 
    d1.modAttack(attacks) 
    assert attacks[0].dmg == 5, "Should be 5dmg" 
    #Test 2
    atk = Attack(tipo=["Dragon"],dmg=3)
    attacks[0] = atk 
    d1.modAttack(attacks)
    assert attacks[0].dmg == 3, "Should be 3dmg" 
    #Test 3
    atk = Attack(tipo=["Physical"],dmg=6)
    d1.takeDmg(atk)
    d1.rageUpkeep(5) 
    assert d1.rage == 1, "Should have 1 rage"
    #~~~KFDragon~~~
    d2.creatureTypes = ["Fire", "Fire", "Fire"]
    #Test 1
    atk = Attack(tipo=["Dragon","Fire"],dmg=2)
    attacks[0] = atk
    d2.modAttack(attacks)
    assert len(attacks) == 2, "Should be length 2"
    # print(attacks) 
    assert attacks[1].dmg == 2, "Should be 2dmg" 
    #Test 2
    attacks = []
    atk = Attack(tipo=["Physical"], dmg=3)
    attacks.append(atk) 
    d2.modAttack(attacks)
    assert len(attacks) == 1, "Should be length 1"
    assert attacks[0].dmg == 3, "Should still be 3dmg"
    #Test 3
    d2.modAllyAttack(attacks)
    assert len(attacks) == 1, "Should be length 1"
    assert attacks[0].dmg == 3, "Should still be 3dmg"
    #Test 4
    atk = Attack(tipo=["Dragon", "Fire"], dmg=4)
    attacks[0] = atk 
    d2.modAllyAttack(attacks)
    assert len(attacks) == 2, "Should be length 2"
    assert attacks[0].dmg == 4, "Should still be 4dmg"
    # print(attacks) 
    assert attacks[1].dmg == 2, "Should be 2dmg" 
    #~~~Dragonling~~~
    attacks = []
    #test 1
    atk = Attack(tipo=["Fire"], dmg=2)
    attacks.append(atk) 
    d3.modAttack(attacks) 
    print(attacks) 
    assert attacks[0].dmg == 1, "Should be 1dmg"
    #Test 2
    atk = Attack(tipo=["Dragon"], dmg=4)
    attacks[0] = atk
    d3.modAttack(attacks)
    assert attacks[0].dmg == 2, "Should be 2dmg"
    
    print("testModAttacks() all tests passed.") 
    
def testHasEnergy():
    d1 = sc.KFDragon()
    d2 = sc.Dragonling()
    
    #~~~Not Dragonling~~~
    #Test 1
    atk = Attack(tipo=["Dragon"],dmg=2,energyCost=2)
    assert d1.hasEnergy(atk) == False, "Should be False" 
    #Test 2
    d1.addEnergy()
    assert d1.hasEnergy(atk) == True, "Should be True"
    #~~~Dragonling~~~
    #Test 1
    atk = Attack(tipo=["Dragon"],dmg=2,energyCost=2)
    assert d2.hasEnergy(atk) == False, "Should be False"
    #Test 2
    d2.addEnergy()
    assert d2.hasEnergy(atk) == True, "Should be True"
    #Test 3
    atk = Attack(tipo=["Dragon"],dmg=2,energyCost=3)
    d2.hasEnergy(atk)
    assert atk.energyCost == 1, "Should be 1 energy"
    #Test 4
    atk = Attack(tipo=["Dragon"],dmg=2,energyCost=4)
    d2.hasEnergy(atk)
    assert atk.energyCost == 2, "Should be 2 energy" 
    #Test 5
    atk = Attack(tipo=["Fire"],dmg=2,energyCost=3)
    assert d2.hasEnergy(atk) == True, "Should be True" 
    #Test 6
    atk = Attack(tipo=["Physical"],dmg=2,energyCost=3)
    assert d2.hasEnergy(atk) == False, "Should be False" 
    
    print("hasEnergy() all tests passed.") 
if __name__ == '__main__':
    # testPrints()
    # testEFDragon()
    # testKFDragon()
    # testDragonling()
    # testModAttacks() 
    testHasEnergy() 
