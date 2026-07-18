# Create a class named flashcard
class flashcard:
    # Constructor to initialize word and meaning
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    # Function to display flashcard details
    def __str__(self):
        # Return the word and its meaning as a string
        return self.word + ' ( ' + self.meaning + ' )'
# List to store flashcards
flash = []

print("Welcome to Flashcard Application")
# Loop to add flashcards
while True:
    word = input("Enter the word you want to add to flashcard: ")
    meaning = input("Enter the meaning of the word: ")
    # Create object and add to list
    flash.append(flashcard(word, meaning))

    option = int(input(
        "Enter 0 if you want to add another flashcard, otherwise enter 1: "
    ))

    # Exit loop if user enters 1
    if option:
        break


# Display all flashcards
print("\nYour Flashcards")

for i in flash:
    print(">", i)