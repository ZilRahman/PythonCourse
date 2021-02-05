# Question 11: Secret number guessing game
#
# Program asks the user to guess a secret number (5) if user input too low
# the user is re-promted and hinted number is low. If input is too high the 
# program hints its too high. Once the number is guessed correctly the program ends.



secretNumber = "5"

selection = " "

while selection not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
    
    selection = input("Guess a number between 1-10: ")
    
    if selection not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
        print("Thats not a valid response!")

    if (selection=="1") or (selection=="2") or (selection=="3") or (selection=="4"):
        print("That number is too low! Try again.") 
        selection = " "

    if (selection=="6") or (selection=="7") or (selection=="8") or (selection=="9") or (selection=="10"):
        print("That number is too high! Try again.")
        selection = " "

    if (selection==secretNumber):
        print("Congratulations! thats the correct number.")