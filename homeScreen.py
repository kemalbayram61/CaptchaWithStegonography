from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class HomeScreen:
    def __init__(self):
        self.frameSize=()

    def createHomeScreen(self):     
        root = Tk('Main')      
        root.title("Captcha With Stegonography")
        img=PhotoImage(file="images/shoes.jpg")
        lblIm=Label(root,image=img)
        lblIm.image=img
        lblIm.pack()
        lblIm.place(x=10,y=10,width=120,height=50)
        mainloop()  

hm=HomeScreen()
hm.createHomeScreen()



