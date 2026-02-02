print("Hello! I am AI BOT.")

name= input("What is you name? : ")
print("Nice to meet you, ",name)

mood = input("How are you feeling today? (good/bad) : ").lower()

if mood=="good":
    print("I'm glad to hear that!")
elif mood=="bad": 
    print("I'm sorry to hear that. Hope things get better soon")
else:
    print("I see. Sometimes it's hard to put feelings into words")

print(f"It was nice chatting with you {name}. Goodday!")
