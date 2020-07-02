# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:27:24 2020

@author: Nathan
"""


import Player as pl

class Game(object):
    
    def __init__(self):
        self.player1 = pl.Player(1, r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Documents\TestDeck.csv")
        self.player2 = pl.Player(2, r"C:\Users\Nathan\Documents\Drive Sync\Domain_Dominance\Documents\TestDeck2.csv")
        self.turn = 0
        self.currentPlayer = self.player1
        self.opponent = self.player2 
        
    def play(self):
        while self.player1.alive and self.player2.alive:
            self.setCurrentPlayer() 
            self.takeTurn() 
            self.turn += 1 
            
        if self.player1.alive:
            print("Congratulations, Player 1! You win!")
        else:
            print("Congratulations, Player 2! You win!")

    def takeTurn(self):
        print("\nPlayer ", self.current, " turn") 
        self.currentPlayer.upkeep()
        while True: #Input validation 
            print(self.currentPlayer.getCards()) 
            choice = input("Would you like to attack? (y/n) ").lower() 
            if choice == 'n':
                print("Chose not to attack.") 
                break 
            elif choice == 'y':
                while True:
                    self.currentPlayer.battle(self.opponent) 
                    if self.currentPlayer.hasAPLeft():
                        choice = self.currentPlayer.attackAgain() 
                        if choice == 'n':
                            print("End of turn.\n") 
                            break 
                    else:
                        break 
                break 
            else:
                print("Invalid entry.") 

    def setCurrentPlayer(self):
        self.current = self.turn % 2 + 1
        
        if self.current == 1:
            self.currentPlayer = self.player1
            self.opponent = self.player2
        elif self.current == 2:
            self.currentPlayer = self.player2 
            self.opponent = self.player1         
        
    
if __name__ == '__main__':
    game = Game()
    game.play() 