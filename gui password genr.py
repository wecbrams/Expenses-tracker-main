from tkinter import *
import random
import string

def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(chars, k=12))
    textbox.delete("1.0", END)
    textbox.insert(END, password)

w = Tk()
w.title("Random Password Generator")
w.geometry("700x600")

button = Button(w, text="Click for a random password", bg='orange', fg="black", command=generate_password)
button.pack(pady=20)

textbox = Text(w, fg='white', bg='black', height=2, font=("Arial", 16))
textbox.pack()

w.mainloop()
