print("Half Pyramid of stars (*)")
n= int(input("Enter the rows: "))
for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    print()