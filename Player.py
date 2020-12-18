 # -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 01:31:28 2020

@author: Nathan
"""
from Dragons import *
from Golems import *
from Creature import Attack 
from Creature import Creature 
import logging
import copy 

logger_player = logging.getLogger('dd.player') 

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

    def chooseCreature(self) -> Creature: 
        """
        Allow user to choose a creature to attack with.
        Called by player.battle(). Does not display creature list. 
    
        Parameters
        ----------
        None

        Returns
        -------
        self.field[x] : - Creature
            The creature at index x, chosen by user.
    
        Example
        -------
        attacker = chooseCreature()
        attacker.attack() 
        
        Notes
        -------
        Consider renaming "chooseAttacker()". Choosing a creature is what it actually does, so it could be used for other things. However, it only gets used for choosing an attacker, so that could be better since it would make it more obvious what it is for.
    
        """
        while True:
            choice = input("Choose a creature (by index): ")
            logger_player.debug("User entered ", choice) 
            result = self.field[int(choice)] 
            logger_player.debug("Corresponds to ", result.name) 
            if result.AP:
                return result
            else:
                return -1
            print("Invalid entry.") 
                
            # for x in range(len(self.field)):
            #     if choice == self.field[x].name:
            #         if self.field[x].AP:
            #             return self.field[x]  
            #         else: #No AP, creature already used its action 
            #             return -1 
            # print("Invalid entry.")
                
    def battle(self, opponent: "Player"): 
        print(self.getCards()) 
        while True:
            #Choosing a creature to attack with                    
            while True:
                creature = self.chooseCreature() #Reports -1 if no AP 
                if type(creature) == int: 
                    print("Creature has already used its action.")
                    choice = input("Choose another creature? (y/n) ").lower() 
                    if choice == 'n':
                        print("Decided not to attack.") 
                        return 
                    #Otherwise, loops to choose another creature 
                else: #Player chose a creature 
                    break 
            
            #Choosing an attack 
            atk = creature.attack() 
            if type(atk) == int: #Chose not to attack with that creature 
                choice = input("Choose another creature? (y/n) ").lower() 
                if choice == 'n':
                    print("Decided not to attack.") 
                    return
            else: #proceeding with attack 
                break 
            
        #Make atk into a list - may need to be moved earlier at some point 
        atkList = []
        atkList.append(atk) 
        
        # logger_player.info("atk type: " + str(type(atk))) 
        # logger_player.info("atk contents: " + str(atk)) 

        logger_player.info("atkList type: " + str(type(atkList))) 
        logger_player.info("atkList contents: " + str(atkList)) 

        
        #Target and allies buff attack 
        self.buffOutgoing(creature, atkList) 
        
        #Player chooses targets for attack(s) 
        self.assignTargets(atkList, opponent) 
            
        #Pass attack(s) to opponent
        opponent.receiveAttack(atkList) 
                            
    def buffOutgoing(self, attacker: Creature, attacks: list):
        """
        Allow attacker to modify the attack(s), then allow allies to do so. 
    
        Parameters
        ----------
        attacker : Creature, attacks : list of Attacks

        Returns
        -------
        Nothing. Changes to list are simply retained.
    
        Called by
        ---------
        player.battle()
        
        Calls
        -----
        creature.modAttack()
        creature.modAllyAttack() 
            
        """
        attacker.modAttack(attacks)
        for creature in self.field:
            if creature != attacker:
                creature.modAllyAttack(attacks) 
                
    def singleTargetAttack(self, atk: Attack, opponent: "Player"):
        print("Available targets: ") 
        print(opponent.getCards()) 
        target = opponent.chooseTarget() 
        opponent.field[target].takeDmg(atk) 
        
    def multiTargetAttack(self, atk: Attack, opponent: "Player"):
        print("Targeting all enemy champions.") 
        for creature in opponent.field:
            creature.takeDmg(atk) 
            
    def divideAttack(self, atk: Attack, opponent: "Player") -> list:
        """
        Allow player to choose targets for a divisible attack. 
        Called by assignTargets() 
    
        Parameters
        ----------
        atks : Attack\n 
        opponent : Player

        Returns
        -------
        List of Attacks 
    
        Example
        -------
        if atk.divisible: newAtks = divideAttack(atk, opponent) 
    
        """
        #Display number of allowed targets (int) 
        #Display enemy creatures
        #Choose a target creature 
            #If number of targets left is 1, allocate all remaining dmg 
            #Else subtract 1 from targets: begin getDmg() 
            #Show how much dmg exists to be allocated (atk.dmg)
            #Player chooses how much dmg to allocate 
            #Create new attack with chosen target and dmg 
            #End getDmg() 
            #If returned dmg == 0, don't subtract 1 from targets  
            #Else:
            #Subtract dmg from original atk
            #Append new attack to list 
        
        logger_player.info("In divideAttack()...") 
        
        #List that will be returned 
        newAtks = [] 
        #Attack object to modify and used to populate newAtks 
        newAtk = Attack() 
        
        #Continue assigning damage as long as there is damage left
        #and targets to choose 
        while(atk.targets > 0 and atk.dmg > 0):
            print("Targets left: ", atk.targets) 
            
            #Choose a target
            currentTarget = self.chooseTarget(opponent) 
            
            print("Target chosen: ", currentTarget.name) 
            
            #Copy essential elements from atk into newAtk 
            #Can be replaced with copy.deepcopy() 
            newAtk.tipo = atk.tipo 
            newAtk.dmg = atk.dmg 
            # logger_player.info("Before Dmg:" + str(newAtk.dmg)) 
            newAtk.energyCost = atk.energyCost 
            newAtk.targets = 1 
            newAtk.divisible = False 
            newAtk.target = currentTarget 
            
            #If only 1 target left 
            if atk.targets == 1:
                print("Last target. Assigning remaining", atk.dmg, "points of damage to", currentTarget.name) 
                # logger_player.info("Remaining damage. Dmg:" + str(newAtk.dmg))
                newAtks.append(copy.deepcopy(newAtk))
                atk.targets -= 1 
                
            else: 
                #Get damage
                damage = self.getDmg(atk) 
                # logger_player.info("Input damage:" + str(damage)) 
                if damage == 0:
                    print("Chose not to attack", currentTarget.name, ".")  
                else: 
                    print("Appending attack.") 
                    newAtk.dmg = damage 
                    # logger_player.info("Assigned damage:" + str(newAtk.dmg))
                    atk.dmg -= damage 
                    # logger_player.info("Updated atk damage:" + str(atk.dmg)) 
                    newAtks.append(copy.deepcopy(newAtk))
                    atk.targets -= 1
                    
        #For testing 
        print("Damage split as follows: ") 
        print(newAtks) 
        for x in newAtks:
            print(x.dmg, "damage for", x.target.name) 
            
        logger_player.info("Returning from divideAttack() " + str(newAtks)) 
        return newAtks 
    
    def assignTargets(self, atks: list, opponent):
        """
        Allow player to choose targets for all outgoing attacks. 
        Called by battle() 
    
        Parameters
        ----------
        atks : list\n 
        opponent : Player 

        Returns
        -------
        None. List modifications are retained after function call ends.
    
        Example
        -------
        assignTargets(atks)  
    
        """
        for atk in atks:
            # logger_player.info("atk type: " + str(type(atk)))
            # logger_player.info("atks type: " + str(type(atks))) 
            logger_player.info("atk contents: " + str(atk)) 
            logger_player.info("atks contents: " + str(atks)) 
            if atk.divisible:
                logger_player.info("\nDividing attack: " + str(atk)) 
                print("Dividing attack: ", atk) 
                dividedAtk = self.divideAttack(atk, opponent)
                atks.remove(atk) 
                for x in dividedAtk:
                    atks.append(x) 
            else: 
                if atk.target == None:
                    print("Assigning target for:", atk) 
                    logger_player.info("Assigning target for: " + str(atk)) 
                    atk.target = self.chooseTarget(opponent) 
                
    def getDmg(self, atk: Attack) -> int:
        #Display damage
        while True:
            print(atk.dmg, " damage available.") 
            choice = int(input("How much damage would you like to assign to this target?")) 
            if choice > atk.dmg or choice < 0:
                print("Invalid entry. Please enter a number between 0 and ", atk.dmg) 
            else: 
                return choice 
        
                
    def chooseTarget(self, opponent) -> Creature: 
        """
        Choose a creature from enemy's field as target for an attack. 
        Called by assignTargets() and divideAttack() 
    
        Parameters
        ----------
        opponent : - Player 

        Returns
        -------
        target : - Creature
    
        Example
        -------
        target = chooseTarget(opponent) 
    
        """

        while True:
            print(opponent.getCards()) 
            choice = int(input("Choose a creature (by index): ")) 
            
            if choice in range(len(opponent.field)):
                target = opponent.field[choice]
                return target 
            else:
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
        choice = input("Choose a creature to make guardian (by index): ")
        #Input validation 
        self.field[int(choice)].guardian = True 
        print("Appointed %s as guardian." % self.field[int(choice)].name) 
            
        
    def updateCreatureInfo(self):
        """Allows creatures to request info on allies by setting the getCreatureTypes variable to True
        
        Built to accomodate one of King Fire Dragon's abilities.
        """
        types = [] 
        for creature in self.field:
            types += creature.tipo 

        for creature in self.field:
            if creature.getCreatureTypes:
                creature.creatureTypes = types 
                
    def updateAllyData(self):
        for creature in self.field:
            if creature.getAllyData == True:
                #Remove the creature from the list
                temp = self.field 
                #Is this needed? Note that temp is a reference, not a copy 
                #temp.remove(creature) 
                creature.allies = temp 
                    
    def healthUpkeep(self):
        #Remove any creatures that are dead 
        pass
    
    def activateOTA(self):
        """Run One-Time Ability functions of all creatures"""
        for creature in self.field:
            creature.oneTimeAbility() 
        
    def receiveAttack(self, incomingAttacks: list):
        """
        Take a list of attacks from opponent and pass it to targets/allies as appropriate. 

        Parameters
        ----------
        incomingAttacks : list of Attacks 
            The attacks to be passed.

        Returns
        -------
        None.
        
        Called by
        ---------
        Player.battle() 
        
        Function Calls
        --------------
        modAllyIncoming() 
        takeDmg() 

        """
        
        logger_player.info("In receiveAttack()...") 
        logger_player.info("incomingAttacks contents: " + str(incomingAttacks)) 
        

        for attack in incomingAttacks:
            logger_player.info("attack type: " + str(type(attack))) 
            logger_player.info("attack contents: " + str(attack))
            
            #modAllyIncoming for each creature that is not the target
            for creature in self.field:
                if not creature == attack.target:
                    attack = creature.modAllyIncoming(attack) 
                    
            #pass attack to target using takeDmg()
            attack.target.takeDmg(attack) 
            #resetAbilities() 
                    
            
            
            
            
            
            
            
            
            
            
            
            
            
            




