

    
# def goToLivingRoom():

#     livRoomSelect = " "
#     ballSelect = " "
#     atticSelect = " "
#     cheeseSelect = " "
#     # livingRoomMenuTwo = " "

#     while livRoomSelect not in ("1", "2", "3", "4"):
#         print("(1) View the pot of soil")
#         print("(2) Take stairs up to the attic")
#         print("(3) Take the dark entranceway")
#         print("(4) Approach ball of string")
#         livRoomSelect = input("Enter you selection: ")

#         if livRoomSelect not in ("1", "2", "3", "4"):
#             print("Please enter one of '1' or '2' or '3' or '4'\n")

#         elif (livRoomSelect == "1"):
#             print("The pot of soil looks dry, perhaps if its fertilized something will grow...\n")
#             # make a yes or no statement

#         elif (livRoomSelect == "2"):
#             print("You take the creaky stairs into the attic\n")
#             goToAttic(livRoomSelect, ballSelect, atticSelect, cheeseSelect)

#         elif (livRoomSelect == "3"):
#             print("You take the dark entaceway into the bedroom\n")

#         elif (livRoomSelect == "4"):
#             ballofString(livRoomSelect, atticSelect, cheeseSelect)

#         # else: goToLivingRoom(ballSelect, livRoomSelect, atticSelect, cheeseSelect)


#     return (livRoomSelect, ballSelect)      
    
# def livingRoomMenuTwo(livRoomSelect ,ballSelect, atticSelect, cheeseSelect):

#     while livRoomSelect not in ("1", "2", "3"):
#         print("(1) View the pot of soil")
#         print("(2) Take stairs up to the attic")
#         print("(3) Take the dark entranceway")
#         livRoomSelect = input("Enter you selection: ")

#         if livRoomSelect not in ("1", "2", "3", "4"):
#             print("Please enter one of '1' or '2' or '3' ")

#         elif (livRoomSelect == "1"):
#             print("The pot of soil looks dry, perhaps if its fertilized something will grow...\n")
#             livingRoomMenuTwo(ballSelect, livRoomSelect, atticSelect, cheeseSelect)

#         elif (livRoomSelect == "2"):
#             print("You take the creaky stairs into the attic\n")
#             goToAttic(livRoomSelect, ballSelect, atticSelect, cheeseSelect)

#         elif (livRoomSelect == "3"):
#             print("You take the creepy entaceway into the bedroom\n")

#     return(livRoomSelect, ballSelect)

# def ballofString(livRoomSelect, atticSelect, cheeseSelect):

#     print("There is a ball of string, pick it up?\n")
#     ballSelect = input("Take ball of string? (y/n): ")

#     if (ballSelect == "y"):
#         print("Picked up the ball of string!\n")
#         livingRoomMenuTwo(ballSelect, livRoomSelect, atticSelect, cheeseSelect)
#         return (True)

#     elif (ballSelect == "n"):
#         print("you've decided not to pick up the ball of string\n")
#         return (False)

# def goToAttic(livRoomSelect, ballSelect, atticSelect, cheeseSelect):



#     print("You are in the attic.\n")
#     while atticSelect not in ("1", "2", "3"):
#         print("(1) There is a tiny hole here to the bedroom below... ")
#         print("(2) There seems to be some cheese here... ")
#         print("(3) Take the stairs down to the living room ")
#         atticSelect = input("Enter your selection: ")

#         if atticSelect not in ("1", "2", "3"):
#             print("Please enter 1 or 2 or 3\n")

#         elif (atticSelect == "1"):
#             print("Upon further inspection, this hole overlooks the bedroom below. Maybe we could drop something in it?\n")
#             goToAttic(livRoomSelect ,ballSelect, atticSelect, cheeseSelect)

#         elif (atticSelect == "1") and (cheeseSelect == True):
#             print("You try to drop the cheese down the hole but it's too big! Perhaps if there was another item we could dangle it with....\n")

#         elif (atticSelect == "1") and (cheeseSelect == True) and (ballSelect == True):
#             print("You tie the cheese to the string and drop it down the hole!.....The cat has been distracted and left the room!\n")
#             goToAttic(livRoomSelect ,ballSelect, atticSelect, cheeseSelect)
#             # needs cat distraction

#         elif (atticSelect == "2"):
#             cheeseSelect = cheeseFunction(livRoomSelect ,atticSelect, ballSelect, cheeseSelect)
#             # if cheeseSelect == True

#         elif (atticSelect == "3"):
#             print("You've decided to go back to the living room.\n")
#             goToLivingRoom()

#         elif (atticSelect == "3") and (ballSelect == "y"):
#             print("You've decided to go back to the living room.\n")
#             livingRoomMenuTwo(ballSelect, livRoomSelect, atticSelect, cheeseSelect)
        

#     return (atticSelect, cheeseSelect)

# def cheeseFunction(livRoomSelect ,atticSelect, ballSelect, cheeseSelect):

#     print("This cheese could come in handy.\n")
#     cheeseSelect = input("Pick up the cheese? (y/n): \n")
#     if (cheeseSelect == "y"):
#         print("You've decided to pick up some of the cheese!\n")
#         return (True)

#     elif (cheeseSelect == "n"):
#         print("You've decided to not pick up the cheese.\n")
#         return (False)

#     # return(cheeseSelect, atticSelect)

# def goToBedroom():
#     print("You are in the bedroom.\n")

# def start ():
#     goToLivingRoom()

# start()


           


