import urllib.request
from tkinter import *
from tkinter.tix import *

root = Tk()
root.iconbitmap(default='./img/Coffee.ico')
root.wm_title('Got Skills\' Skill Tracker')
frame = Frame(width="500",height="500")
frame.pack()
swin = ScrolledWindow(frame, width=500, height=500)
swin.pack()
win = swin.window


def show():
  name = "zezima"
  page = urllib.request.urlopen('https://secure.runescape.com/m=hiscore/compare?user1=' + name)
  page = page.readlines()

  skills = []
  for line in page:
    skills.append([line.decode("utf-8").replace("\n", "").split(",")])

  skills = skills[0:25]

  for item in skills:
    toPrint = item[0][0],"-",item[0][1],"-",item[0][1]
    w = Message(win, text=' '.join(toPrint), width=500)
    w.pack()


menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="Commands", menu=filemenu)
filemenu.add_command(label="Show Skills", command=show)


root.mainloop()
