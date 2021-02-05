# Question 12: Lucky number generator
# Importing the random() and using the range function within random().
# User inputs the number of values they want, then program prints a list of random numbers and displays that.

import random

selection = " "
selection = int(input("How many digits do you want?: " ))

while (selection <= 0):
    print("Please enter a positive integer only!")
    selection = " "
    selection = int(input("How many digits do you want?: " ))


for i in range(0, selection):
    luckyNumber = random.randrange(1, 100)
    print(luckyNumber, end=" ")


