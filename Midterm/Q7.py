# Question 7: Grocery Sales Tax calculator
#
# Program asks for five inputs calculates the total before and after tax (6%) 
# then displays the amount total, tax amount and net amount owed.

itemOne = int(input("Cost of Item one: "))
itemTwo = int(input("Cost of Item two: "))
itemThree = int(input("Cost of Item three: "))
itemFour = int(input("Cost of Item four: "))
itemFive = int(input("Cost of Item five: "))

subTotal = (itemOne + itemTwo + itemThree + itemFour + itemFive)

print("Your subtotal is:", subTotal)

tax = subTotal*0.06

tax = round(tax, 2)

print("The taxes owed are:", tax)

subTotal = tax + subTotal

print("The total amount owed is:", subTotal)

