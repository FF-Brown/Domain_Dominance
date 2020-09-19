# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 23:04:07 2020

@author: Nathan
"""


from Menu import mainMenu, mainMenuOptions
import Player as pl
from Creature import Attack
from Game import Game
import logging

logger = logging.getLogger("dd")
logger.setLevel(logging.INFO)
fh = logging.FileHandler("./tests/dd.log")
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt =  "%Y-%m-%d %H:%M")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)


# print("Hasn't broken yet.")
logger.info('Not broken yet')
# logger.warning("Is it broken? Probably not.") 

game = Game()
game.play() 

# option = mainMenu()
# mainMenuOptions(option)
# if option != 3:
#     #Play ball
    


#     # while p1.alive and p2.alive:
#     #     print(p1.displayCards())
#     #     print(p2.displayCards()) 
#         #response = input("Choose a champion to attack with: ")
        
#     pass