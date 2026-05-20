# Armstrong number
# 234  2^3+3^3+4^3 = 
# 371  3^3+7^3+1^3 = 27+343+1 =371
num = int(input("Enter a number: "))  
temp=num
sum = 0
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp //=10
if num == sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
