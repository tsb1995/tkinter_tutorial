from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("TITLE")
root.iconbitmap('./img/Coffee.ico')
root.geometry("400x400")


def show():
    my_label = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check this box!",
                        variable=var,
                        onvalue="on",
                        offvalue="off",
                        )
c.deselect() # Prevent auto checked on to prevent weird bug
c.pack()

my_button = Button(root, text="Click!", command=show).pack()

root.mainloop()
