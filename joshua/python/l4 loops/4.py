num = int(input("Enter a number to check: "))
if num>1:
    for i in range(2,int(num**0.5)+1):
        if num%i ==0:  # 
            print(f"{num} is not A prime number")
            break
    else: 
            print(f"{num} is A prime number")
else: 
            print(f"{num} is Not A prime number")
# 131   1^3+3^3+1^3 ==131
