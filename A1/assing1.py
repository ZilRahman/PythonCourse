GPA = 4.0 #Good -m

assingment = float(input("Enter assingment grade point (0-4):"))     #   
midterm = float(input("Enter midterm grade point (0-4):"))           # user inputs marks data (0.0 - 4.0)    
finalExam = float(input("Enter final exam grade point(0-4):"))       #


compactAssignment = (30/100)*assingment         #
compactMidterm = (30/100)*midterm               # formulas to determine weight and calculate GPA
compactFinalExam = (40/100)*finalExam           #

overallGpa = compactAssignment+compactMidterm+compactFinalExam      # compiling marks to get overall GPA
overallGpa = round((overallGpa),2)                                  # round funtion to two decimal points
print("Overall GPA for this class is:", overallGpa)                 # overall GPA results printed

if(overallGpa==GPA):
    print("KISS ASS!!")

    