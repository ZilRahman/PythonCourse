# Question 10: Price tally counter
#
# Program keeps track of the running total as the user enters prices. 
# Program prompts the user after each price to see if they wish to continue entering prices. 
# When they are finished, program print out the total amount entered.
# 


item = []
itemprice = 0
price = True

while (price == True):
    itemPrice = int(input("Enter the price of the item: "))

    item.append(itemPrice)

    priceSelection = input("Do you wish to continue entering prices? (y/n): ")

    if (priceSelection == "y"):
        
        price = True

    if (priceSelection == "n"):
        
        sumOfAllItems = sum(item)

        print("Your total sum is: {}".format(sumOfAllItems))

        price = False