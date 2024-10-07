from tkinter import *
from tkinter import messagebox 

root = Tk()
root.title("Message box")
root.geometry("300x300")

def msg():
    messagebox.showwarning("Alert","Erorr in the box!!")
button = Button(root,text="Scan",command=msg)
button.place(x=40, y=80)

root.mainloop()