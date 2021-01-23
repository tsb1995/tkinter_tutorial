from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Frame Test App')
root.iconbitmap('./img/Coffee.ico')

frame = LabelFrame(root,
                                padx = 5,
                                pady = 5)

frame.pack(padx=20, pady=20)

b = Button(frame, text="TEST BUTTON")
b.grid(row=0, column=0)
b2 = Button(frame, text="TEST BUTTON 2")
b2.grid(row=1, column=1)



root.mainloop()
