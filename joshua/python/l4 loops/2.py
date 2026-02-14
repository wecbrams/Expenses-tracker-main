n= int(input("Enter the number of rows: "))
for i  in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

total=sum(range(1,11))
print(f"The sum of natural numbers is {total}")