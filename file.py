from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("TITLE")
root.iconbitmap('./img/Coffee.ico')

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir = './img',
                                                                        title="Select a file",
                                                                        filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")) # (label for filetype, filetype)
                                                                        ) # Returns the location of the file (directory)

    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(root, image=my_image).pack()

my_btn = Button(root, text="Open File", command=open).pack()







root.mainloop()
