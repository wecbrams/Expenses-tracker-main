num1=int(input("Enter your first numner: "))
num2=int(input("Enter your second numner: "))

a=num1
b=num2

# Euclidean Algorithm
while num2>0:
    r=num1%num2
    num1=num2
    num2=r
print("GCD",num1)

lcm=abs(a*b)\\num1
print(lcm)