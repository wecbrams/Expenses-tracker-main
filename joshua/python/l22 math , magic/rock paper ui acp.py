import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Scores
user_score = 0
computer_score = 0

# Function to play game
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a Tie!"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1

    else:
        result = "Computer Wins!"
        computer_score += 1

    # Update labels
    computer_label.config(text="Computer chose: " + computer_choice)
    result_label.config(text=result)

    score_label.config(
        text=f"Your Score: {user_score}    Computer Score: {computer_score}"
    )

# Create window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x350")
window.config(bg="lightblue")

# Title
title_label = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Arial", 20, "bold"),
    bg="lightblue"
)
title_label.pack(pady=10)

# Instruction
instruction_label = tk.Label(
    window,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 12),
    bg="lightblue"
)
instruction_label.pack()

# Buttons Frame
button_frame = tk.Frame(window, bg="lightblue")
button_frame.pack(pady=20)

# Rock Button
rock_button = tk.Button(
    button_frame,
    text="Rock",
    width=10,
    font=("Arial", 12),
    command=lambda: play("Rock")
)
rock_button.grid(row=0, column=0, padx=10)

# Paper Button
paper_button = tk.Button(
    button_frame,
    text="Paper",
    width=10,
    font=("Arial", 12),
    command=lambda: play("Paper")
)
paper_button.grid(row=0, column=1, padx=10)

# Scissors Button
scissors_button = tk.Button(
    button_frame,
    text="Scissors",
    width=10,
    font=("Arial", 12),
    command=lambda: play("Scissors")
)
scissors_button.grid(row=0, column=2, padx=10)

# Computer Choice Label
computer_label = tk.Label(
    window,
    text="Computer chose: ",
    font=("Arial", 14),
    bg="lightblue"
)
computer_label.pack(pady=10)

# Result Label
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 16, "bold"),
    fg="darkblue",
    bg="lightblue"
)
result_label.pack(pady=10)

# Score Label
score_label = tk.Label(
    window,
    text="Your Score: 0    Computer Score: 0",
    font=("Arial", 14),
    bg="lightblue"
)
score_label.pack(pady=20)

# Run window
window.mainloop()