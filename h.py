from tkinter import *

window = Tk()
window.title('Tkinter Sample Window')
window.geometry('300x300')

# Label
greeting = Label(text="Hello User", fg='white', bg='black')

# Button 
button = Button(text="Click me", bg='black', fg='white')

# Entry 
entry = Entry(fg="yellow", bg="blue", width=50)

# Pack the widgets
greeting.pack()
button.pack()
entry.pack()

# Frame with a Label and a Text widget inside
frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()

label = Label(master=frame, text='Sample Frame')
label.pack()

textbox = Text(frame, fg='green', bg='yellow', height=5, width=30)  # Added height and width for Text widget
textbox.pack()

window.mainloop()
