import random
from Globals import *
# imports random to use function capabilities and the global constants provided in asssigment


# creates Defender class that generates the defense
# returns the probabilities of Extra-lwo, low, medium and high defense
# in a variable 'defendChoice'
class Defender:

    probEL = 0
    probL = 0
    probM = 0
    probH = 0

    numEL = 0
    numL = 0
    numM = 0
    numH = 0

    def __init__(self, EL, L, M, H):
        self.probEL = EL
        self.probL = L
        self.probM = M
        self.probH = H

    def generateDefense(self):

        defendList = [EXTRA_LOW]*self.probEL + [LOW] * \
            self.probL + [MED]*self.probM + [HIGH]*self.probH

        defendChoice = random.choice(defendList)

        if defendChoice == EXTRA_LOW:
            self.numEL = self.numEL + 1

        elif defendChoice == LOW:
            self.numL = self.numL + 1

        elif defendChoice == MED:
            self.numM = self.numM + 1

        elif defendChoice == HIGH:
            self.numH = self.numH + 1

        return defendChoice
