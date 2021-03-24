
# creates FileIO class
# gathers input file from user and parses the file diffrentiating number of turns
# and attacker and defender probabilities the user inputs in the file 'input.txt'
# returns the number of turns and the probabilities of attacker and defender.
class FileIO:
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
                prob = self.parseFile(fileObject)
                fileObject.close()
                return prob

    # parses file and reads the lines given to determine number of turns and attacker/defender probabilities
    # inputed by user in 'input.txt' file.
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

        return (numberOfTurns, attackerProbEL, attackerProbL, attackerProbM, attackerProbH, defenderProbEL, defenderProbL, defenderProbM, defenderProbH)
