import random


SIZE = 10


def clean(world):
   # You must implement

    poop = "O"
    cleaned = "."

    for row in range(0, SIZE, 1):
        for column in range(0, SIZE, 1):
            if (poop == world[row][column]):
                world[row][column] = cleaned

    print("clean")


def count(world):
    # You must implement
    print("Counting number of occurances of a character")
    number = 0
    element = input("Enter character: ")

    for row in range(0, SIZE, 1):
        for column in range(0, SIZE, 1):
            if (element == world[row][column]):
                number = number + 1

    # Insert your answer here for counting occurances
    return(element, number)

# Randomly generates an 'occupant' for a location in the world


def createElement():
    # It's been pre-written for you
    chrs = 'POOPDESCOOP'  # Change your required characters here
    n = 1  # Change your word length here

    return ''.join(random.choices(chrs, k=n))

# Creates the SIZExSIZE world (SIZE = a named constant). Randomly populates it with the
# return values from function createElement


def createWorld():
   # It's been pre-written for you
    world = []
    for r in range(0, SIZE, 1):
        world.append([])
        for c in range(0, SIZE, 1):
            world[r].append(createElement())

    return world

# Shows the elements of the world. All the elements in a row will appear on the same line.


def display(world):
    # It's been pre-written for you
    for r in range(0, SIZE, 1):
        for c in range(0, SIZE, 1):
            print(world[r][c], end="\t")
        print("")


def start():
    # Randomly generate world using the above two functions: createWorld and createElement
    world = createWorld()
    display(world)

    # Count # instances (in the world) of a user entered character
    element, number = count(world)

    print("# occurances of %s=%d" % (element, number))

    clean(world)   # Remove the "undesired debris" from the world

    display(world)    # Show again the 'cleaned' world


start()
