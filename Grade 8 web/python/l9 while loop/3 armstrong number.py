# Armstrong number 153 = 1^3 + 5^3 + 3^3 == 153

num = int(input("Enter the number to be checked: "))
sum = 0

temp = num
while temp> 0:
    digit = temp % 10
    sum += digit**len(str(num).strip())
    temp //=10

if num == sum:
    print(num," is an armstrong number")
else:
    print(num," is not an armstrong number")
