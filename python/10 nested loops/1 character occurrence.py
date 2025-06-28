# Take input of a word
string = input("Please enter your own word: ")
# Take input of a character
char = input("Please enter a character to count: ")
# Initialize counter
count = 0
i = 0
# Loop through the string
while i < len(string):
    if string[i] == char:
        count += 1
    i += 1

# Display the result
print(f"The total number of times '{char}' has occurred = {count}")
