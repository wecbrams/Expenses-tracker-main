from tkinter import *
from random import randint

password= chr(randint(36,126))
def new_rand():
    pass_box.delete(0,END)
    my_password=''
    for x in range(10):
        my_password += chr(randint(36,126))
    pass_box.insert(0,my_password)

window = Tk()

window.title("Random Password Generator")
window.geometry("500x500")
 
label = Label(window, text="Welcome!", bg="white", fg="black")
label.pack()
greeting = Label( text="Click button to generate a password!!", bg="white", fg="black")
greeting.pack()
pass_box = Entry(font=("Times New Roman", 16)) 
pass_box.pack()
bl = Frame(window)
bl.pack()
button = Button(bl, text="Click me!", bg="pink", fg='white',command=new_rand)
button.pack()

password= chr(randint(36,126))


window.mainloop()