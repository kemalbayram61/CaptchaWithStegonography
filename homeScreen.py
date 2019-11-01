from tkinter import * 
from PIL import ImageTk,Image

class HomeScreen:
    def __init__(self):
        self.frameSize=()

    def createHomeScreen(self):     
        root = Tk('Main')      
        root.title("Captcha With Stegonography")

        #img=PhotoImage(file=r'images/shoes.jpg')
        img=ImageTk.PhotoImage(Image.open("images/shoes.jpg"))

        lblIm=Label(root,image=img)
        lblIm.image=img
        lblIm.pack()
        lblIm.place(x=10,y=10,width=183,height=183)
        mainloop()  
        

hm=HomeScreen()
hm.createHomeScreen()



