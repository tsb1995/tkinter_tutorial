from tkinter import *
# Create initial window widget
root = Tk()

# Setup button function
def myClick():
    myLabel = Label(root, text="Look! I clicked a button")
    myLabel.pack()
# Create label widget to go in root widget
# myLabel1 = Label(root, text="Hello World!")
# myLabel2 = Label(root, text="My Name is Slim Shady")
# myLabel3 = Label(root, text="                 ")
myButton = Button(root, text="Click Me!",
                                padx = 50,
                                pady = 50,
                                command = myClick,
                                fg = "blue",
                                bg = "orange")

# Throw our label widet onto the screen
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=2)
# myLabel3.grid(row=1, column=1)
myButton.pack()

# Get our root loop running
root.mainloop()
