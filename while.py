# Natural numbers

# n =int(input("Enter the number of terms: "))

# sum = 0
# i = 0

# while i<=n:
#     sum=sum+i
#     i=i+1

# print("Sum = ",sum)


# Infinit loop
# i=0
# while i<=0:
#     print("I will run forever")


#HCF
num1 =float(input("Enter the first value: "))   
num2 =float(input("Enter the second value: "))   

while(num2 != 0):
    temp=num2
    num2=num1%num2
    num1=temp

hcf = num1

print("HCF num1 and num2 is: ", hcf)

# 153 ==== 1^3+5^3+3^3  == 153

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp \\= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")