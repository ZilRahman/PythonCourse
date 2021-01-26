# Assingment 3
# Text based adventure game 




# Imported time since function can be used in the game for supense and story telling.
import time             

#
# This is the main function called inside the start() function. It records all the flags
# and uses a living room menu selection input variable to call other functions/rooms.
# The game is only won when the player views the soil after all conditions have met.
# Conditions to meet to end game; distract the cat from the attic by using the string,
# feeding the mouse some cheese so the soil is fertilized.
#
def goToLivingRoom():           
    
    ballofString = False
    cheeseSelect = False
    catDistracted = False
    mouseCheeseDecision = False
    selection = " "
    print("You are in the main living room...\n")
    if (ballofString == False):
        selection = " "
        while selection not in ("1", "2", "3", "4"):
            print ("List of possible actions")
            print ("(1) View the pot of soil")
            print ("(2) Take the stairs up to the attic")                  
            print ("(3) Go to Bedroom")
            print ("(4) Ball of string")
            selection = input("Enter your selection: ")
            if selection not in ("1", "2", "3", "4"):
                print("\nPlease enter one of '1' or '2' or '3' or '4' \n")
            if (selection == "1"):
                print("\nA dry pot of soil...perhaps something can grow out of it...\n")
                selection = " "
            if (selection == "2"):
                print("\nYou go to the attic\n")
                ballofString, cheeseSelect, catDistracted = goToAttic(ballofString, cheeseSelect, catDistracted)
            if (selection == "3"):
                print("\nYou go to the bedroom\n")
                goToBedroom(ballofString, cheeseSelect, catDistracted, mouseCheeseDecision)
                selection = " "
            if (selection == "4"):
                print("\nYou observe the ball of string.\n")
                ballofString = ballofYarn()

    if (ballofString == True):
        
        while selection not in ("1", "2", "3"):
            print ("List of possible actions")
            print ("(1) View the pot of soil")
            print ("(2) Take the stairs up to the attic")                  
            print ("(3) Go to Bedroom")
            selection = input("Enter your selection: ")
            if selection not in ("1", "2", "3"):
                print("Please enter one of '1' or '2' or '3'\n")

            if (selection == "1") and (mouseCheeseDecision == True):
                print("\nVine growing out\n")
                return(None)

            if (selection == "1"):
                print("\nLooks super dry...maybe if its fertilized something would grow...\n")
                selection = " "

            if (selection == "2"):
                print("\nYou go to the attic\n")
                ballofString, cheeseSelect, catDistracted = goToAttic(ballofString, cheeseSelect, catDistracted)
                selection = " "
            if (selection == "3"):
                print("\nYou go to the bedroom\n")
                ballofString, cheeseSelect, catDistracted, mouseCheeseDecision = goToBedroom(ballofString, cheeseSelect, catDistracted, mouseCheeseDecision)
                selection = " "
        print("\nBall True\n")


#
# This function is called upon by goToLivingRoom() and lists interactions that determine
# if the flag conditions have met. It is passed the boolean expressions; ballofString, cheeseSelect, catDistracted.
# It also returns the boolean expressions ballofString, cheeseSelect, catDistracted.
# These expressions either True/False determine if conditions have been met to end the game.
#
def goToAttic(ballofString, cheeseSelect, catDistracted):
    print("You are in the attic.")
    print("There is a tiny hole to the bedroom below, maybe you could try dropping something.")
    print("There is also unlimited supply of cheese....")
    atticSelect = " "
    while atticSelect not in ("1", "2", "3"):
        print("(1) Take the stairs down to the living room ")
        print("(2) Observe the cheese ")
        



        if (ballofString == True):
            print("(3) - Drop the ball of string in the hole")

        else:
            print("(3) - Ponder on the hole....... ")
            
        
        atticSelect = input("Enter your selection: ")

        if atticSelect not in ("1", "2", "3"):
            print("Please enter 1 or 2 or 3\n")


        elif (atticSelect == "1"):
            print("You've decided to go back to the living room.\n")
            atticSelect = " "
            return(ballofString, cheeseSelect, catDistracted)

        elif (atticSelect == "2"):
            print("Observing the cheese... there seems to be a lottttttt of cheese")
            atticSelect = " "
            cheeseSelect = cheeseFunction()

        elif (atticSelect == "3") and (ballofString == True):
            print("You have now distracted the cat in the bedroom!")
            atticSelect = " "
            ballofString = False
            catDistracted = True

        elif (atticSelect == "3"):
            atticSelect = " "
            print("Its tiny enough that you could try dropping some string....")
           
#       
# The cheeseFunction() is called upon by goToAttic(). it determines wether the cheeseSelect flag will be met.
# This function returns the cheeseSelect as either True/False, which in turn determines if player wins the game.
#  

def cheeseFunction():
    print("This cheese could come in handy.\n")
    cheeseSelect = input("Pick up the cheese? (y/n): \n")
    if (cheeseSelect == "y"):
        print("You've decided to pick up some of the cheese!\n")
        return (True)

    elif (cheeseSelect == "n"):
        print("You've decided to not pick up the cheese.\n")
        return (False)


    
#
# The goToBedroom() is called upon by the goToLivinngRoom() and it is passed in 
# ballofString, cheeseSelect, catDistracted, mouseCheeseDecision boolean expressions. 
# This in turn determines the flags of these boolean expressions as either True/False and
# determines if the user will win the game. The player is given options depending on if hes met some conditions.
# This function also returns the same boolean expressions its passed in (ballofString, cheeseSelect, catDistracted, mouseCheeseDecision). 
#

def goToBedroom(ballofString, cheeseSelect, catDistracted, mouseCheeseDecision):
    print("You are in the bedroom")
    bedroomSelect = " " 
    while bedroomSelect not in ("1", "2", "3"):
        print("(1) Go back to the living room")# wtf is this random print line

        if (catDistracted == True) and (cheeseSelect == True):
            print("\nThe mouse has come out of its hole after the cat left!\n") 
            mouseCheeseDecision = mouseCheeseSelection(cheeseSelect, mouseCheeseDecision)
            bedroomSelect = " "


        if(ballofString == True):
            catInput = input("(2) Play with the cat using the string? (y/n): ")
            if (catInput == "y"):
                print("\nThe cat briefly looks at you and looks at the mousehole again.\n")
                bedroomSelect = " "
                # needs option list
            else:
                print("\nYou leave the cat alone\n")
                
        bedroomSelect = input("Enter your selection: ")

        if bedroomSelect not in ("1", "2", "3"):
            print("Please enter the correct numerical input outlined in the options\n")
        
        if (bedroomSelect == "1"):
            print("You have decided to go back to the living room.\n")
            bedroomSelect = " "
            return(ballofString, cheeseSelect, catDistracted, mouseCheeseDecision)

#
# The mouseCheeseSelection() is called on by goToBedroom() and is passed in the boolean exprssions cheeseSelect and mouseCheeseDecision.
# The cheeseSelect expression aids in providing a new option to the user if they are carrying the cheese or not.
# This function return the mouseCheeseDecision boolean expression as eiither true/false.
#

def mouseCheeseSelection(cheeseSelect, mouseCheeseDecision):
    print("The mouse looks at you...\n")
    mouseCheeseDecisionInput = input("Would you like to feed the mouse? (y/n)?: \n")
    if (mouseCheeseDecisionInput == "y") and (cheeseSelect == True):
        print("You fed the mouse some cheese!\n")
        print("It briefly left the room and 'fertilized' the soil....if you catch my drift...\n")
        return(True)

    if (mouseCheeseDecisionInput == "y") and (cheeseSelect == False):
        print("The mouse looks hungry AF maybe some cheese will staisfy its hunger.\n")
        return(False)


    if (mouseCheeseSelection == "n"):
        print("The mouse looks sad you did not share the cheese :(")
        mouseCheeseDecisionInput = " "

#
# The ballofYarn() is called by goToLivingRoom() and determines if the user will pick up the ball of string or not
# by returning the boolean expression ballofString as either True/False. 
#     

def ballofYarn():
    print("You approach the ball of string\n")
    ballofString=input("Pick up the ball of string? (y/n): ")

    if (ballofString == "y"):
        print("\nPicked up the ball of string.\n")
        return(True)
    else:
        print ("\nLeft the ball of string in its place.\n")
        return(False)

#
# This is the main function which executes the entire program by calling goToLivingRoom().
#
#

def start():

    print("Welcome to Wocky Cheesy Escape!\n")
    print("You are back again at the vacational beach house! Only now life has moved quie fast and it feels like forever since you came here..")
    print("Your family has moved on and this place has turned into a rundown house, you go to retrieve some things that grandpa might have left there.")
    print("You come across the documents in the living room and fianlly are about to leave when soemthing keeps you waiting...\n")
    time.sleep(1)
    
    print("Ever since coming to the beach house as a kid there has been soemthing odd about this pot of soil in the living room.")
    print("Your grandfather has told you of a magical plant that will sprout for the one worthy of it...")
    print("You always recall him watering this plant but nothing would grow.")
    print("You dont know what the fuck any of that means but there is something magical, soemthing ancient about this soil and you cannot over look this.")
    print("You start your hunt to get to the bottom of this mystery and try to find the soil soemthing that will nurture its growth...")

    goToLivingRoom()

    print("The Vine sprouts and isntantly grows into a circle and in the midst of it is.....")
    time.sleep(1)
    print("You can't believe your eyes....")
    time.sleep(1)
    print("Lucious garden with foliage that moves you to tears, you've never seen anything as beautiful as this place in your life before... ")
    print("Without thinking you go through and set on spending the rest of your life in heaven itself.")
    print("")
    print("")
    print("The End")

    


start()