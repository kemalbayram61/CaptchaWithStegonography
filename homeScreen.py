from tkinter import * 
from PIL import ImageTk,Image
import cv2

class HomeScreen:
    def __init__(self):
        self.frameSize=()

    def createHomeScreen(self,frames):     
        root = Tk('Main')      
        root.title("Captcha With Stegonography")

        #img=PhotoImage(file=r'images/shoes.jpg')
        img=ImageTk.PhotoImage(Image.open("images/shoes.jpg"))
        
        counterY=10
        counterX=10
        counter=0

        for frame in frames:
            lblIm=Label(root,image=ImageTk.PhotoImage(Image.fromarray(frame,'RGB')),name=(str)(counterX)+(str)(counterY))
            lblIm.image=ImageTk.PhotoImage(Image.fromarray(frame,'RGB'))
            lblIm.pack()
            lblIm.place(x=counterX,y=counterY,width=frame.shape[0],height=frame.shape[1])
            counterX=counterX+frame.shape[0]+10
            counter=counter+1

            if(len(frames)**0.5==counter and counter!=1):
                counterX=10
                counterY=counterY+frame.shape[1]+10
                counter=0
        mainloop()  
        



