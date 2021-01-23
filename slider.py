from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('TITLE')
root.iconbitmap('./img/Coffee.ico')

vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slide(var):
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL, command=slide)
horizontal.pack()

my_btn = Button(root, text="click me!", command = slide).pack()




root.mainloop()
