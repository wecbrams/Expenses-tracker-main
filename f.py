# def intro(name):
#     print("Hello,\nGood Evening I am ",name)

# user_name=input("Enter Your name: ")
# intro(user_name)

# def rec_fact(n):
#     if n==1:
#         return n
#     else:
#         return n*rec_fact(n-1)
    
# num = int(input("Enter a number you want to check for fasctorials: "))

# if num<0:
#     print("Sorry, factorials doesn't exist for negative numbers;")
# elif num==0:
#     print("Factorial of 0 is 1")
# else:
#     print("The factorial of ",num, "is", rec_fact(num))

# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

def remainder(x, y):
    return x % y

num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

print("Sum :", add(num1, num2))
print("Difference :", subtract(num1, num2))
print("Product :", multiply(num1, num2))
print("Quotient :", divide(num1, num2))
print("Remainder :", remainder(num1, num2))

