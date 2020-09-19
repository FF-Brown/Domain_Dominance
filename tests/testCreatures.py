#Test classes and functions

from Creature import Creature
from Creature import Attack
from Dragons import Dragonling, EFDragon, KFDragon
from Golems import SpGolem, CGolem, MiGolem


def testCreature():
    
    test = Creature(50, 2, "Dragon", False)
    assert test.health == 50, "Should be 50"
    assert test.energy == 2, "Should be 2"
    assert test.tipo == "Dragon", "Should be Dragon"
    assert test.guardian == False, "Should be False"
    print("Creature: All tests passed.")
    
def testEFDragon():
    test = EFDragon(False)
    assert test.health == 70, "Should be 70"
    assert test.energy == 2, "Should be 2"
    assert test.tipo == "Dragon", "Should be Dragon"
    assert test.guardian == False, "Should be False"
    
    test2 = EFDragon(True)
    assert test2.health == 80, "Should be 80"
    assert test2.energy == 2, "Should be 2"
    assert test2.tipo == "Dragon", "Should be Dragon"
    assert test2.guardian == True, "Should be True"
    assert test2.rage == 0, "Should be 0"
    assert test2.element == "Fire", "Should be Fire"
    print("Dealing damage:")
    test2.dealDmg()
    print("Taking damage")
    test2.takeDmg()
    print("EFDragon: All tests passed.")
    
def testKFDragon():
    
    test = KFDragon(False)
    assert test.health == 60, "Should be 60"
    assert test.energy == 2, "Should be 2"
    assert test.tipo == "Dragon", "Should be Dragon"
    assert test.guardian == False, "Should be False"
    assert test.rage == 0, "Should be 0"
    assert test.element == "Fire", "Should be Fire"
    
    test2 = KFDragon(True)
    assert test2.health == 60, "Should be 60"
    assert test2.energy == 2, "Should be 2"
    assert test2.tipo == "Dragon", "Should be Dragon"
    assert test2.guardian == True, "Should be True"
    assert test2.rage == 0, "Should be 0"
    assert test2.element == "Fire", "Should be Fire"
    print("KFDragon: All tests passed.")

def testDragonling():
    print("Choose Fire")
    test = Dragonling(False)
    assert test.health == 40, "Should be 40"
    assert test.energy == 1, "Should be 1"
    assert test.tipo == "Dragon", "Should be Dragon"
    assert test.guardian == False, "Should be False"
    assert test.element == "Fire", "Should be Fire"
    
    print("Choose Ice")
    testIce = Dragonling(False)
    assert testIce.element == "Ice", "Should be Ice"
    
    print("Choose Water")
    testWater = Dragonling(False)
    assert testWater.element == "Water", "Should be Water"
    
    print("Choose anything")
    testGuardian = Dragonling(True)
    assert testGuardian.guardian == True, "Should be True"
    print("Dragonling: All tests passed")
    

def testAttack():
    test = Attack("KFDragon", 3, 7, "Fire")
    assert test.origin == "KFDragon", "Should be KFDragon"
    assert test.targets == 3, "Should be 3"
    assert len(test.dmg) == 1, "Should be 1"
    assert test.dmg["Fire"] == 7, "Should be 7"
    print("Attack: All tests passed")

# testAttack()
# testEFDragon()
# testKFDragon()
# testDragonling()
# testCreature()

