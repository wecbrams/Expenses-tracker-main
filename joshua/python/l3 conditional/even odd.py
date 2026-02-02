num = int(input("Enter the number to check: "))
print("Number to be checked: ",num)

if num > 50:
    print(f"{num} is greater than 50")
    if num%2==0:
     print(f"and also {num} is an even number")
    else:
        print(f"and also {num} is not an even number")
else:
    print(f"{num} is less than 50")
    if num%2==0:
     print(f"and also {num} is an even number")
    else:
        print(f"and also {num} is not an even number")
   
