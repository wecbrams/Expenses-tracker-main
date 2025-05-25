# # Import necessary libraries
# from tkinter import *
# from tkinter import messagebox

# # Setup Tkinter Window
# root = Tk()
# root.geometry("200x200")

# def msg():
# 	messagebox.showwarning("Alert", "Stop! Virus Found.")

# # Adding Button Widget to Window
# button = Button(root, text="Scan for Virus", command=msg)
# button.place(x=40, y=80)

# # Entering main event loop
# root.mainloop()
def myfunction(n):
    for i in range(0,n+1):
        print("First Loop")
        
    j=1
    while(j<=n+1):
        print("Second Loop",j)
        j=j*2
        
    for i in range(0,100):
        print("Third Loop")
myfunction(4)
  