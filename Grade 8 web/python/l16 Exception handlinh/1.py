try:
    num = int(input("Enter a number: "))
    print("The number entered is",num)

except ValueError as e:
    print("Exception:",e)