# Question 15: Coffee Shop Menu
#
# Program asks for users money amount and is displayed 4 coffee shop menu items which the user selects one. 
# The program determines how much they can afford using their money amount divided by the cost
# of the menu item. The user is then displayed how many items they can afford with their purchase power.
#
#

userMoney = float(input("How much money do you have: "))

selection = " "

while selection not in ("d", "c", "b", "s"):
    
    print("""What would you like to buy?
             Donut  (d) – 1.50
             Coffee (c) – 1.00
             Bagel  (b) – 2.50
             Scone  (s) – 2.75 """)

    selection = input("Enter your choice (d/c/b/s): ")

    if selection not in ("d", "c", "b", "s"):
        print("Thats not a valid response.")
        selection = " "

    if (selection=="d"):
        
        buy = userMoney/1.50
        buy = round(buy)

        print("You can purchase {} donuts with ${} ".format(buy, userMoney))

    if (selection=="c"):

        buy = userMoney/1.00
        buy = round(buy)

        print("You can purchase {} coffees with ${} ".format(buy, userMoney))

    if (selection=="b"):

        buy = userMoney/2,50
        buy = round(buy)

        print("You can purchase {} bagels with ${} ".format(buy, userMoney))

    if (selection=="s"):

        buy = userMoney/2.75
        buy = round(buy)

        print("You can purchase {} scones with ${} ".format(buy, userMoney))






    
