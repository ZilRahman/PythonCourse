# Question 5: Sales profit calculator
# 
# Program inputs annual sales from user and calculates. the annual profit from that amount
# The final calculation is rounded and displayed.

profit = int(input("Enter annual sales: "))

profit = (profit*0.23)

profit = round(profit)

print("Your annual profit will be:",profit)
