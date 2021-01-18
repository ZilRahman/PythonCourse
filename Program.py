# myCar = "Mercedes Benz C63"
# hp = 450
# displacement = 6.2
# color = "white"
# doors = 4
# print("I have a " + myCar, end = "" )
# print(1 + 4)
# print(" it has " + doors + " and is " + color + ".")
# print(displacement, end="")
# print("L is the engine size", end= "" )
# print(" and it pushes close to ", end="" )
# print(hp, end="hp.")


# BIRTH_RATE = 0.1758
# MORTALITY_RATE = 0.3000
# currentPopulation = 1000000
# populationChange = (BIRTH_RATE - MORTALITY_RATE) * currentPopulation

# print("population", populationChange)

# name = input("L do you know?")

# print("Gods of Death: ", name)

# name = input("What is your name?")
# age = input("How old are you?")

# print(name, "is", age, "years old.")

# CURRENT_YEAR = 2020

# yearOfBirth = input("What is your birthyear?")

# age = (CURRENT_YEAR - int(yearOfBirth))
# print("you are", age, "years old.")


# height = input("How tall are you?(inches only)")
# weight = input("How much do you weight?(pounds only)")

# CONVERSION_FACTOR_BMI = 703

# BMI = 703 * int(weight)/(int(height))**2

# BMI = round(int(BMI),1)

# print("Your BMI is:", BMI)


# number = int(input("What is your number?(1-10):"))

# if(number == 1):
#     print("I")
# elif(number == 2):
#     print("II")
# elif(number == 3):
#     print("III")
# elif(number == 4):
#     print("IV")
# elif(number == 5):
#     print("V")
# elif(number == 6):
#     print("VI")
# elif(number == 7):
#     print("VII")
# elif(number == 8):
#     print("VIII")
# elif(number == 9):
#     print("IX")
# elif(number == 10):
#     print("X")
# else:
#     print("This number is not between 1 and 10!")






# num = 1.0 - 0.55
# num = round(num, 2)
# print(num)
# if (num == 0.45):
#     print("Forty five")
# else:
#     print("Not forty five")



# a = 0.15 + 0.15
# b = 0.2 + 0.1
# print(a)
# print(b)
# print(abs((a - b)/b))
# if (a == b):
#    print("Equal")
# else:
#     print("Not equal")

# Grade cut-offs
# A_SCORE = 90
# B_SCORE = 80
# C_SCORE = 70
# D_SCORE = 60

# score = int(input("What is your score?"))

# if (score >= A_SCORE):
#     print("Your grade is A")
# elif(score >= B_SCORE):
#     print("Your grade is B")
# elif(score >= C_SCORE):
#     print("Your grade is C")
# elif(score >= D_SCORE):
#     print("Your grade is D")
# else:
#     print("Your grade is F")



# oddNum = (1, 3, 5, 7, 9)
# userInput = int(input("Please enter an odd number between 0-10: "))
# if (userInput in oddNum):
#     print("That's an odd number")
# else: 
#     print("Not an odd number")




# age = int(input("Enter your age in whole years, 18+ only: "))

# while (age < 18 ):
#     if (age <= 0):
#         print("In order to type on this computer you need to be born first!")

#     age = int(input("Enter your age in whole years, 18+ only: "))

# print("Age requirement met, you must now pay to actually use this program.")


# print(range(1, 4, -1))

# for i in range (1, 4, 1):
#     print("i=", i)
# print("Done!")

# i=1
# while (i <= 4):
#     print("i=", i)
#     i = i+1


# i = 0
# total = 0
# for i in range (1, 4, 1):
#     total = total + i
#     print("i=", i, "\ttotal=", total)
# print("Done!")

# for i in range (3, 0, -1):
#     print("i = ", i)
# print("Done!")

# for i in [3, 2, 1]:
#     print("i = ", i)
# print("Done!")






# name = "ILOVENY"

# print("This is how you say your name")
# for ch in name:
#     print(ch, end="**")

# for i in range (5, 0, -1):
#     print("i = ",i)
# print("Done!")



# total = 0
# temp = 0
# while(temp >= 0):
#     temp = input ("Enter a non-negative integer (negative to end  series): ")
#     temp = int(temp)
#     if (temp >= 0):
#         total = total + temp

# print("Sum total of the series:", total)




# age = - 1
# MIN_AGE = 1
# MAX_AGE = 118
# age = int(input("How old are you (1-118): "))
# while ((age < MIN_AGE) or (age > MAX_AGE)):
#     if (age < MIN_AGE):
#         print("Age cannot be lower than", MIN_AGE, "years")
#     else:
#         print("Age cannot be greater than", MAX_AGE, "years")
#     age = int(input("How old are you (1-118): "))

# print("Age=", age, "is age-okay")



# sum = 0
# i = 1
# last = 0

# last = int(input("Enter the last number in the sequence to sum : "))
# while (i <= last):
#     sum = sum + i
#     print("i = ", i)
#     i = i + 1

# print("sum =", sum)




# value = int(input("Enter a positive value: "))

# while(value < 0 ):
#     value = int(input("Enter a positive value: "))

# print("You've yeed your last haw.")

# base = int(input("Enter a number: "))
# exponent = int(input("Enter an Exponent: "))
# finalValue = 1


# while (exponent > 0):
#     finalValue = base*finalValue
#     exponent = exponent - 1

# print("your final value is:", finalValue)

# def getUserInput():
#     age = input("What is your age")
#     print(age)


#     print(age)

# def display(celsius, farenheit):
#     celsius = round(celsius, 2)
#     print("today weather is:", celsius, "celsius", farenheit, "farenheit")

# def convert():
#     celsius = float(input("Enter a celsius value"))
#     farenheit = celsius * 9/5
    
#     display(celsius, farenheit)

#     print("Celcius entered", celsius)
#     print("farenheit", farenheit)


# convert()


# This programs function is to recieve a numerical input and doubles its amount then display it!

# getInput function is for asking the user for a numerical input and returns the amount to the double() function.
def getinput():
    num = float(input("What is your number?: "))

    return(num)

# This function recieves a numerical input value and doubles the amount, the new calculated value is then returned to a display function.
def double(num):
    numDouble = num*2

    return(numDouble)


# This function displays the returned amount from the double functions and displays it.
def display(numDouble):
    print("The value of your number doubled is:", numDouble)

# This function calls upon all the three functions above and starts the program.
def start():
    
    num = getinput()
    numDouble = double(num)
    display(numDouble)

# Program execution begins
start() 



# def getInputs():
#     principle = int(input("Please enter princiap: "))
#     rate = int(input("rate: "))
#     time = int(input("time:"))



# print(getInputs())










