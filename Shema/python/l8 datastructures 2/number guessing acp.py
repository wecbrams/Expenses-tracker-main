import random

secret_number = random.randint(1, 20)
attempts = 5

print("🎮 Welcome to the Number Guessing Game!")
print("You have 5 attempts to guess the number (1–20)")

while attempts > 0:
    guess = int(input("Enter your guess: "))
    attempts -= 1

    if guess == secret_number:
        print("🎉 You won!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    print(f"Attempts left: {attempts}")

if attempts == 0:
    print(f"😢 You lost! The number was {secret_number}")