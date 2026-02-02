st=input("Enter your ownwords: ")
ch = input("Enter a character to find its frequency: ")
i =0
count=0
while (i< len(st)):
    if (st[i]==ch):
        count=count+1
    i=i+1
print(f"The total number of times {ch} has occured = {count}")