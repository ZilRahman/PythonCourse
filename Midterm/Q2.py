# Question 2: Random number guess program 
#
# For simplicity purposes the program will limit the user to enter a value between one and ten.

# Random() imported so it can be used in the program

import random

# Value that the computer generates which is converted to string and is stored in a variable

computerValue = str(random.randint(1, 10))

# Value that the user inputs

personValue = input("Enter a whole value between 1 and 10: ")

# If statement which checks if both computer and person values are the same then game is won.
# Otherwise program tells user to try again.

if (computerValue == personValue):
    print("You Win!")
else:
    print("Try Again!")
