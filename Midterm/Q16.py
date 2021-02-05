# Question 16: Interactive calculator program
# 
# The program asks the user for two numbers as well as an "operation code" 
# ("a" for add, "s" for subtract, "d" for divide or "m" for multiply). 
# Using the information provided perform the specified operation and print the result.
# Note: It is assumed the user will not divide by zero otherwise run-time error is encountered.

numOne = int(input("Number 1: "))

numTwo = int(input("Number 2: "))

selection = " "

while selection not in ("a", "s", "d", "m"):
    print("press (a) to add")
    print("press (s) to substract")
    print("press (d) to divide")
    print("press (m) to multiply")
    
    selection = input("Operation (a/s/d/m): ")

    if selection not in ("a", "s", "d", "m"):
        print("Thats not a valid response")
        selection = " "

    if (selection == "a"):

        dis = numOne+numTwo
        
        print("{} + {} = {}".format(numOne,numTwo,dis))

    if (selection == "s"):

        dis = numOne-numTwo
        
        print("{} - {} = {}".format(numOne,numTwo,dis))

    if (selection == "d"):

        dis = numOne/numTwo
        dis = round(dis, 2)
        
        print("{} / {} = {}".format(numOne,numTwo,dis))

    if (selection == "m"):

        dis = numOne*numTwo
        
        print("{} X {} = {}".format(numOne,numTwo,dis))