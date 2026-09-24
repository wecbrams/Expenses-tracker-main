import random, re
from colorama import Fore, init
init(autoreset=True)
dest = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Alps", "Rockies", "Himalayas"],
    "cities": ["Tokyo", "Paris", "NYC"]
}

jokes = [
    "Programmers hate nature—too many bugs!",
    "Computer sick? Must be a virus!",
    "Travelers are warm from hot spots!"
]

clean = lambda t: re.sub(r"\s+", " ", t.lower().strip())

def recommend():
    p = clean(input(Fore.CYAN + "Beaches, mountains, or cities? "))
    if p in dest:
        print(Fore.GREEN + f"Try {random.choice(dest[p])}!")
    else:
        print(Fore.RED + "Not an option.")

def pack():
    d = input(Fore.CYAN + "How many days? ")
    print(Fore.GREEN + f"Tips for {d} days: clothes, chargers, weather check.")

def chat():
    print(Fore.CYAN + "TravelBot (type recommend / pack / joke / exit)")
    while True:
        c = clean(input(Fore.YELLOW + "> "))
        if c == "recommend": recommend()
        elif c == "pack": pack()
        elif c == "joke": print(Fore.YELLOW + random.choice(jokes))
        elif c == "exit": break
        else: print("Try again.")

chat()
# import re, random
# from colorama import Fore, init

# init(autoreset=True)

# destinations = {
#     "beaches": ["Bali", "Maldives", "Phuket"],
#     "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
#     "cities": ["Tokyo", "Paris", "New York"]
# }

# jokes = [
#     "Why don't programmers like nature? Too many bugs!",
#     "Why did the computer go to the doctor? It had a virus!",
#     "Why do travelers feel warm? Too many hot spots!"
# ]

# def clean(text):
#     return re.sub(r"\s+", " ", text.lower().strip())

# def recommend():
#     pref = clean(input(Fore.CYAN + "Beaches, mountains, or cities? "))
#     if pref not in destinations:
#         print(Fore.RED + "Sorry, I don't have that option.")
#         return

#     while True:
#         place = random.choice(destinations[pref])
#         if clean(input(Fore.GREEN + f"How about {place}? (yes/no) ")) == "yes":
#             print(Fore.CYAN + f"Enjoy your trip to {place}!")
#             break

# def packing():
#     loc = clean(input(Fore.CYAN + "Where to? "))
#     days = input(Fore.CYAN + "How many days? ")
#     print(Fore.GREEN + f"\nPacking tips for {days} days in {loc}:")
#     print("- Versatile clothes\n- Chargers\n- Check the weather")

# def joke():
#     print(Fore.YELLOW + random.choice(jokes))

# def help_menu():
#     print(Fore.MAGENTA + "\nCommands:")
#     print("- recommend\n- packing\n- joke\n- exit\n")

# def chat():
#     print(Fore.CYAN + "Hello! I'm TravelBot.")
#     name = input(Fore.YELLOW + "Your name? ")
#     help_menu()

#     while True:
#         cmd = clean(input(Fore.YELLOW + f"{name}: "))

#         if "recommend" in cmd:
#             recommend()
#         elif "pack" in cmd:
#             packing()
#         elif "joke" in cmd:
#             joke()
#         elif cmd in ("exit", "bye"):
#             print(Fore.CYAN + "Safe travels! 👋")
#             break
#         else:
#             help_menu()

# if __name__ == "__main__":
#     chat()

# import re
# import random
# from colorama import Fore, init

# # Initialize colorama (autoreset ensures each print resets after use)
# init(autoreset=True)

# # Destination & joke data
# destinations = {
#     "beaches": ["Bali", "Maldives", "Phuket"],
#     "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
#     "cities": ["Tokyo", "Paris", "New York"]
# }

# jokes = [
#     "Why don't programmers like nature? Too many bugs!",
#     "Why did the computer go to the doctor? Because it had a virus!",
#     "Why do travelers always feel warm? Because of all their hot spots!"
# ]

# # Helper function to normalize user input (remove extra spaces, make lowercase)
# def normalize_input(text):
#     return re.sub(r"\s+", " ", text.strip().lower())

# # Provide travel recommendations (recursive if user rejects suggestions)
# def recommend():
#     print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
#     preference = input(Fore.YELLOW + "You: ")
#     preference = normalize_input(preference)

#     if preference in destinations:
#         suggestion = random.choice(destinations[preference])
#         print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
#         print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
#         answer = input(Fore.YELLOW + "You: ").lower()

#         if answer == "yes":
#             print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
#         elif answer == "no":
#             print(Fore.RED + "TravelBot: Let's try another.")
#             recommend()
#         else:
#             print(Fore.RED + "TravelBot: I'll suggest again.")
#             recommend()
#     else:
#         print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
#         show_help()

# # Offer packing tips based on user's destination and duration
# def packing_tips():
#     print(Fore.CYAN + "TravelBot: Where to?")
#     location = normalize_input(input(Fore.YELLOW + "You: "))
#     print(Fore.CYAN + "TravelBot: How many days?")
#     days = input(Fore.YELLOW + "You: ")

#     print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
#     print(Fore.GREEN + "- Pack versatile clothes.")
#     print(Fore.GREEN + "- Bring chargers/adapters.")
#     print(Fore.GREEN + "- Check the weather forecast.")

# # Tell a random joke
# def tell_joke():
#     print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

# # Display help menu
# def show_help():
#     print(Fore.MAGENTA + "\nI can:")
#     print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
#     print(Fore.GREEN + "- Offer packing tips (say 'packing')")
#     print(Fore.GREEN + "- Tell a joke (say 'joke')")
#     print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

# # Main chat loop
# def chat():
#     print(Fore.CYAN + "Hello! I'm TravelBot.")
#     name = input(Fore.YELLOW + "Your name? ")
#     print(Fore.GREEN + f"Nice to meet you, {name}!")

#     show_help()

#     while True:
#         user_input = input(Fore.YELLOW + f"{name}: ")
#         user_input = normalize_input(user_input)

#         if "recommend" in user_input or "suggest" in user_input:
#             recommend()
#         elif "pack" in user_input or "packing" in user_input:
#             packing_tips()
#         elif "joke" in user_input or "funny" in user_input:
#             tell_joke()
#         elif "help" in user_input:
#             show_help()
#         elif "exit" in user_input or "bye" in user_input:
#             print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
#             break
#         else:
#             print(Fore.RED + "TravelBot: Could you rephrase?")

# # Run the chatbot
# if __name__ == "__main__":
#     chat()
