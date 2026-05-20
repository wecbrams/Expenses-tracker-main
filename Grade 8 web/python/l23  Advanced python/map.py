num=[1,2,3]
num1=[4,5,6]
result = map(lambda x,y: x + y, num, num1)
print(f"The additiona of two lists:\n{list(result)}")

number=[1,2,3,4,5]
def sq(n):
    return n*n
square =list(map(sq,number))
print(f"Square of numbers in list\n{square}")
