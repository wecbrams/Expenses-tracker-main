from tkinter import *
from PIL import Image, ImageTk

root =Tk()
root.title("Images")
root.geometry('350x400')

u = Image.open("m.jpeg")

image=ImageTk.PhotoImage(u)

label =Label(root,image=image, height=200, width=300)
label.pack(x=50, y=0)

label1=Label(root, text="This is how we add imagea")
label.pack(x=40, y=360)

root.mainloop()