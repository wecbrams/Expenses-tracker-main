# Take input from user
lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

print("Prime numbers between", lower, "and", upper, "are:")

# Iterate loop from lower to upper
for num in range(lower, upper + 1):
    # All prime numbers are greater than 1
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):  # more efficient check
            if num % i == 0:
                break
        else:
            print(num)
