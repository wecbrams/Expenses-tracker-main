def add(x,y): 
    return x +y
def subtract(x,y): 
    return x - y
def multiply(x,y): 
    return x * y
def divide(x,y): 
    return x / y

num = int(input("Enter the first number: "))
num1 = int(input("Enter the second number: "))
print("Sum :", add(num,num1))
print("Difference:", subtract(num,num1))
print("Product :", multiply(num,num1))
print("Quotient :", divide(num,num1))

# fibonacci sequence  == Each number is the sum of the two numbers before it
"""
0 => first number
1 => s number
0+1 =1
1+1 =2
1+2 = 3
3 +2=5

return fib(n-1)+fib(n-2)
"""