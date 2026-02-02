def add(p,q):
    return p + q
def subtract(p,q):
    return p - q
def multiply(p,q):
    return p * q
def divide(p,q):
    return p / q
def module(p,q):
    return p % q

print("Select an operator")
print("a. Add\nb. Subtract\nc.Multiply\nd. Division\ne. Remainder")
choice = input("Enter choice(a/b/c/d/e): ").lower()

num = int(input("Enter the first number: "))
num1 = int(input("Enter the second number: "))
if choice == "a":
    print(f"{num} + {num1} = {add(num,num1)}")
elif choice == "b":
    print(f"{num} - {num1} = {subtract(num,num1)}")
elif choice == "c":
    print(f"{num} x {num1} = {multiply(num,num1)}")
elif choice == "d":
    print(f"{num} ➗ {num1} = {divide(num,num1)}")
elif choice == "e":
    print(f"{num} % {num1} = {module(num,num1)}")
else:
    print("This is an invalid input")