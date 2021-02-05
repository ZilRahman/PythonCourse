# Question 4: Grade calculation program
# This program inputs three test scores and a homework score and calculates the final grade.
# The test scores combined weight 50% and the homework score weight 50% alone.
# 


testScore1 = int(input("Enter your test score 1 (1 - 100): "))

testScore2 = int(input("Enter your test score 2 (1 - 100): "))

testScore3 = int(input("Enter your test score 3 (1 - 100): "))

homeWorkScore = int(input("Enter your homework score (1 - 100): "))

testFinal = (((testScore1 + testScore2 + testScore3)/3) + homeWorkScore)/2

# round function is used for clarification purposes.

testFinal = round(testFinal, 2)

# The final grade is displayed with the number and the letter equivalent. 

if (testFinal < 100 and testFinal > 90):
    print("You scored an A:", testFinal)

elif (testFinal < 89.99 and testFinal > 80):
    print("You scored a B:", testFinal)

elif (testFinal < 79.99 and testFinal > 70):
    print("You scored a C:", testFinal)

elif (testFinal < 69.99 and testFinal > 60):
    print("You scored a D:", testFinal)

elif (testFinal < 65):
    print("You scored an F:", testFinal)

