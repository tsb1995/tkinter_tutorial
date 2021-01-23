from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("TITLE")
root.iconbitmap('./img/Coffee.ico')

def open():
    global my_img # Must be global if generated in new window
    top = Toplevel()
    top.title('Top level window')
    my_img = ImageTk.PhotoImage(Image.open('img/Coffee.ico'))
    lbl = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command = top.destroy)
    btn2.pack()

btn = Button(root, text="Open second window", command=open)

btn.pack()


root.mainloop()
