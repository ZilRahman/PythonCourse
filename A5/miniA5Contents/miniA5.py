from tkinter import *

# Instantiate the tkinter module
window = Tk()


# set the title
window.title('My Awesome program!')

# set the min size of the window
window.minsize(350, 350)


# Function to handle what happens when a button is pressed.
# 1. Create a new popup window when button is pressed
# 2. Add rectangle to popup window
def handle_button():
    newWindow = Tk()

    newWindow.geometry('600x600')

    backgroundFrame = Frame(newWindow, width=202,
                            height=102, background='gold')

    frameOne = Frame(newWindow, width=200, height=100,
                     background='pink')

    backgroundFrame.place(x=49, y=99)

    frameOne.place(x=50, y=100)


# Create a button object
# @arg1: window - the window object in which this button will reside
# @arg2: text - the text to display on this button
# @arg3: font
# @arg4: foreground color
# @arg5: handler for the button, any function passed in here will run once the button is pressed.
btn_one = Button(window, text='PRESS ME', font='freesansbold',
                 fg='Blue', command=handle_button)

# Button is laid onto the top left corner,
# this is only one of the many ways to lay out an element on the window
# you can also use cartesian coordinates and specify the width and height
# of elements
btn_one.grid(column=0, row=0)

# Run a main loop so that the window keep running forever.
window.mainloop()
