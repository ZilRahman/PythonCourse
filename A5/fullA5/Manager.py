from FileIO import *
from Attacker import *
from Defender import *
import sys
# importing modules; FileIO, Attacker and Defender and importing everything in them
# importing sys to use built-in functions to write to file output.txt


# creating a class Manager; manages and runs the simulation by calling to FileIO class
# using a getFileIO() method and runs the simulation using a runSimulation() method.
# As well as making a report per turn using the fightingReport() method.
# At the end of the simulation a report is made showing the grand total of blocks/hits and the
# percentage proportions of the Attacker and Defender blocks/hits.
# Per-turn report and the end of simulation report is written to 'output.txt'
class Manager:

    run = ""
    numberOfTurns = 0
    attacker = Attacker(0, 0, 0, 0)
    defender = Defender(0, 0, 0, 0)

    totalHits = 0
    totalBlocks = 0

    def __init__(self):
        pass

    # method to call the FileIO class and captures the return values
    def getFileIO(self):
        print("getFileIO")
        fileObject = FileIO()
        probabilities = fileObject.getInput()
        (numberOfTurns, attackerProbEL, attackerProbL, attackerProbM, attackerProbH,
         defenderProbEL, defenderProbL, defenderProbM, defenderProbH) = probabilities

        self.numberOfTurns = numberOfTurns
        self.attacker = Attacker(EL=attackerProbEL, L=attackerProbL,
                                 M=attackerProbM, H=attackerProbH)
        self.defender = Defender(
            EL=defenderProbEL, L=defenderProbL, M=defenderProbM, H=defenderProbH)

    # method to run the simulation based on number of turns and writes to 'output.txt'
    # calls the endOfSimulation() method
    def runSimulation(self):
        sys.stdout = open("output.txt", "w")

        for i in range(0, self.numberOfTurns):
            generatedAttack = self.attacker.generateAttack()
            generatedDefense = self.defender.generateDefense()
            self.fightingReport(i+1, generatedAttack, generatedDefense)
        print("")
        print("")
        sys.stdout.close()
        self.endOfSimulationReport()

    # determines if a attack/defense is either block/hit and calls the changeNumToString() method
    def fightingReport(self, roundNumber, attack, defense):
        result = ""
        if attack == defense:
            result = "Blocked"
            self.totalBlocks = self.totalBlocks + 1

        else:
            result = "Hit!"
            self.totalHits = self.totalHits + 1

        print("MK Round{}:\t".format(roundNumber), "Attack:{},\t".format(self.changeNumToString(
            attack)), "Defense:{}\t.........".format(self.changeNumToString(defense)), result)

    # converts the number of global constants to strings the simulator can use to showcase during/after
    # simulation report.

    def changeNumToString(self, number):
        if number == EXTRA_LOW:
            return "X-low"
        elif number == LOW:
            return "low"
        elif number == MED:
            return "medium"
        else:
            return "high"

    # writes a report counting the tally number of blocks and hits as well as the proportion based on
    # percentages of the attacker and defender. Appends the report to the 'output+.txt' file.
    def endOfSimulationReport(self):

        sys.stdout = open("output.txt", "a")

        print("Summary of Kombat")
        print("Total Hits:{}\t".format(self.totalHits),
              "Total Blocks:{}".format(self.totalBlocks))
        print("Attacker proportions:\t", "X-low {}%,".format(self.attacker.numEL), "Low {}%,".format(
            self.attacker.numL), "Medium {}%,".format(self.attacker.numM), "High {}%".format(self.attacker.numH))
        print("Defender proportions:\t", "X-low {}%,".format(self.defender.numEL),
              "Low {}%,".format(self.defender.numL), "Medium {}%,".format(self.defender.numM), "High {}%".format(self.defender.numH))

        sys.stdout.close()
