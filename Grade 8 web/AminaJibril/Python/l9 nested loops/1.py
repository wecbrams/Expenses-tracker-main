#Take input of a word
string = input("Please enter your own word : ").lower()
#take input of a character
char = input("Please enter your own Character : ").lower()
i = 0
count = 0
#loop will to find the occurence of character
while(i < len(string)): #string operation

    if(string[i] == char): #condition 1
        count = count + 1
    i = i + 1
#Display the result
print("The total Number of Times ", char, " has Occurred = " , count)
