from tkinter import *
import time
from random import randint

def Draw(oldframe=None):
    # load = Image.open("rabbit.gif")
    render = PhotoImage(file="rabbit.gif")
    img = Label(text='rabbit', image=render)
    img.place(x=-250, y=-60)
    img.image = render
    img.master.overrideredirect(True)
    img.master.geometry(f"+{randint(0,500)}+{randint(0,500)}")
    img.master.lift()
    img.master.wm_attributes("-topmost", True)

    return img

def Refresher(frame=None):
    print('Placing rabbit')
    frame = Draw(frame)
    frame.after(1000, Refresher, frame)

root = Tk()
Refresher()
root.mainloop()