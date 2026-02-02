x=7
if(type(x)is int):
    print("True")
else:
    print ("false")

x=5.0
if (type(x)is not float):
    print("True")
else:
    print("False")

x=20
y=20
if(x is y):
    print("X and Y have SAME identity")

y =30
if(x is not y):
    print("X and Y have Different identity")

# Bitwise
a=10
b=-10
print("a<<1",a<<1)
print("b<<1",b<<1)
print("\na>>1",a>>1)
print("a>>1",a>>1)
