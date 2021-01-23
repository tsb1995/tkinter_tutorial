from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("TITLE")
root.iconbitmap('./img/Coffee.ico')
root.geometry('400x400')

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
    "Mo",
    "Tu",
    "Wd",
    "Th",
    "Fr",
    "Sa",
    "Su"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
