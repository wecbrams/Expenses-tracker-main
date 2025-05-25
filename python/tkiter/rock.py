from tkinter import *
import random

choices=["rock","paper","scissors"]
user_score=0
com_score=0
user_choice=""
com_choice=""
result=""
result_text=Label()
scores=Label()

def winner(user_choice):
    com_choice=random.choice(choices)
    global user_score, com_score
    if user_choice==com_choice:
        result="It is a tie!"
    elif(user_choice == "rock" and com_choice == "scissors") or \
         (user_choice == "paper" and com_choice == "rock") or \
         (user_choice == "scissors" and com_choice == "paper"):
        result="You win!"
        user_score+=1
    else:
        result="You lose"
        com_score +=1
    result_text.config(text=f"You chose {user_choice} and I chose {com_choice}.   {result}")  
    scores.config(text=f"Your score: {user_score} | My score: {com_score}")  
    return result,com_choice,user_choice,com_score,user_score  
    

def reset():
    global user_score, com_score
    user_score=0
    com_score=0
    result_text.config(text="")
    scores.config(text=f"Your score: {user_score} | My score: {com_score}")

root=Tk()
root.geometry("500x500")
root.title("Rock Paper Scissors")
label = Label(root, text="Choose your weapon")
btn_r=Button(root,text="Rock",bg="white",border=2,fg="red",command=lambda:winner("rock"),height=5,width=15)
btn_p=Button(root,text="Paper",bg="white",fg="green",border=2,command=lambda:winner("paper"),height=5,width=15)
btn_s=Button(root,text="Scissors",bg="white",fg="blue",border=2,command=lambda:winner("scissors"),height=5,width=15)
btn_reset=Button(root,text="reset",command=reset,height=3,width=10)

label.pack()
btn_r.pack()
btn_p.pack()
btn_s.pack()
btn_reset.pack()

result_text=Label(root,text=f"You chose {user_choice} and I chose {com_choice}.   {result}")
scores=Label(root,text=f"Your score: {user_score} | My score: {com_score}")
result_text.pack()
scores.pack()
root.mainloop()