# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 01:31:28 2020

@author: Nathan
"""
from Dragons import *
from Golems import *
from Creature import Attack 
from Creature import Creature 

class Player(object):
    
    
    
    def __init__(self, playerNum, deckFile):
        self.coin = 0
        self.deck = []
        self.hand = []
        self.field = []
        self.alive = True 
        self.num = playerNum 
        #Put this in its own function 
        with open(deckFile, "r") as inFile:
            inFile.readline()
            cards = inFile.read()
        cards = cards.split('\n')
        cards = cards[0:3] #Won't be necessary once cards other than creatures are implemented
        cards = ",".join(cards)
        cards = cards.split(',')
        cards = cards[1::2]
        for x in range(3):
            #e.g. self.field.append(EFDragon())     r is necessary for formatting 
            phrase = r"self.field.append(" + cards[x] + r"())"
            eval(phrase) 
        self.getGuardian() 
        self.updateAllyData() 
        self.activateOTA() 
        
            
    def getCards(self):
        names = []
        for creature in self.field:
            names.append(creature.name)
        return names 

    def chooseCreature(self): #For choosing a creature to attack with 
        while True:
            choice = input("Choose a creature: ")
                
            for x in range(len(self.field)):
                if choice == self.field[x].name:
                    if self.field[x].AP:
                        return x 
                    else:
                        print("Creature has already used its action.") 
                        return -1 
            print("Invalid entry.")
                
    def battle(self, opponent: "Player"): 
        print(self.getCards()) 
        while True:
        #Choosing a creature to attack with                    
            while True:
                creature = self.chooseCreature() #Reports -1 if no AP 
                if creature == -1: 
                    choice = input("Choose another creature? (y/n) ").lower() 
                    if choice == 'n':
                        print("Decided not to attack.") 
                        return 
                    #Otherwise, loops to choose another creature
                else:
                    break 
            
            #Choosing an attack 
            atk = self.field[creature].attack() 
            if type(atk) == int: #Chose not to attack with that creature 
                choice = input("Choose another creature? (y/n) ").lower() 
                if choice == 'n':
                    print("Decided not to attack.") 
                    return
            else:
                break 
        #Attacking 
        #IF LIST
        # Rambling thoughts: If the attack targets only 1 creature, we COULD have a list because the attack could be a fire attack
            #and the creature could have an equipment that adds damage of another type. So we would have to add that as another 
            #attack on the list. What a crappy situation that will be for Future Me to deal with. Now. That's the only situation
            #in which we would have a list for a single-target attack. If the attack targets multiple enemies and gains a per-enemy
            #buff, we won't need a list - unless, again, the buff is a different type. But idk how to deal with that yet. 
            #The main case in which we'll have a list is when the attack targets multiple enemies and the buff or buffs is/are 
            #divisble. So let's just focus on that case and worry about the other two cases later. 
        if type(atk) == list:
            for attack in atk:
                if attack.divisible:
                    
                    pass
                else:
                    if atk.targets == 3:
                        self.multiTargetAttack(atk, opponent)  
                    else:
                        self.singleTargetAttack(atk, opponent) 
        #IF NOT LIST 
        else:
            if atk.targets == 3:
                self.multiTargetAttack(atk, opponent)  
            else:
                self.singleTargetAttack(atk, opponent) 
                
    def singleTargetAttack(self, atk: Attack, opponent: "Player"):
        print("Available targets: ") 
        print(opponent.getCards()) 
        target = opponent.chooseTarget() 
        opponent.field[target].takeDmg(atk) 
        
    def multiTargetAttack(self, atk: Attack, opponent: "Player"):
        print("Targeting all enemy champions.") 
        for creature in opponent.field:
            creature.takeDmg(atk) 
            
    def divisibleAttack(self, atk: Attack, opponent: "Player"):
        """Allow player to divide damage from an attack as desired."""
        #Display enemy creatures
        #For each creature:
            #Show base dmg
            #While floating dmg exists, offer to allocate it
            #If last creature, add in all remaining floating dmg 
        pass
                
    def chooseTarget(self): 
        """For opponent's use. Allows opponent to choose target from self.field."""
        while True:
            choice = input("Choose a creature: ")
                
            for x in range(len(self.field)):
                if choice == self.field[x].name:
                    return x 
            print("Invalid entry.")
        
        
    def upkeep(self):
        self.energyUpkeep() 
        self.APUpkeep() 
        self.updateCreatureInfo() 
        
    def energyUpkeep(self):
        for creature in self.field:
            creature.addEnergy() 
    
    def APUpkeep(self):
        for creature in self.field: 
            creature.resetAP() 
            
    def hasAPLeft(self):
        result = False
        for creature in self.field:
            if creature.AP:
                result = True
        return result 
    
    def attackAgain(self):
        while True:
            choice = input("Would you like to attack again? (y/n) ") 
            if choice == 'y' or choice == 'n':
                return choice
            else:
                print("Invalid entry.") 
        
    def getGuardian(self):
        print(self.getCards()) 
        while True:
            choice = input("Choose which of your creatures you would like to have as guardian: ")
                
            for x in range(len(self.field)):
                if choice == self.field[x].name:
                    self.field[x].guardian = True
                    print("Appointed %s as guardian." % self.field[x].name) 
                    return 
            print("Invalid entry.")
        
    def updateCreatureInfo(self):
        """Allows creatures to request info on allies by setting the getCreatureTypes variable to True
        
        Built to accomodate one of King Fire Dragon's abilities.
        """
        types = [] 
        for creature in self.field:
            types += creature.tipo 
            # types.append(creature.tipo) 
        for creature in self.field:
            if creature.getCreatureTypes:
                creature.creatureTypes = types 
                
    def updateAllyData(self):
        for creature in self.field:
            if creature.getAllyData == True:
                # print("Sending ally data...") 
                #Remove the creature from the list
                temp = self.field 
                #For some reason removes creature from self.field? Should be 
                #working with a copy of self.field. 
                #temp.remove(creature) 
                creature.allies = temp 
                    
    def healthUpkeep(self):
        #Remove any creatures that are dead 
        pass
    
    def activateOTA(self):
        """Run One-Time Ability functions of all creatures"""
        for creature in self.field:
            creature.oneTimeAbility() 
        





