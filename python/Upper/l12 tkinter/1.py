from tkinter import *
w=Tk()
w.title("Intro to tkinter")
w.geometry('400x400')

greetings=Label(text="Hello user",fg='white', bg='pink')
button=Button(text="Click here", bg='white', fg='pink')
entry=Entry(fg='lightblue',bg='yellow')

greetings.pack()
button.pack()
entry.pack()

frame = Frame(master=w, relief=RAISED, borderwidth=6) #relief== flat, sunken, groove, ridge, raised
frame.pack()
label=Label(master=frame,text="Frame display")
label.pack()

textbox=Text(fg='yellow', bg='black')
textbox.pack()

w.mainloop()