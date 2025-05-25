from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("image")
root.geometry("400x400")

upload=Image.open("Screenshot 2025-01-04 202126.png")

image=ImageTk.PhotoImage(upload)

label= Label(root, image=image, height=300, width=300)
label.place(x=50, y=0)

label2=Label(root, text="This is how you can add an image")
label2.place(x=40, y=350)

root.mainloop()