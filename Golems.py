# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 02:14:35 2020

@author: Nathan
"""

from Creature import Creature
from Creature import Attack
import logging

logger_golems = logging.getLogger('dd.golems') 

class SpGolem(Creature):
    def __init__(self):
        logger_golems.info("Creating SpGolem.") 
        super(SpGolem,self).__init__("Spike Golem", ["Golem"], 40, "Whenever a creature attacks this creature with a melee attack,"+ \
                                     " this creature deals 2 damage to that creature.", 2)
        self.attacks.append(Attack("", 4, 4))
        
    def __repr__(self):
        return "\n%s\t%d Health\n\n%s\n%s\n%s" % (self.name, self.health, self.tipo, str(self.attacks), self.ability)

class CGolem(Creature):
    def __init__(self):
        logger_golems.info("Creating CGolem.") 
        self.element = "void"
        super(CGolem,self).__init__("Golem", ["Golem"], 55, "+2 (Fire/Water/Ice) Protection", 2, ["Fire", "Water", "Ice"]) 
        self.attacks.append(Attack(self.element, 1, 1))
        self.attacks.append(Attack(self.element, 2))
    def __repr__(self):
        return "\n%s\t%d Health\n\n%s %s\n%s\n%s" % (self.name, self.health, self.element, self.tipo, str(self.attacks), self.ability)
    def modDmg(self, atk: Attack) -> Attack:
        atk = self.buffAttack(atk, -2, [self.element])
        return atk

class MiGolem(Creature):
    def __init__(self):
        logger_golems.info("Creating MiGolem.") 
        super(MiGolem, self).__init__("Mirrored Golem", ["Golem"], 50, "Whenever a creature attacks and deals damage" + \
                                      " to this creature that creature takes damage equal to half (rounded down)" + \
                                          " the damage taken by this creature.", 2)
        self.attacks.append(Attack("", 2, 2))
        self.attacks.append(Attack("", 4))
    def __repr__(self):
        return "\n%s\t%d Health\n\n%s\n%s\n%s" % (self.name, self.health, self.tipo, str(self.attacks), self.ability)
