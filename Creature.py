# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:33:44 2020

@author: Nathan
"""

# from Player import Player 
import logging

logging_creature = logging.getLogger('dd.creature') 

class Attack(object):
    """
    Represents either one attack or the part of an attack targeting one creature.

    ...

    Attributes
    ----------
    tipo : - str
        damage type if any, i.e. Fire 
    dmg : - int
        amount of damage dealt 
    energyCost : - int
        amount of energy required for use 
    targets : - int
        max number of targets possible 
    divisible : - bool 
        whether damage should be divided between targets 
    target : - Creature
        what Creature is being targeted 
    """
    def __init__(self, tipo=[], dmg=0, energyCost=0, targets=1, divisible=False, target=None, needsReset=False, active=True):
        if tipo == []:
            self.tipo = ["void"] 
        else:
            self.tipo = tipo 
        self.dmg = dmg 
        self.energyCost = energyCost 
        self.targets = targets 
        self.divisible = divisible 
        self.target = target 
        #Remove in case of a divisible attack with limited number of targets 
        if self.divisible == True and targets == 1:
            self.targets = dmg 
        
    def __repr__(self):
        if self.target == None:
            return "%d points %s damage to %d creatures for %d energy" % (self.dmg, self.tipo, self.targets, self.energyCost)
        else: 
            return "%d points %s damage to %s for %d energy" % (self.dmg, self.tipo, self.target.name, self.energyCost)


class Creature(object):
    """
    Any kind of creature a player may have.

    ...

    Attributes
    ----------
    name : str
        creature name 
    tipo : list
        creature type(s)  
    health : int
        amount of health remaining  
    ability : str
        description of creature ability 
    energyUpkeep : int 
        amount of energy received per turn 
    elementList : list
        creature element(s) if any
    guardian : bool
        whether creature appointed as guardian 
    dmgTaken : int
        damage taken by creature so far 
    getCreatureTypes : bool
        whether creature should be informed of ally types
    getAllyData : bool 
        whether creature should have access to allies 

    Methods
    -------
    getAttack() -> int:
        Get user to choose an attack from list.
    More forthcoming. 
    """

    def __init__(self, name, tipo, health, ability, energyUpkeep, elementList=[], guardian=False): 
        self.name = name
        self.tipo = tipo
        self.health = health
        self.ability = ability 
        self.attacks = []
        self.energy = 0
        self.energyUpkeep = energyUpkeep
        self.AP = False 
        self.elementList = elementList 
        self.setElement() 
        self.guardian = guardian 
        self.dmgTaken = 0 
        self.getCreatureTypes = False 
        self.getAllyData = False 
        self.abilities = [] 
        
    def getAttack(self) -> int: 
        """Get user to choose an attack from list."""
        logging_creature.info("Choosing attack from list.") 
        while True:
            for index, item in enumerate(self.attacks):
                print(index + 1,". ", self.attacks[index]) 
            atk = int(input("Choose an attack by number: "))
            if atk in range(1,len(self.attacks) + 1):
                break
            else: 
                print("Invalid entry")
        return atk - 1
            
    def hasEnergy(self, attack: Attack) -> bool:
        """Check if creature has enouh energy for a given attack. Can be overridden if an ability affects this."""
        if attack.energyCost > self.energy:
            return False
        else:
            return True 
    
    def attack(self) -> Attack:
        """
        Manage all other attacking functions in the Creature class. 
        Calls self.getAttack() for user input
        No longer calls self.modAttack()
        Checks if creature has enough energy for the attack.
    
        Parameters
        ----------
        None

        Returns
        -------
        atk : - Attack
            The attack chosen by user from self.attacks[]. 
        Returns -1 if player chose not to attack with this creature.
    
        Example
        -------
        atk = attacker.attack() 
        outgoingAttacks.append(atk) 
        
        Called by
        ---------
        player.battle() 
        
        Calls
        -----
        getAttack()
        hasEnergy()
    
        """
    
        logging_creature.info(self.name + " is attacking.")  
        while True:
            x = self.getAttack() #Put card attacks in this function? 
            atk = self.attacks[x] 
             
            #If not enough energy: 
            if not self.hasEnergy(atk):
                print("Not enough energy for this attack.") 
                while True: #Input validation 
                    choice = input("Choose a different attack? (y/n) ").lower() 
                    if choice == 'n':
                        print("Chose not to attack with this creature.") 
                        return -1
                    elif choice == 'y':
                        print("Choosing a different attack.") 
                        break
                    else: 
                        print("Invalid entry.") 
                        break 
            else:
                #Able to attack 
                self.energy -= atk.energyCost 
                self.AP = False 
                break 
        return atk
    
    def takeDmg(self, atk: Attack):
        """Modify an incoming attack as necessary, then subtract damage from health.
        
        Called by
        ---------
        receiveAttack() 
        
        Calls
        -----
        modDmg() 
        """
        logging_creature.info("In takeDmg()...") 
        logging_creature.info(self.name + " taking damage.") 
        logging_creature.info("Attack: " + str(atk)) 
        newAtk = self.modDmg(atk) 
        logging_creature.info("Attack returned by modDmg(): " + str(newAtk)) 
        self.health = self.health - newAtk.dmg 
        self.dmgTaken += newAtk.dmg 
        print("%s took %d damage. Health reduced to: %d" % (self.name, newAtk.dmg, self.health)) 
        
    def isAlive(self) -> bool:
        """Allow Player to check if Creature is alive."""
        if self.health <= 0:
            return False
        else:
            return True
        
    def addEnergy(self):
        """Add energy based on Creature's unique energy upkeep. Upkeep function."""
        self.energy += self.energyUpkeep 
        
    def resetAP(self):
        """Give creature AP. Upkeep function."""
        self.AP = True  
        logging_creature.debug("Resetting AP for ", self.name) 

    def setElement(self): 
        """Have user choose an element for a Creature with variable element."""
        if len(self.elementList) > 0: #Only acts if there are items in the elementList
            logging_creature.info("Selecting element.") 
            print("Available elements: ", self.elementList) 
            while not self.element in self.elementList:
                print("Choose an element for your %s. " % self.name)
                self.element = input().capitalize() 
                if not self.element in self.elementList:
                    print("Invalid entry.") 
            self.name = self.element + " " + self.name  
            self.tipo.insert(0,self.element) 

#STANDARD FUNCTIONS FOR MODIFYING DAMAGE~~~~~~~~~~~~~~~~~~~~~~
    def modAttack(self, atks: list) -> list:
        """Allow Creature to modify its own outgoing attacks. To be overwritten.
        
        Called by
        ---------
        buffOutgoing() 
        """
        pass 
    
    def modAllyAttack(self, atks: list) -> list:
        """Allow Creature to modify an ally's outgoing attack. To be overwritten.
        
        Called by
        ---------
        buffOutgoing() 
        """
        pass 
    
    def modDmg(self, atk: "Attack") -> Attack:
        """Allow Creature to modify or record damage from incoming attacks.
        MUST RETURN ATK
        
        Called by
        ---------
        creature.takeDmg() 
        """
        return atk 

    def rageUpkeep(self, dmgPerRage):
        """Determines rage based on damage taken. For use in modDmg()."""
        self.rage = self.dmgTaken % dmgPerRage  
        print("Rage: ", self.rage) #For testing purposes 

    def buffAttack(self, atk: Attack, damageModifier: int, elementDependence: list=None):
        """
        Buff/debuff an attack, optionally based on its type. For use in modAttack() and modDmg().
        SUPPORT FOR LISTS REMOVED 12/14/2020 

        Parameters
        ----------
        atk : Attack
            The attack to be modified.
        damageModifier : int
            Positive for buffs, negative for debuffs.
        elementDependence : list
            Only included if the ability is dependent on type. The default is None.

        Returns
        -------
        Attack
            The modified attack.

        Called by
        ---------
        modAttack()
        modDmg()
        
        Calls
        -----
        None
        """
        if elementDependence == None:
            atk.dmg += damageModifier 
        else: 
            #Apply modifier if requirement met 
            for value in atk.tipo:
                if value in elementDependence:
                    atk.dmg += damageModifier 
                    return atk 
        return atk 
    
    def modEnergyCost(self, atk: Attack, energyModifier: int, elementDependence: list=None) -> Attack:
        """Raise/lower energy cost of an attack, optionally based on its type. For use in modAttack()."""
        if elementDependence == None:
            atk.energyCost += energyModifier  
        else:
            if atk.tipo in elementDependence:
                atk.energyCost += energyModifier 
        return atk
    
    def oneTimeAbility(self):
        """Allow Creature to use any one-time abilities triggered at the beginning of the game. To be overwriten."""
        pass 
        
    def resetAbilities(self):
        """First draft for resetting abilities that get triggered once per attack or once per turn."""
        for ability in self.abilities:
            if ability.resetAfterAtk:
                ability.used = False 
    
    def modAllyIncoming(self, atk: Attack) -> Attack:
        """
        Allow modification of attacks targeting allies for creatures with ability to do so. Overwritten by individual creature classes. 

        Parameters
        ----------
        atk : Attack
            The attack to be modified.

        Returns
        -------
        Modified attack
        
        Called by 
        ---------
        player.receiveAttack() 

        """
        
        return atk  
    
    
    
    
    
    
    
    