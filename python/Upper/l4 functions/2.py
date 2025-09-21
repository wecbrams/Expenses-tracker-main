# Factorial of a number using recursion
def recur_factorial(n):
   if n == 1: #false
       return n
   else: #true
       return n*recur_factorial(n-1)

num = int(input("Enter a number"))

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))

"""
Factorial >>= 5x4x3x2x1 = 120
10 >>= 10x9x8x7x6x5x4x3x2x1

recur_factorial(5)

- 5x recur_factorial(4)
- 4xrecur_factorial(3)
- 3x recur_factorial(2)
- 2xrecur_factorial(1)
- 1

2x1=2
3x2=6
4x6=24
5x24 =120
""" 