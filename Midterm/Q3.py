# Question 3: Credit Card qualifier program



# Two inputs (annual salary and house ownership) are asked which determines
# the programs route to wether the user will qualify for the credit card.


yearlyPayment = int(input("How much do you make per year?: "))

houseQualify = input("Do you own your own home? (y/n): ")

# Minimum annual salalry threshold is 30000 and if house ownership 
# is a yes then qualification is met.

if (yearlyPayment >= 30000) and (houseQualify == "y"):
    print("You qualify!")

# If house ownership is not met but annual salary is good then 
# a calcualtion is done wether they pay more than 5% of their annual 
# salary in rent. If they do they don't qualify.

elif (yearlyPayment >= 30000) and (houseQualify == "n"):
    rentInput = int(input("How much rent do you pay per month?: "))
    
    rentPercentage = yearlyPayment*0.05

    if (rentInput < rentPercentage):
        print("You Qualify!")

    elif (rentInput >= rentPercentage):
        print("Sorry you don't qualify, your rent is too high.")

else:
    print("You don't qualify.")


    
    