# Question 17: College admission determining program
#
# Program uses a while loop and asks for inputs on their name, SAT score, Highschool Gpa
# and number of extracurricualar avtivities. Then program determines if student should be accepted or not
# into the college. The user is promted the selection again if they wish to add another student.
#

student = True

while (student == True):
    studentName = input("Student name: ")
    combinedSatScore = float(input("Combined SAT score: "))
    highSchoolGpa = float(input("High School GPA: "))
    extraCurricular = int(input("# of extra curricural activities: "))

    if (combinedSatScore >= 1600) and (highSchoolGpa >= 3.0) and (extraCurricular >= 3 and extraCurricular <= 4.9):
        print(studentName, "should be admitted!")
        addStudent = input("Add another student? (y/n): ")
        if (addStudent == "y"):
            student = True
        if (addStudent == "n"):
            student = False

    if (extraCurricular >= 5) and (combinedSatScore >= 1400 and combinedSatScore <= 1599) and (highSchoolGpa >= 2.8):
        print(studentName, "should be admitted!")
        addStudent = input("Add another student? (y/n): ")
        if (addStudent == "y"):
            student = True
        if (addStudent == "n"):
            student = False

    if (combinedSatScore < 1400 ) or (highSchoolGpa < 2.8) or (extraCurricular < 3):
        print(studentName, "should not be admitted!")
        addStudent = input("Add another student? (y/n): ")
        if (addStudent == "y"):
            student = True
        if (addStudent == "n"):
            student = False


        
