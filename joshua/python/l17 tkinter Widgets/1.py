from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Create main window
root = Tk()
root.title("Image & Alert App")
root.geometry("400x400")

# Load and display image
img = ImageTk.PhotoImage(Image.open("img.jpg"))
Label(root, image=img, width=300, height=300).place(x=50, y=0)

Label(root, text="Image in Tkinter Window").place(x=100, y=310)

# Function for warning message
def show_alert():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

Button(root, text="Scan for Virus", command=show_alert).place(x=120, y=340)

root.mainloop()