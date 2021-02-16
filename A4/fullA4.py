

# world is 10x10
SIZE = 10
debugOn = False


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


def display(fileList, newList):
    print("this fun() displays ")
    for row in range(0, SIZE, 1):
        print(" - - - - - - - - - -#\t  - - - - - - - - - ")
        oldListRow = ""
        newListRow = ""
        for col in range(0, SIZE, 1):
            oldListRow = oldListRow + "|{}".format(fileList[row][col])
            newListRow = newListRow + "|{}".format(newList[row][col])
        print(oldListRow, "\t", newListRow)
        print("")


def selectionList(fileList):
    selection = ""
    critter = "*"
    selectionCount = 0

    while selection not in ("", "q"):
        selection = input("Hit enter to continue or 'q' to quit: ")
        if selection not in ("", "q"):
            print("That's not a valid response!")

        if (selection == "q"):
            print("You've decided to quit.")

        if (selection == ""):
            print("Onto the next turn...")
            selectionCount = selectionCount + 1


def createNewList(fileList):
    newList = []

# this first loop initializes the new list to be made from the
# old list value.
    for row in range(0, SIZE, 1):
        newList.append([])
        for col in range(0, SIZE, 1):
            newList[row].append(" ")


# this for loop check the previous fileList and transfers data
# based on the rules of the game.
    # for row in fileList:
    #     for col in fileList:
    #         print("lora")

    return newList


def start():
    userInput = input("What is the file name?: ")
    fileList = createListFileRead(userInput)
    newList = createNewList(fileList)
    display(fileList, newList)
    # print(fileList)
    # print(newList)


start()
