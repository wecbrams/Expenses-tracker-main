def setornot(num, n):
    if num & (1<<(n-1)):
        print("\nSet")
    else:
        print("\nNot Set")
number = int(input("Enter a number: "))
n = int(input("Enter bit number: "))
setornot(number, n)
