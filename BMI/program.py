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


height = input("How tall are you?(inches only)")
weight = input("How much do you weight?(pounds only)")

CONVERSION_FACTOR_BMI = 703

BMI = 703 * int(weight)/(int(height))**2

BMI = round(int(BMI),1)

print("Your BMI is:", BMI)
