import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import databaseOperation as db

class loginForm(ttk.Frame):
    def __init__(self,parent,*arags,**kwargs):
        tk.Frame.__init__(self,parent)
        self.parent = parent

        self.parent.protocol("WM_DELETE_WINDOW",self.closing_window)

        window_width = 350
        window_height = 100
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()

        x_position = int((screen_width/2) - (window_width/2))
        y_position = int((screen_height/2) - (window_height/2))

        self.parent.geometry("{}x{}+{}+{}".format(window_width,window_height,x_position,y_position))

        self.widgeter()

    def widgeter(self):
        self.ent_username = ttk.Entry(self.parent)
        self.ent_username.insert(0,"username")
        self.ent_username.bind("<FocusIn>",self.foc_in_username)
        self.ent_username.bind("<FocusOut>",self.foc_out_username)


        self.ent_password = ttk.Entry(self.parent)
        self.ent_password.insert(0,"password")
        self.ent_password.bind("<FocusIn>",self.foc_in_password)
        self.ent_password.bind("<FocusOut>",self.foc_out_password)

        btn_login = ttk.Button(self.parent,text="Login",command=self.submit)
        btn_exit = ttk.Button(self.parent,text="Exit",command=self.closing_window)

        self.ent_username.grid(row=0,column=0,columnspan=3,sticky="nsew")
        self.ent_password.grid(row=1,column=0,columnspan=3,sticky="nsew")

        btn_login.grid(row=2,column=0,sticky="nsw")
        btn_exit.grid(row=2,column=1,sticky="nse")


    def foc_in_username(self, *args):
        if self.ent_username.get() == "username":
            self.ent_username.delete(0, tk.END)

    def foc_out_username(self,*args):
        if not self.ent_username.get():
            self.ent_username.insert(0,"username")

    def foc_in_password(self,*args):
        if self.ent_password.get() == "password":
            self.ent_password.delete(0,tk.END)
            self.ent_password.configure(show="*")

    def foc_out_password(self,*args):
        if not self.ent_password.get():
            self.ent_password.insert(0,"password")
            self.ent_password.configure(show="")

    def closing_window(self):
        answer = messagebox.askyesno("Exit","You want to exit the program?")
        if answer == True:
            self.parent.destroy()

    def submit(self):
        __verify = db.DatabaseManip(self.ent_username.get(),self.ent_password.get())
        __str_verify = str(__verify)
        if __str_verify == "correct":
            self.initialize_mainApplication()
        elif __str_verify is "incorrect":
            messagebox.showerror("Incorrect Password","You have entered incorrect password")
            # add deleter
        elif __str_verify == "notexist":
            messagebox.showerror("Username does not exist","The username you entered does not exist")


    def initialize_mainApplication(self):
        self.parent.destroy()
        self.parent = tk.Tk()
        self.mainApp = mainApplicaiton(self.parent)
        self.parent.mainloop()

class mainApplicaiton(tk.Frame):
    def __init__(self,parent):
        self.parent = parent

if __name__ == "__main__":
    root = tk.Tk()
    loginForm(root)
    root.mainloop()