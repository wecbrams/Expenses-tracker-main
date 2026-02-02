i = int(input("Enter a number: "))
if i<15:
    print("I is smaller than 15")
    print("I'm in if block")

else:
    print("I is larger than 15")
    print("I'm in else block")

print("I'm neither in if nor else Blocks")

# Odd- Even 

number=int(input("Enter Number to check: "))
print("Number to be checked: ",number)
if number%2==0:
    print(number,"is a even number")
else:
    print(number,"is an odd number")