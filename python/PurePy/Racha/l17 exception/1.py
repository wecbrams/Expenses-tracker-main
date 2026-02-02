try:
    num = int(input("Enter a number: "))

    print("The number created is ", num)
except ValueError as ex:
    print("Exception",ex)