# Importing necessary modules from tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Setting up the main window
window = Tk()
window.title("Sir's Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Functions to open and save files
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_edit.insert(END, text)
    window.title(f"Ali Text Editor - {filepath}")
def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"Ali Text Editor - {filepath}")

# Creating the text area and buttons frame
text_edit = Text(window)    
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

# Placing the widgets using grid
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
text_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()