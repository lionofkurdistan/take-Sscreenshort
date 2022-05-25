from tkinter import *
from tkinter import ttk
import sys
import pyautogui
import tkinter as tk

from tkinter import filedialog

root=tk.Tk()

canvas1=tk.Canvas(root,width=300,height=300)
canvas1.pack()

def takeScreenshort():
    myScreenshort=pyautogui.screenshot()
    file_path=filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshort.save(file_path)

myButton=tk.Button(text='take Sscreenshort', command=takeScreenshort,bg='black',fg='white',font=10)
canvas1.create_window(150,150,window=myButton)

root.mainloop()
