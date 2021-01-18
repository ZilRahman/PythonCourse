

# Assingment 3; part 1; Refining assingment 2 into functions.

# This program runs an adventure text-based game. 
# The setting of this game is isnide a house where the objective is to unlock
# the door to the inner house. The Objective is achieved through setting the golden lock
# in the kitchen to the 'left' position and the silver lock to the 'left' position. Only when the 
# locks are set to their desired position will the inner door unlock and the user will win the game.
#  
# 
# 
# 
# 
# 

import time # I imported the time so I can use the time function later on in the game (for suspense).    

# goToEntranceRoom();
# Main function inside start function that operates the game and stores values
# that are used to determine if user has won the game.
# from here the user can go to the kitchen, pantry or unlocks the inner door using a 'Selection' input.
#

def goToEntranceRoom():
    print("You are in the main entrance room.")
    selection = " "
    silverLockValue = " "
    goldLockValue = " "



    while (selection not in ("1", "2", "3")):
        print ("List of possible actions")
        print ("(1) Try to open the Inner door")
        print ("(2) Go through the left entryway (kitchen)")                  
        print ("(3) Go through the right entryway (Pantry)")
        selection = input("Enter your selection: ")
        if selection not in ("1", "2", "3"):
            print ("Please enter one of '1' or '2' or '3' ")

        if (selection == "1"):
            doorUnlocked = unlockInnerDoor(goldLockValue, silverLockValue)
            if doorUnlocked == True:
                return(None)

        if (selection == "2"):
            goldLockValue = goToKitchen(goldLockValue)

        if (selection == "3"):
            silverLockValue = goToPantry(silverLockValue)

        selection = " "

#
# unlockInnerDoor(); calculates if the golden and silver lock values have been met and ends the game.  
# using a simple True/False in the return function, we can figure out when the game can be won or not.
# 

def unlockInnerDoor(goldLockValue, silverLockValue):
    print("You fruiosly fumble with the Inner Door lock....\n\n")
    time.sleep(2)

    if (goldLockValue == "1") and (silverLockValue == "2"):
        print ("\nHuzzah! You've entered the house.\n")
        print ("\nFinally now you can kick back and enjoy summer vacation properly! \n")
        print ("Game won!\n")
        return(True)
    else:
        print ("\n\nInner door is still locked!\n\n")
        return(False)

#   
# goToPantry(); calculates and stores the silverLockValue positions and returns the user to the 
# goToLivinfRoom(), to determine if game can be won or not. 
# returns(silverLockValue) and prompts the user back to the goToLivingRoom() function.
#

def goToPantry(silverLockValue):
    print("\n\nYou are in the pantry, there is a silver lock.\n\n")

    silverLockFlag = " "
    while silverLockFlag not in ("1", "2", "3", "4"):
        print("You are in the pantry. Silver lock is at", silverLockValue, "Position!")
        print ("List of possible actions")
        print ("(1) Turn the silver lock to the left position")
        print ("(2) Turn the silver lock to the right position")                  
        print ("(3) Turn the silver lock to the center position")
        print ("(4) Return to entranceway")
        silverLockFlag = input("Enter your selection: ")
        if silverLockFlag not in ("1", "2", "3", "4"):
            print ("Please enter one of '1' or '2' or '3' or '4' ")
            print ("\n\n")
        elif (silverLockFlag == "1"):
            print("Silver Lock set to left position!")
            print ("\n")
            silverLockValue = "1"
            silverLockFlag = " "
        elif (silverLockFlag == "2"):
            print("Silver lock set to right position!")
            print ("\n")
            silverLockValue = "2"
            silverLockFlag = " "
        elif (silverLockFlag == "3"):
            print("Silver lock set to center position!")
            print ("\n")
            silverLockValue = "3"
            silverLockFlag = " "
        else:
            print("Returning to entranceway!\n")
            return(silverLockValue)

#   
# goToKitchen(); calculates and stores the goldLockValue positions and returns the user to the 
# goToLivinfRoom(), to determine if game can be won or not. 
# returns(goldLockValue) and prompts the user back to the goToLivingRoom() function.
#

def goToKitchen(goldLockValue):
    print("\n\n You are in the Kitchen, there is a golden lock.\n\n")

    goldenLockFlag = " "
    while goldenLockFlag not in ("1", "2", "3", "4"):
        print("You are in the kitchen. Golden lock is at", goldLockValue, "Position!")
        print ("List of possible actions")
        print ("(1) Turn the golden lock to the left position")
        print ("(2) Turn the golden lock to the right position")                  
        print ("(3) Turn the golden lock to the center position")
        print ("(4) Return to entranceway")
        goldenLockFlag = input("Enter your selection: ")


        if goldenLockFlag not in ("1", "2", "3", "4"):
            print ("Please enter one of '1' or '2' or '3' or '4' \n")
        elif (goldenLockFlag == "1"):
            print("Golden lock set to left position!\n")
            goldLockValue = "1"
            goldenLockFlag = " "
        elif (goldenLockFlag == "2"):
            print("Golden lock set to right position!\n")
            goldLockValue = "2"
            goldenLockFlag = " "
        elif (goldenLockFlag == "3"):
            print("Golden lock set to center position!\n")
            goldLockValue = "3"
            goldenLockFlag = " "
        else:
            print("Returning to entranceway!\n")
            return(goldLockValue)

#   
# start(); Main function which executes the program and starts the game. This function doesn't calculate
# or return any value.
#

def start():
    print(""" 
    
    After a long and exhasuting year, fianlly summer vacation is here! You and your family           
    have decided to spend some time in the family beach house.


    Ahh....the thought of the ocean and the big blue sky make you impatient but alas you arrive at 
    your destination. """)

    time.sleep(7)

    print(""" 
    
    
    Whats this! You have forgotten the keys! *facepalm* 
    
    
    """)

    time.sleep(3)

    print(""" 
    
    Luckily your Mom remembers there is a secret way to get in, if she recalled correctly there 
    are two rooms before the main entrance; a kitchen and a pantry. In these rooms are two locks.
    The kitchen has a golden lock and the pantry has a silver lock. If you can correctly guess
    the position on both of these locks, the main entranceway will open! 

    """)
    time.sleep(2)

    goToEntranceRoom()


start()