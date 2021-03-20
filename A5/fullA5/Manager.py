

class Manager():

    run = ""

    def __init__(self):
        self.run = "running"

    def getFileIO(self):
        print("getFileIO")

    def runSimulation(self):
        print("Simualtion is", self.run)

    def fighting(self):
        print("each turn attacker to attack, defender to defend")

    def fightingReport(self):
        print("this fun determines results of the attack-defense and makes per-turn report")

    def endOfSimulationReport(self):
        print("this fun to make end of simulation report and write per turn and endofSimulation report to file")

# see assingment to see details

# The minimum attributes for this class should include:
# a FileIO object,
# an Attacker object,
# a Defender object
