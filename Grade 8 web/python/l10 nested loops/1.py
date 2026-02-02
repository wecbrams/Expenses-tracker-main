string = input("Enter you own word: ")
char = input("Enter your character to check: ")

i =0
count = 0
while (i<len(string)):
    if (string[i] == char):
        count = count + 1
    i = i+1
print(f"The total Number of times {char} has occured = {count}")