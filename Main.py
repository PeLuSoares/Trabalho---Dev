
from pydoc import doc
from re import L, M
from tkinter import *
from tkinter import font
from turtle import width
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
img_jan2bg = PhotoImage(file="imgs\\jan2bg.png")

#Labels main
lb_bg = Label(mainj, image=img_bg)
lb_bg.pack()
lb_li = Listbox(mainj, font=("Calibri 15 bold"), justify=CENTER,  bg="#caf6ff", width=75)
lb_li.config(selectbackground="black", activestyle="none")
lb_li.place(width=430, height=250, x=210, y=110)


#Functions

def popup():
    #Window creation
    jan2 = Toplevel()
    jan2.title("Adicionar Afazeres")
    jan2.geometry("400x200")
    jan2.resizable(False, False)
    jan2.transient(mainj)
    jan2.focus_force()
    jan2.grab_set()

    #Label
    lb_bg2 = Label(jan2, image=img_jan2bg)
    lb_bg2.pack()
    en_afazer = Entry(jan2, bd=2, font=("Calibri 12 bold"), justify=CENTER)
    en_afazer.place(width=286, height=21, x=57, y=65)




#Buttons

b_new = Button(mainj, image=img_bnew, borderwidth=0, command=popup)
b_new.place(width=84, height=31, x=29, y = 130)

b_del = Button(mainj, image=img_bdel, borderwidth=0)
b_del.place(width=84, height=31, x=29, y = 185)


b_save = Button(mainj, image=img_bsave, bd=0, borderwidth=0)
b_save.place(width=84, height=31, x=29, y = 240)


b_undo = Button(mainj, image=img_bundo, bd=0, borderwidth=0)
b_undo.place(width=84, height=31, x=29, y = 290)

b_mode = Button(mainj, image=img_bmode, bd=0, borderwidth=0)
b_mode.place(width=84, height=31, x=29, y = 376.4)



###################


teste = ["Teste1", "Teste 2"]

for item in teste:
    lb_li.insert(END,item)

mainj.mainloop()