def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def divide(x,y):
    return x/y
def modules(x,y):
    return x%y
def floor(x,y):
    return x//y
print("Enter your choice:")
print("a. Add\nb. Subtract\nc. Multiplication\nd. Division\ne. Modules\nf. Floor")
choice = input().lower().strip()
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice =='a':
    print(f"{num1} + {num2} =",add(num1,num2))
elif choice =='b':
    print(f"{num1} - {num2} =",subtract(num1,num2))
elif choice =='c':
    print(f"{num1} x {num2} =",multiplication(num1,num2))

elif choice =='d':
    print(f"{num1} / {num2} =",divide(num1,num2))   
elif choice =='e':
    print(f"{num1} % {num2} =",modules(num1,num2)) 
elif choice =='f':
    print(f"{num1} // {num2} =",floor(num1,num2))
else:
    print("Error: This is invalid input")