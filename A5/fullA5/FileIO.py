

class FileIO():
    def __init__(self):
        pass

    def getInput(self):

        fileCorrectFlag = False

        while fileCorrectFlag is False:

            fileInput = input("Enter the file name: ")

            try:
                fileObject = open(fileInput, "r")

            except:
                print("Incorrect file name")

            else:

                fileCorrectFlag = True
                self.parseFile(fileObject)
                fileObject.close()

    def parseFile(self, fileObject):

        numberOfTurns = int(fileObject.readline())
        attackerLine = fileObject.readline()

        attackerProb = attackerLine.split(",")
        attackerProbEL = int(attackerProb[1])
        attackerProbL = int(attackerProb[2])
        attackerProbM = int(attackerProb[3])
        attackerProbH = int(attackerProb[4])

        defenderLine = fileObject.readline()

        defenderProb = defenderLine.split(",")
        defenderProbEL = int(defenderProb[1])
        defenderProbL = int(defenderProb[2])
        defenderProbM = int(defenderProb[3])
        defenderProbH = int(defenderProb[4])

    def generateResults(self):
        print("Generate results from simulation and write them to results.txt")


newFile = FileIO()

newFile.getInput()
