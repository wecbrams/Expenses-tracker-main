def powerOf4(number):
    count = 0
    # Check if number is power of 2
    if number & (number - 1) == 0:
        while number > 1:
            number >>= 1
            count += 1
        return count % 2 == 0
    return False

number = int(input("Enter your number: "))
if powerOf4(number):
    print(number, "is a power of 4")
else:
    print(number, "is NOT a power of 4")
