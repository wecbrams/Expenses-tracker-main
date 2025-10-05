def divide(ourdividend, ourDivisor):
    # Determine the sign of the answer
    sign = -1 if ((ourdividend < 0) ^ (ourDivisor < 0)) else 1
    # Work with positive values only
    ourdividend = abs(ourdividend)
    ourDivisor = abs(ourDivisor)

    quotientNumber = 0
    tempNumber = 0

    # Check every bit from 31 down to 0
    for i in range(31, -1, -1):
        if (tempNumber + (ourDivisor << i) <= ourdividend):
            tempNumber += ourDivisor << i
            quotientNumber |= 1 << i

    # Apply sign
    if sign == -1:
        quotientNumber = -quotientNumber

    return quotientNumber

# Take input
a = int(input("Enter a for a\b: "))
b = int(input("Enter b for a\b: "))
print("Result of", a, "\n", b, "is", divide(a, b))
