# Question 9: Even or Odd list print.
#
# Program prints out an even or od dlist from 0-100 depending on user input.
# If input doesn't match then user is re-promted for a valid inout.

selection = "" ""

while selection not in ("even", "odd"):
    
    selection = input("Enter 'even or 'odd': ")
    
    if selection not in ("even", "odd"):
        print("That's not a valid choice!")

    if (selection == "even"):    
        print("""

        HERE WE GO!

        2, 4, 6, 8, 10, 12, 
        14, 16, 18, 20, 22, 
        24, 26, 28, 30, 32, 
        34, 36, 38, 40, 42, 
        44, 46, 48, 50, 52, 
        54, 56, 58, 60, 62, 
        64, 66, 68, 70, 72, 
        74, 76, 78, 80, 82, 
        84, 86, 88, 90, 92, 
        94, 96, 98 and 100
        
        
        """)

    if (selection == "odd"):
        print("""

        HERE WE GO!


        9, 15, 21, 25, 27,
        33, 35, 39, 45, 49,
        51, 55, 57, 63, 65,
        69, 75, 77, 81, 85,
        87, 91, 93, 95, 99

        """)




