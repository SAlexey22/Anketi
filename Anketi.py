import os
import time
import pyautogui
import tkinter
from tkinter import *
from tkinter import ttk

def prozorets ():
    root = Tk()
    root.title("Анкети")

    def broiank():
        izhod = Label(root, text=pole.get())
        izhod.pack()

    pole = Entry(root)
    myLabel = Label(root, text="Въведете броя анкети които ви трябват:")
    kopche = Button(root, text="Да започваме", command=broiank)

    myLabel.pack()
    pole.pack()
    kopche.pack()

    root.mainloop()

prozorets()
#os.startfile('C:\\myprogram.exe')
pyautogui.hotkey('ctrl', 'shift', 'n')
time.sleep(3)

#BrAnk = input("vyvedete broq anketi:")
#fafsafasf
#fasfafsa