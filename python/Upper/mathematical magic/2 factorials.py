# Function to find and print all factors of a number
def print_factors(number):
    print("The factors of", number, "are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

# Taking input from the user
number = int(input("Enter your number to find its factors: "))
print_factors(number)
