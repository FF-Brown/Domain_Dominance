# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:32:54 2020

@author: Nathan
"""

from Creature import Creature
from Creature import Attack
    
class EFDragon(Creature):
        
    def __init__(self):
        super(EFDragon, self).__init__("Elder Fire Dragon", ["Fire", "Dragon"], 70, \
                                       "+2 Fire Attacks\n-2 Fire Damage\n+1 Attack/Rage\n" + \
                                           "For every 5 damage taken +1 Rage\n" + \
                                               "For every 5 health healed -1 Rage\nGuardian +10 Health\n", 2)
        self.attacks.append(Attack("Fire", 3, 2))
        self.rage = 0 
        
    def __repr__(self):
        return "\n%s\t%d Health\n\n%s\n%s\n%s" % (self.name, self.health, self.tipo, str(self.attacks), self.ability)
    
    def modAttack(self, atk) -> Attack: 
        atk = self.buffAttack(atk, 2, ["Fire"]) #+2 to Fire-type attacks 
        atk.dmg += self.rage #+1 per rage
        return atk 
        
    def modDmg(self, atk: Attack) -> Attack:
        self.rageUpkeep(5) 
        return atk 
    
    def oneTimeAbility(self):
        if self.guardian:
            self.health += 10 
    
        
class KFDragon(Creature):
    
    def __init__(self):
        super(KFDragon, self).__init__("King Fire Dragon", ["Fire", "Dragon"], 60, \
                                       "+1 fire damage/other living non-minion fire creature you control\n"+ \
                                           "For every 5 damage taken +1 Rage\nFor every 5 health healed -1 Rage\n"+ \
                                               "Guardian: Give each other non-minion fire creature you control "+ \
                                                   "+1 fire damage/other living non-minion fire creature you control.\n", 2)
        self.attacks.append(Attack("Fire", 3, 3))
        self.attacks.append(Attack("Dragon", 3, 5, 3))
        self.getCreatureTypes = True 
        self.creatureTypes = [] #Counter for # of other fire creatures controlled - used to modify atks
        
    def __repr__(self):
        return "\n%s\t%d Health\n\n%s\n%s\n%s" % (self.name, self.health, self.tipo, str(self.attacks), self.ability)

    def modAttack(self, atk: Attack) -> Attack:
        #If multiple targets:
            #Have user choose which targets to damage, then distribute points normally 
        #Done this way for single-target attacks only
        if self.creatureTypes.count("Fire") > 0: 
            self.buffAttack(atk, self.creatureTypes.count("Fire") - 1, "Fire")
        return atk 

    def modAllyAttack(self, atk: Attack) -> Attack:
        if self.creatureTypes.count("Fire") > 0: 
            self.buffAttack(atk, self.creatureTypes.count("Fire") - 1, "Fire")
        return atk 

    def modDmg(self, atk: Attack) -> Attack:
        self.rageUpkeep(5) 
        return atk 
    
    
    

class Dragonling(Creature):
    
    def __init__(self):
        self.element = "void"
        super(Dragonling, self).__init__("Dragonling", ["Dragon"], 40, \
                                         "(Fire/Ice/Water) and dragon attacks cost 2E less for this creature (cannot cost less than 1E)"+ \
                                             " and do 2 less damage (cannot do less than 1 damage)\n", 1, ["Fire", "Water", "Ice"])
        self.attacks.append(Attack(self.element, 2, 3))
        self.rage = 0 
        self.getAllyData = True 
        self.allies = [] 
        
    def __repr__(self):
        return "\n%s\t%d Health\n\n%s %s\n%s\n%s\n" % (self.name, self.health, self.element, self.tipo, str(self.attacks), self.ability)

    def modAttack(self, atk: Attack) -> Attack:
        atk = self.buffAttack(atk, -2, [self.element, "Dragon"]) 
        atk = self.modEnergyCost(atk, -2, [self.element, "Dragon"]) 
        if atk.energyCost < 1:
            atk.energyCost = 1
        if atk.dmg < 1:
            atk.dmg = 1 
        return atk 
    
    def borrowAttacks(self):
        """
        Give creature the same built-in attacks as one allied creature.
        
        Must be called AFTER first call of player.updateAllyData() 
        """
        print(self.allies) 
        #Not bothering to do input validation yet 
        #Prevent choosing creatures without any printed attacks
        #Prevent choosing self
        temp = int(input("Choose an ally (by index) for Dragonling to borrow attacks from: ")) 
        ally = self.allies[temp] 
        print("Borrowing attacks from ", ally.name) 
        self.attacks = ally.attacks 
        
    def oneTimeAbility(self):
        self.borrowAttacks() 
        
    






