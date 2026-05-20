from tkinter import *
 
root = Tk()
root.geometry("400x300")
root.title("main")

# Function to open New (Top Level) Window
def topwin():
	# Setting up Top Window
	top = Toplevel()
	top.geometry("180x100")
	top.title("toplevel")
	l2 = Label(top, text = "This is toplevel window")
	l2.pack()

	top.mainloop()

l = Label(root, text = "This is root window")
btn = Button(root, text = "Click here to open another window", command = topwin)

# Arranging widgets
l.pack()
btn.pack()
root.mainloop()

