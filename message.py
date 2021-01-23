from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('TITLE GOES HERE')
root.iconbitmap('./img/Coffee.ico')

# Types of popups
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def popup():
    response = messagebox.askyesno("This is my popup!", # Title of Popup
                                        "POPUP!!!!" # Popup Text
                                        )
    if response == 1:
        Label(root, text= "You clicked Yes!").pack()
    else:
        Label(root, text= "You clicked No!").pack()


    # Label(root, text=response).pack()

Button(root, text="Popup", command=popup).pack()






root.mainloop()
