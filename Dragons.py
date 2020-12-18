# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:32:54 2020

@author: Nathan
"""

from Creature import Creature
from Creature import Attack
import logging

logger_dragons = logging.getLogger('dd.dragons') 

class EFDragon(Creature):
        
    def __init__(self):
        logger_dragons.info("Creating EFDragon.") 
        super(EFDragon, self).__init__("Elder Fire Dragon", ["Fire", "Dragon"], 70, "+2 Fire Attacks\n-2 Fire Damage\n+1 Attack/Rage\n" + "For every 5 damage taken +1 Rage\n" + "For every 5 health healed -1 Rage\nGuardian +10 Health\n", 2)
        self.attacks.append(Attack("Fire", dmg=3, energyCost=2))
        self.rage = 0 
        
    def __repr__(self):
        return "\n%s\t%d Health\n\n%s\n%s\n%s" % (self.name, self.health, self.tipo, str(self.attacks), self.ability)
    
    def modAttack(self, atks: list) -> list: 
        for atk in atks:
            atk = self.buffAttack(atk, 2, ["Fire"]) #+2 to Fire-type attacks 
        atks[0].dmg += self.rage #+1 per rage 
        
    def modDmg(self, atk: Attack) -> Attack:
        """May change name to modIncomingAtk()"""
        self.rageUpkeep(5) 
        return atk 
    
    def oneTimeAbility(self):
        if self.guardian:
            self.health += 10 
    
        
class KFDragon(Creature):
    
    def __init__(self):
        logger_dragons.info("Creating KFDragon.") 
        super(KFDragon, self).__init__("King Fire Dragon", ["Fire", "Dragon"], 60, "+1 fire damage/other living non-minion fire creature you control\n" + "For every 5 damage taken +1 Rage\nFor every 5 health healed -1 Rage\n" + "Guardian: Give each other non-minion fire creature you control " + "+1 fire damage/other living non-minion fire creature you control.\n", energyUpkeep=2)
        self.attacks.append(Attack("Fire", dmg=3, energyCost=3)) 
        self.attacks.append(Attack("Dragon", dmg=3, energyCost=5, targets=3)) 
        self.getCreatureTypes = True 
        self.creatureTypes = [] #Counter for # of other fire creatures controlled - used to modify atks
        
    def __repr__(self):
        return "\n%s\t%d Health\n\n%s\n%s\n%s" % (self.name, self.health, self.tipo, str(self.attacks), self.ability)

    def modAttack(self, atks: list) -> list:
        fireCount = self.creatureTypes.count("Fire")
        if fireCount > 0 and "Fire" in atks[0].tipo: 
            atks.append(Attack(tipo=["Fire"],dmg=fireCount-1,divisible=True)) 

    def modAllyAttack(self, atks: list):
        logger_dragons.info("KFDragon is modifying ally's attack.")
        logger_dragons.info("Current attack list: " + str(atks))
        fireCount = self.creatureTypes.count("Fire")
        logger_dragons.info("Number of fire creatures: " + str(fireCount)) 
        if fireCount > 0 and "Fire" in atks[0].tipo: 
            # self.buffAttack(atks, fireCount - 1, "Fire") 
            logger_dragons.info("Appending attack.")
            atks.append(Attack(tipo=["Fire"],dmg=fireCount-1,divisible=True))
            logger_dragons.info("New attack list: " + str(atks)) 
            print("\nKFDragon has modified attack. New attack list: ", str(atks), "\n") 

    def modDmg(self, atk: Attack) -> Attack:
        self.rageUpkeep(5) 
        return atk 
    
    

class Dragonling(Creature):
    
    def __init__(self):
        logger_dragons.info("Creating Dragonling.") 
        self.element = "void"
        super(Dragonling, self).__init__("Dragonling", ["Dragon"], health=40, ability="(Fire/Ice/Water) and dragon attacks cost 2E less for this creature (cannot cost less than 1E) and do 2 less damage (cannot do less than 1 damage)\n", energyUpkeep=1, elementList=["Fire", "Water", "Ice"])
        self.attacks.append(Attack(self.element, 2, 3))
        self.rage = 0 
        self.getAllyData = True 
        self.allies = [] 
        
    def __repr__(self):
        return "\n%s\t%d Health\n\n%s %s\n%s\n%s\n" % (self.name, self.health, self.element, self.tipo, str(self.attacks), self.ability)

    def modAttack(self, atks: list): 
        if atks[0].dmg < 4:
            debuff = -1 * (atks[0].dmg - 1)
        else:
            debuff = -2
        for atk in atks:
            atk = self.buffAttack(atk, debuff, [self.element, "Dragon"]) 
    
    def borrowAttacks(self):
        """
        Give creature the same built-in attacks as one allied creature.
        
        Must be called AFTER first call of player.updateAllyData() 
        """
        logger_dragons.info("Dragonling is borrowing attacks.") 
        print(self.allies) 
        #Not bothering to do input validation yet 
        #Prevent choosing creatures without any printed attacks - or perhaps not, in case neither ally has any
        #Prevent choosing self 
        #Prevent entering index outside of list 
        temp = int(input("Choose an ally (by index) for Dragonling to borrow attacks from: ")) 
        ally = self.allies[temp] 
        print("Borrowing attacks from ", ally.name) 
        self.attacks = ally.attacks 
        
    def oneTimeAbility(self):
        self.borrowAttacks() 
    
    def hasEnergy(self, attack: Attack) -> bool:
        """If attack shares type with Dragonling, reduce energyCost by 2, but can't go below 1."""
        
        if self.element in attack.tipo or "Dragon" in attack.tipo:
            logger_dragons.info("Applying Dragonling energy ability.") 
            if attack.energyCost > 1:
                logger_dragons.info("Reducing energy cost.") 
                attack.energyCost -= 2
                logger_dragons.info("Energy cost reduced to " + str(attack.energyCost))
                if attack.energyCost < 1:
                    logger_dragons.info("Adjusting energy cost to be >= 1") 
                    attack.energyCost = 1 
        
        return super(Dragonling, self).hasEnergy(attack) 
        
    






