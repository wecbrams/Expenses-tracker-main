from textblob import TextBlob
from colorama import Fore, Style, init

init()
print(Fore.CYAN + "🕵️ Welcome to Sentiment Spy!" + Style.RESET_ALL)
name = input(Fore.MAGENTA + "Enter your name: " + Style.RESET_ALL).strip() or "Agent"
history = []

while True:
    text = input(Fore.GREEN + "\n>> " + Style.RESET_ALL).strip()
    if text.lower() == "exit":
        print(Fore.BLUE + "👋 Goodbye " + name + Style.RESET_ALL)
        break

    elif text.lower() == "reset":
        history.clear()
        print(Fore.CYAN + "🧹 History cleared!" + Style.RESET_ALL)
        continue

    elif text.lower() == "history":
        print(Fore.YELLOW + "📜 History:", history, Style.RESET_ALL)
        continue

    if not text:
        print(Fore.RED + "❗ Enter something!" + Style.RESET_ALL)
        continue

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.25:
        mood = "😊 Positive"
        color = Fore.GREEN
    elif polarity < -0.25:
        mood = "😡 Negative"
        color = Fore.RED
    else:
        mood = "😐 Neutral"
        color = Fore.YELLOW

    history.append((text, mood))
    print(color + "Result: " + mood + Style.RESET_ALL)