valid = False
while not valid:
    try:
        n=int(input("Enter an number: "))
        while n%2==0:
            print("Bye")
        valid =True
    except ValueError:
        print("Invalid")