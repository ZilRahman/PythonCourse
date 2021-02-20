# Assingment 4
# text based version of "Game of life"
# inside a 10x10 matrix.


# world is 10x10
SIZE = 10
debugOn = False


# createListFileRead inputs a file from user and runs the program
# implemented by teacher
# returns fileList
def createListFileRead(fileName):
    fileList = []
    try:
        fileObject = open(fileName, "r")
    except OSError:
        for line in range(0, SIZE, 1):
            listLine = []
            print("\n")
            for char in range(0, SIZE, 1):
                listLine.append("!")

            fileList.append(listLine)
    else:
        for line in fileObject:
            listLine = []
            for char in line:
                if (char != "\n"):
                    listLine.append(char)
            fileList.append(listLine)
    return fileList


# display() displayes the old and new file side by side respectively in a readable fashion.
# passed in arguements are old list and new list respectively.
def display(fileList, newList):

    for row in range(0, SIZE, 1):
        print(" - - - - - - - - - -#\t  - - - - - - - - - -")
        oldListRow = ""
        newListRow = ""
        for col in range(0, SIZE, 1):
            oldListRow = oldListRow + "|{}".format(fileList[row][col])
            newListRow = newListRow + "|{}".format(newList[row][col])
        print(oldListRow, "\t", newListRow)


# slectionList() is the main game menu selection and prompts the user wether they would like to
# continue or quit the game.
# passed in arguements are old list and new list respectively.
def selectionList(fileList, newList):
    selection = " "
    selectionCount = 0

    while selection not in ("e", "q"):

        selection = input("Hit 'e' to continue or 'q' to quit: ")

        if selection not in ("e", "q"):
            print("That's not a valid response!")
            selection = " "

        if (selection == "q"):
            print("You've decided to quit.")

        if (selection == "e"):
            selectionCount = selectionCount + 1
            print("Turn: {}".format(selectionCount))
            print("Before               \t After           ")
            display(fileList, newList)
            fileList = newList
            newList = createNewList(fileList)
            iterateList(fileList, newList)
            selection = " "


# createNewList() function creates a new list from the old list value.
# passed in arguement is the old list.
def createNewList(fileList):

    newList = []

    for row in range(0, SIZE, 1):
        newList.append([])
        for col in range(0, SIZE, 1):
            newList[row].append(" ")
    return newList


# iterateList() determines wether or not critters die or are born by calling and capturing
# the return value of calculateNeighbours(). After calculations the newList is updated on their
# x and y elements wether critters die or are born.
# passed in arguements are fileList and newList for the old list and new list respectively.
def iterateList(fileList, newList):

    for x in range(0, SIZE, 1):
        for y in range(0, SIZE, 1):
            neighbour = calculateNeighbours(fileList, x, y)
            tempElement = fileList[x][y]

            if (tempElement == "*"):
                if (neighbour >= 4):
                    # over-crowding; critter dies
                    newList[x][y] = " "

                if (neighbour <= 1):
                    # loneliness; critter dies
                    newList[x][y] = " "

                if (neighbour == 3 or neighbour == 2):
                    # remain living
                    newList[x][y] = "*"

            if (tempElement == " "):
                if (neighbour == 3):
                    # critter born
                    newList[x][y] = "*"


# calculateNeighbours() function calculates neighbours of a given element in the list and returns calculated
# amount only if they're within game bounds (10*10).
# passed in arguements are the old list and x and y elements for row and column respectively.
# function returns calculated neighbours value.
def calculateNeighbours(fileList, x, y):

    # neighbour value count
    neighbour = 0

    if ((x-1) >= 0):
        # left neighbour
        if (fileList[x-1][y]) == "*":
            neighbour = neighbour + 1

    if ((y-1) >= 0):
        # top neighbour
        if (fileList[x][y-1]) == "*":
            neighbour = neighbour + 1

    if ((x+1) <= 9):
        # right neighbour
        if (fileList[x+1][y]) == "*":
            neighbour = neighbour + 1

    if ((y+1) <= 9):
        # bottom neighbour
        if (fileList[x][y+1]) == "*":
            neighbour = neighbour + 1

    if ((x-1) >= 0) and ((y+1) <= 9):
        # bottom-left neighbour
        if (fileList[x-1][y+1]) == "*":
            neighbour = neighbour + 1

    if ((x+1) <= 9) and ((y+1) <= 9):
        # bottom-right neighbour
        if (fileList[x+1][y+1]) == "*":
            neighbour = neighbour + 1

    if ((x+1) <= 9) and ((y-1) >= 0):
        # top-right neighbour
        if (fileList[x+1][y-1]) == "*":
            neighbour = neighbour + 1

    if ((x-1) >= 0) and ((y-1) >= 0):
        # top-left neighbour
        if (fileList[x-1][y-1]) == "*":
            neighbour = neighbour + 1

    return neighbour


# start() is the main function that executes the game program.
# all functions are within the bounds of this main function.
def start():

    userInput = input("What is the file name?: ")

    fileList = createListFileRead(userInput)

    newList = createNewList(fileList)

    iterateList(fileList, newList)

    selectionList(fileList, newList)


# program begins by calling upon start()
start()
