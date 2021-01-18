# This program is an adventure game, objective is to unlock the door.There are three rooms. The player starts in the living room.


# No documentation


silverLockValue = " "
goldLockValue = " "
pantry = " "
kitchen = " "
entranceway = " "


selection = " "

while (selection not in ("1", "2", "3")):
    print ("List of possible actions")
    print ("(1) Try to open the Inner door")
    print ("(2) Go through the left entryway (kitchen)")                  
    print ("(3) Go through the right entryway (Pantry)")
    selection = input("Enter your selection: ")
    if selection not in ("1", "2", "3"):
        print ("Please enter one of '1' or '2' or '3' ")

    if (selection == "1"):
        if (goldLockValue == "1") and (silverLockValue == "2"):
            print ("Huzzah! You've entered the house.")
        else:
            print ("Inner door is still locked!")
            print ("\n\n")
            selection = " "

    if (selection == "2"):
        print("\n\n You are in the Kitchen, there is a golden lock.")

        goldenLockFlag = " "
        while goldenLockFlag not in ("1", "2", "3", "4"):
            print ("List of possible actions")
            print ("(1) Turn the golden lock to the left position")
            print ("(2) Turn the golden lock to the right position")                  
            print ("(3) Turn the golden lock to the center position")
            print ("(4) Don't change position! Return to entranceway")
            goldenLockFlag = input("Enter your selection: ")


            if goldenLockFlag not in ("1", "2", "3", "4"):
                print ("Please enter one of '1' or '2' or '3' or '4' ")
                print ("\n\n")
            elif (goldenLockFlag == "1"):
                print("Golden lock set to left position!")
                print ("\n")
                goldLockValue = "1"
                goldenLockFlag = " "
            elif (goldenLockFlag == "2"):
                print("Goldne lock set to right position!")
                print ("\n")
                goldLockValue = "2"
                goldenLockFlag = " "
            elif (goldenLockFlag == "3"):
                print("Golden lock set to center position!\n")
                goldLockValue = "3"
                goldenLockFlag = " "
            else:
                print("Golden lock position not changed! Returning to entranceway!\n")
                selection = " "
            


    if (selection == "3"):
        print("\n\n You are in the pantry, theres is a silver lock.")

    
        silverLockFlag = " "
        while silverLockFlag not in ("1", "2", "3", "4"):
            print ("List of possible actions")
            print ("(1) Turn the silver lock to the left position")
            print ("(2) Turn the silver lock to the right position")                  
            print ("(3) Turn the silver lock to the center position")
            print ("(4) Don't change position! Return to entranceway")
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
                print("Silver lock position not changed! Returning to entranceway!\n")
                selection = " "


















