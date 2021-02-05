# Question 8: Reversing an input and displaying sum total 
#
# Program asks the user for a two digit input then using an extended slice syntax it reverses it and displayes it. 
# Finally after converting both strings into integers it displaye sthe total value.

string = input("Enter a two digit number: ")

stringTwo = string[::-1]

print("Reversed value is:", stringTwo)

string = int(string)

stringTwo = int(stringTwo)

stringThree = string + stringTwo

print("Total of both values are:", stringThree)