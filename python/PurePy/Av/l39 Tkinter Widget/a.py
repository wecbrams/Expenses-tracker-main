# Imporrt necessary libraries
from tkinter import *

#Create Window
root = Tk()
root.title("**Caught you in 4k!**")
root.geometry("400x400")

 # Create a frame to organize elements better
frame = Frame(master=root, height=200, width=200, bg="#b0cdff")

# Add Widgets
# Add Label
lbl1 = label = Label(master=frame, text="Full name", bg="#3f86ff", font=("Arial", 16))
lbl2 = label = Label(master=frame, text="Email ID", bg="#3f86ff", font=("Arial", 16))
lbl3 = label = Label(master=frame, text="Enter Password", bg="#3f86ff", font=("Arial", 16))

# Use Entry Widgets to create a text box for user to enter detials
name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

def display_details():
    name = name_entry.get()
    greet  = f"Hello, {name}! Welcome Caught you in 4k."
    email = email_entry.get()
    password = pass_entry.get()
    print(f"Name: {name}\nEmail: {email}\nPassword: {password}")

# Textbox to display message
textbox = Text(bg="#BEBEBE", fg = "black")

# Add Button, when pressed, message will be displayed
btn = Button(master=frame, text="Create Account", bg="#3f86ff", font=("Arial", 16), command=display_details)

# Arrange all wwidgets

frame.pack(padx=20, pady=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
pass_entry.place(x=150, y=140)
btn.place(x=130, y=210) 
textbox.place(y=250)


# start The GUI event loop
root.mainloop()