#Virtual Dice Roll Program! 


#imports the random function into the program

import random   

# The first dice produces a random integer value between one to six and converts it into a string.

diceOne = str(random.randint(1, 6))  

# The second dice produces a random integer value between one to six and converts it into a string.

diceTwo = str(random.randint(1, 6))

# Displays the virtual rolled dice. 

print("Virtual Dice Roll: {} and {} " .format(diceOne, diceTwo)) 