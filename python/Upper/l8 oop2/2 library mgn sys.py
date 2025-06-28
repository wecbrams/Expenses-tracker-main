class Library:
    def __init__(self, book_list, name):
        self.booksList = book_list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"\nBooks available in {self.name}:")
        for book in self.booksList:
            print(f" - {book}")

    def lendBook(self, user, book):
        if book not in self.lendDict:
            self.lendDict[book] = user
            print("You can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}.")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the list.")

    def returnBook(self, book):
        if book in self.lendDict:
            self.lendDict.pop(book)
            print("Thanks for returning the book!")
        else:
            print("That book wasn't lent out.")

# Main interaction loop
if __name__ == '__main__':
    books = Library(
        ['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'],
        "Let's Upskill Library"
    )

    while True:
        print(f"\nWelcome to {books.name}. Choose an option:")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        
        user_choice = input("Enter your choice (1-4): ")

        if user_choice not in ['1', '2', '3', '4']:
            print("❗ Invalid choice. Please enter 1 to 4.")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            books.displayBooks()
        elif user_choice == 2:
            user = input("Enter your name: ")
            book = input("Enter the book you want to lend: ")
            books.lendBook(user, book)
        elif user_choice == 3:
            book = input("Enter the book you want to add: ")
            books.addBook(book)
        elif user_choice == 4:
            book = input("Enter the book you want to return: ")
            books.returnBook(book)

        print("\nPress 'q' to quit or 'c' to continue:")
        user_choice2 = input().lower()
        while user_choice2 not in ['c', 'q']:
            user_choice2 = input("Enter only 'c' or 'q': ").lower()

        if user_choice2 == 'q':
            print("📚 Thank you for using the library system!")
            break
