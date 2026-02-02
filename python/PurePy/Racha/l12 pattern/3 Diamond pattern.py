rowsize = int(input("Enter rhe number of rows: "))
if rowsize%2==0:
    halfdiarow = int(rowsize/2)
else:
    halfdiarow = int(rowsize/2)+1
space = halfdiarow-1
for i in range(1,halfdiarow+1):
    for j in range(1,space+1):
        print(end=" ")
    space = space -1
    num=1
    for j in range(2*i-1):
        print(end=str(num)) 
        num=num+1
    print()

space = 1
for i in range(1, halfdiarow):
    for j in range(1,space+1):
        print(end=" ")
    space=space+1
    num=1
    for j in range(1,2*(halfdiarow-i)):
        print(end=str(num))
        num = num+1
    print()

