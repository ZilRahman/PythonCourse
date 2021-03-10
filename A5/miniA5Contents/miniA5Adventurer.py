#
# defining a class 'Adventurer' which is called upon in the 'miniA5Start.py' file.
# attributes are name and health and set to default values 'nameless' and '-1' respectively.
# class uses two methods one is a constructor and another one 'gainlevel()' increases health...
# and prints "Congratulations!"
#

class Adventurer:

    def __init__(self):

        self.name = "nameless"

        self.health = -1

    def gainLevel(self):

        print("Congratulations!")

        self.health = self.health + 5
