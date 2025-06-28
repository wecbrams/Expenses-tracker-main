# Program to check if the user-entered number is even or odd
# Returns true if n is even, else false

def isEvenOdd(n):
    # XOR with 1: if n is even, n ^ 1 == n + 1
    if (n ^ 1 == n + 1):
        return True
    else:
        return False

number = int(input("Enter your number: "))

if isEvenOdd(number):
    print(number, "is Even")
else:
    print(number, "is Odd")
