from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#Creating the window

mainj = Tk()
mainj.title("Habit Tracker By Pedro Lucas S Pitanga")
mainj.geometry("720x430+610+153")
mainj.resizable(width=False, height=False)

#Import background

img_bg = PhotoImage(file="imgs\\background.png")
img_bnew = PhotoImage(file="imgs\\New.png")
img_bdel = PhotoImage(file="imgs\\del.png")
img_bundo = PhotoImage(file="imgs\\undo.png")
img_bsave = PhotoImage(file="imgs\\save.png")
img_bmode = PhotoImage(file="imgs\\light.png")

#Frame creation

f_list = Frame(mainj, width=310, height=300, relief="flat")

#Labels
lb_bg = Label(mainj, image=img_bg)
lb_bg.pack()


#Buttons

b_new = Button(mainj, image=img_bnew, borderwidth=0)
b_new.place(width=84, height=31, x=29, y = 130)

b_del = Button(mainj, image=img_bdel, borderwidth=0)
b_del.place(width=84, height=31, x=29, y = 185)


b_save = Button(mainj, image=img_bsave, bd=0, borderwidth=0)
b_save.place(width=84, height=31, x=29, y = 240)


b_undo = Button(mainj, image=img_bundo, bd=0, borderwidth=0)
b_undo.place(width=84, height=31, x=29, y = 290)

b_mode = Button(mainj, image=img_bmode, bd=0, borderwidth=0)
b_mode.place(width=84, height=31, x=29, y = 376.4)


mainj.mainloop()