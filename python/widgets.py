from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

# Add Label
lbl = Label(root, text="Hey There!", fg="white", bg="#072F5F", height=2, width=300)
lbl.pack()

# Add Label and Entry for user's name
name_lbl = Label(root, text="Full Name", bg="#3895D3")
name_lbl.pack()

name_entry = Entry(root)
name_entry.pack()

# Text Widget to display output
text_box = Text(root, height=5, width=40)
text_box.pack()

# Function to display message
def display():
    name = name_entry.get()
    message = f"Hello {name}\nWelcome to the Application!\nToday's date is: {date.today()}\n"
    
    # Clear the text box before inserting new message
    text_box.delete('1.0', END)
    text_box.insert(END, message)

# Add Button
btn = Button(root, text="Begin", command=display, height=1, bg="#1261A0", fg='white')
btn.pack()

# Run the application
root.mainloop()
