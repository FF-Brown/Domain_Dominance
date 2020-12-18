# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:57:58 2020

@author: Nathan
"""


class Ability(object):
    def __init__(self, desc="", used=False, resetAfterAtk=False, resetAfterTurn=False):
        self.desc = desc
        self.used = used 
        self.resetAfterAtk = resetAfterAtk 
        self.resetAfterTurn = resetAfterTurn 

