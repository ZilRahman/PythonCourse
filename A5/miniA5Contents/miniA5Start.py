
# imports Adventure() class from respective file
from miniA5Adventurer import Adventurer

# main execution outlines the program route by calling default values.
# A name is given and health is increased and the new values are displayed.


def start():

    myAdventurer = Adventurer()

    print("The default values are:", myAdventurer.name, myAdventurer.health)

    myAdventurer.name = "Balin"

    myAdventurer.gainLevel()

    print("New values are:", myAdventurer.name, myAdventurer.health)


start()
