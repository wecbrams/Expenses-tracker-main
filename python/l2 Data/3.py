#input a word
text = input("Enter a string: ")
# Reverse String 
# using step value as -1 to iterate in reverse
revText = text[::-1] 
text = revText

print("Reverse of Given String is:")
print(text)

up=text.upper()
print(up)

l= text.lower()
print(l)

print("The length of string ", len(text))