# Program to find the number of bits needed to be swapped to make 2 numbers equal

def totalFlips(number1, number2):
    # XOR the numbers to find differing bits
    xor = number1 ^ number2
    flips = 0

    # Count set bits in XOR result
    while xor > 0:
        flips += xor & 1
        xor >>= 1

    return flips

# Get user input
number1 = int(input("Enter First number: "))
number2 = int(input("Enter Second number: "))

# Output result
print("\nNumber of bit flips needed:", totalFlips(number1, number2))
