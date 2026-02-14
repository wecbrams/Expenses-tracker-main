def fibonacci(n):
    return n-1 + n-2

num = int(input("Enter number to be checked: "))
print(f"Fibonacci series of {num} is {fibonacci(num)}")