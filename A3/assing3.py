def goToLivingRoom():
    
    ballofString = False
    cheeseSelect = False
    selection = " "

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
                print("Please enter one of '1' or '2' or '3' or '4' ")
            if (selection == "1"):
                print("Looks dry")
            if (selection == "2"):
                print("You go to the attic")
                ballofString, cheeseSelect = goToAttic(ballofString, cheeseSelect)
            if (selection == "3"):
                print("You go to the bedroom")
            if (selection == "4"):
                print("You observe the ball of string.")
                ballofString = ballofYarn()
        print("ball false")

    if (ballofString == True):
        
        while selection not in ("1", "2", "3"):
            print ("List of possible actions")
            print ("(1) View the pot of soil")
            print ("(2) Take the stairs up to the attic")                  
            print ("(3) Go to Bedroom")
            selection = input("Enter your selection: ")
            if selection not in ("1", "2", "3"):
                print("Please enter one of '1' or '2' or '3'")
            if (selection == "1"):
                print("Looks dry")
            if (selection == "2"):
                print("You go to the attic")
                # 1st run - you decide to drop the string
                # false, (true or false) =  gotoattic(true, either or (true or false))

                # 2nd run - What do you have?
                # goToAttic(false, (true or false))
                ballofString, cheeseSelect = goToAttic(ballofString, cheeseSelect)
                selection = " "
            if (selection == "3"):
                print("You go to the bedroom")
                selection = " "
        print("Ball True")



def potOfSoil():
    print("You observe the pot of soil")
    



def goToAttic(ballofString, cheeseSelect):
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
            return(ballofString, cheeseSelect)

        elif (atticSelect == "2"):
            print("Observing the cheese... there seems to be a lottttttt of cheese")
            atticSelect = " "
            cheeseSelect = cheeseFunction()

        elif (atticSelect == "3") and (ballofString == True):
            print("You have now distracted the cat in the bedroom!")
            atticSelect = " "
            ballofString = False

        elif (atticSelect == "3"):
            atticSelect = " "
            print("Its tiny enough that you could try dropping some string....")
            
        

def cheeseFunction():
    print("This cheese could come in handy.\n")
    cheeseSelect = input("Pick up the cheese? (y/n): \n")
    if (cheeseSelect == "y"):
        print("You've decided to pick up some of the cheese!\n")
        return (True)

    elif (cheeseSelect == "n"):
        print("You've decided to not pick up the cheese.\n")
        return (False)


    # return(cheeseSelect, atticSelect)

def goToBedroom():
    print("You are in the bedroom")

def ballofYarn():
    print("You approach the ball of string\n")
    ballofString=input("Pick up the ball of string? (y/n): ")

    if (ballofString == "y"):
        print("\nPicked up the ball of string.\n")
        return(True)
    else:
        print ("\nLeft the ball of string in its place.\n")
        return(False)

def start():
    goToLivingRoom()
    print("nigeria")

start()