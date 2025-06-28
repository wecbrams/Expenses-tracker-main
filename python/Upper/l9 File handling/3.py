# Program to count number of lines in this file
# Opening the file
file = open("C:/Users/we4Trust/Downloads/Expenses-tracker-main/python/Upper/l9 File handling/Codingal.txt", "r")

# Initialize the counter
Counter = 0
# Reading the file content
Content = file.read()
# Splitting content into lines and storing them in a list
CoList = Content.split("\n")
# Counting non-empty lines
for i in CoList:
    if i.strip():  # This skips blank lines
        Counter += 1

file.close()

print("This is the number of lines in the file:")
print(Counter)
