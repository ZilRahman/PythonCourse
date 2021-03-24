import random
from Globals import *
# imports random to use function capabilities and the global constants provided in asssigment


# creates Attacker class that generates the attack
# returns the probabilities of Extra-lwo, low, medium and high attacks
# in a variable 'attackChoice'
class Attacker:

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

    def generateAttack(self):

        attackList = [EXTRA_LOW]*self.probEL + [LOW] * \
            self.probL + [MED]*self.probM + [HIGH]*self.probH

        attackChoice = random.choice(attackList)

        if attackChoice == EXTRA_LOW:
            self.numEL = self.numEL + 1

        elif attackChoice == LOW:
            self.numL = self.numL + 1

        elif attackChoice == MED:
            self.numM = self.numM + 1

        elif attackChoice == HIGH:
            self.numH = self.numH + 1

        return attackChoice
