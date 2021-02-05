# Question 13: Using a while loop to generate output outlined in the midterm.
#
# Using a while loop and controlling variables outside, program makes a list of 1-10 number and displays the amount doubled beside each digit.

i = 0
z = 0
print("Number", "  Number*2")
while (i < 10):
    print( i,"\t" ,z, end="\n")
    i = i +1
    z = i*2
    
