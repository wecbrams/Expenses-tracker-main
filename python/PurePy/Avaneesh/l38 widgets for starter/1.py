from tkinter import *
from datetime import date

root= Tk()
root.title("Getting started with widgets")
root.geometry('400x300')

lbl =Label(text="Hey There!!", fg="blue", bg='gold',height=2, width=300)
nlbel=Label(text="Full Name",bg='orange')
name_entry=Entry()

def display():
    name = name_entry.get()
    global message
    message = "Welcome to the application! \nToday's date is: "
    greet="Hello "+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box =Text(height=3)

btn = Button(text='Begin',
command=display, height=1, bg='lightblue', fg='red')

lbl.pack()
nlbel.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()