# Question 6: Square footage to Acres calculator
#
# Program inputs square footage area and calculates to acres then displays that value
# rounded to a decimal place of 2.

squareFootage = int(input("Enter the total square feet: "))

acre = (squareFootage/43560)

acre = round(acre, 2)

print("Your acreage value is:", acre)