def power_of_4(number):
    count = 0
    # Edge case: 0 or negative numbers are not powers of 4
    if number <= 0:
        return False
    # Check if number is a power of 2 (only one set bit)
    if number & (number - 1) != 0:
        return False

    # Count the number of bits before the set bit (i.e., position of set bit)
    while number > 1:
        number >>= 1
        count += 1

    # Power of 4 has the single set bit at an even position (0-based)
    return count % 2 == 0

# Take input and check
number = int(input("Enter your number: "))
if power_of_4(number):
    print(number, 'is a power of 4')
else:
    print(number, 'is not a power of 4')
