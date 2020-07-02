# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:26:58 2020

@author: Nathan
"""

import sys

def mainMenu():
    print("~~~~~~~~DOMAIN DOMINANCE BETA~~~~~~~~")
    menuOptions = ["Play Game", "Instructions", "Exit"]
    #May replace multi-line string with variables in list, enumerated
    while True:
        print("""
              1. Play Game
              2. Instructions
              3. Exit
              """)
        option = int(input("Select an option: "))
        if option in range(1, len(menuOptions) + 1):
            break;
        else:
            print("Invalid entry.") 
    return option 

def mainMenuOptions(option):
    assert option in range(1, 4), "Should be between 1 and 3 inclusive"
    if option == 1:
        print("Starting game...")
    elif option == 2:
        print("Instructions forthcoming...")
    elif option == 3:
        print("See you next time!")
        sys.exit("Ending program")

        

if __name__ == '__main__':
    option = mainMenu() 
    mainMenuOptions(option)
