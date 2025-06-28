def setornot(number,n):
    if number&(1<<(n-1)):
        print("SET")
    else:
        print("NOT A SET")
number=int(input("Enter a number: "))
n=int(input("Enter bit number: "))
setornot(number,n)