from tkinter import *

root = Tk()

# Setup entry box
e = Entry(root,
                width = 50,
                borderwidth = 5)
e.pack()
# Default text in text box
e.insert(0, "Enter Your Name!")

# On click function
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

# Setup button
myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()

root.mainloop()
