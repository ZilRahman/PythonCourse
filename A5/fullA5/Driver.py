from Manager import *
# Imports everything from Manager module


# execution point of program capturing return value of Manager class in the
# Manager module. Calls upon the getFileIO() and runSimulation methods and
# starts the simulation.
def start():
    aManager = Manager()

    aManager.getFileIO()

    aManager.runSimulation()


start()
