def power2(number):
    if number == 0:
        return False
    return (number & (number - 1)) == 0

number = int(input("Enter the number: "))
if power2(number):
    print(number, "is a power of 2")
else:
    print(number, "is NOT a power of 2")
