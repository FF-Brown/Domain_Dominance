# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:33:44 2020

@author: Nathan
"""

# from Player import Player 


class Attack(object):
    def __init__(self, tipo=[], dmg=0, energyCost=0, targets=1, divisible=False):
        if tipo == []:
            self.tipo = ["void"] 
        else:
            self.tipo = tipo 
        self.dmg = dmg 
        self.energyCost = energyCost 
        self.targets = targets 
        self.divisible = divisible 
        
    def __repr__(self):
        return "%d points %s damage to %d creatures for %d energy" % (self.dmg, self.tipo, self.targets, self.energyCost)


class Creature(object):
    
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
        
    def getAttack(self) -> int: 
        """Get user to choose an attack from list."""
        while True:
            for index, item in enumerate(self.attacks):
                print(index + 1,". ", self.attacks[index]) 
            atk = int(input("Choose an attack by number: "))
            if atk in range(1,len(self.attacks) + 1):
                break
            else: 
                print("Invalid entry")
        return atk - 1
            
    def attack(self) -> Attack:
        """Manage all other attacking functions in the Creature class."""
        while True:
            x = self.getAttack() #Put card attacks in this function? 
            temp = self.modAttack(self.attacks[x])              
            #If not enough energy: 
            if temp.energyCost > self.energy:
                print("Not enough energy for this attack.") 
                while True: #Input validation 
                    choice = input("Choose a different attack? (y/n) ").lower() 
                    if choice == 'n':
                        print("Chose not to attack with this creature.") 
                        return -1
                    elif choice != 'y':
                        print("Invalid entry.") 
            else:
                #Able to attack 
                self.energy -= temp.energyCost 
                self.AP = False 
                break 
        return temp
    
    def takeDmg(self, atk: Attack):
        """Modify an incoming attack as necessary, then subtract damage from health."""
        newAtk = self.modDmg(atk) 
        self.health = self.health - newAtk.dmg
        self.dmgTaken += newAtk.dmg 
        print("%s took %d damage. Health reduced to: " % self.name, newAtk.dmg, self.health) 
        
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

    def setElement(self): 
        """Have user choose an element for a Creature with variable element."""
        if len(self.elementList) > 0: #Only acts if there are items in the elementList
            print("Available elements: ", self.elementList) 
            while not self.element in self.elementList:
                print("Choose an element for your %s. " % self.name)
                self.element = input() 
                if not self.element in self.elementList:
                    print("Invalid entry.") 
            self.name = self.element + " " + self.name  
            self.tipo.insert(0,self.element) 

#STANDARD FUNCTIONS FOR MODIFYING DAMAGE~~~~~~~~~~~~~~~~~~~~~~
    def modAttack(self, atk: Attack) -> Attack:
        """Allow Creature to modify its own outgoing attacks. To be overwritten."""
        return atk
    
    def modAllyAttack(self, atk: Attack) -> Attack:
        """Allow Creature to modify an ally's outgoing attack. TO be overwritten."""
        return atk 
    
    def externalUpkeep(self):
        #TRASH 
        #To be overwritten. Allows creatures upkeep abilities related to their surroundings
        #TRASH 
        pass
    
    def modDmg(self, atk: "Attack") -> Attack:
        """Allow Creature to modify or record damage from incoming attacks."""
        return atk 

    def rageUpkeep(self, dmgPerRage):
        """Determines rage based on damage taken. For use in modDmg()."""
        self.rage = self.dmgTaken % dmgPerRage  
        print("Rage: ", self.rage) #For testing purposes 

    def buffAttack(self, atk: Attack, damageModifier: int, elementDependence: list=None) -> Attack:
        """
        Buff/debuff an attack, optionally based on its type. For use in modAttack() and modDmg().

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

        """
        if elementDependence == None:
            atk.dmg += damageModifier 
        else: 
            if atk.tipo in elementDependence:
                atk.dmg += damageModifier
        return atk
    
    def modEnergyCost(self, atk: Attack, energyModifier: int, elementDependence: list=None) -> Attack:
        """Raise/lower energy cost of an attack, optionally basaed on its type. For use in modAttack()."""
        if elementDependence == None:
            atk.energyCost += energyModifier  
        else:
            if atk.tipo in elementDependence:
                atk.energyCost += energyModifier 
        return atk
    
    def oneTimeAbility(self):
        """Allow Creature to use any one-time abilities triggered at the beginning of the game. To be overwriten."""
        print() 
        
    
    
    
    
    
    
    
    
    
    
    