num = int(input("Enter a number whose sum you want to find: "))
sum = 0
for i in range(1, num + 1): 
    sum += i
    print("The sum is:", sum)
print("The final sum from 1 to", num, "is:", sum)