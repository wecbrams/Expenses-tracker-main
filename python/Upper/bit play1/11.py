def SetOrNot(number,n):
    if number &(1<<(n-1)):
        print("SET")
    else:
        print("\nNot Set")

number=int(input("Enter number: "))
n=int(input("Enter bit number: "))
SetOrNot(number,n)