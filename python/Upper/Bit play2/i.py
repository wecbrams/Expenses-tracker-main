def checkifsame(num1,num2):
    if((num1^num2)!=0):
        print("Numbers are not equal")
    else:
        print("Both numbers are equal")

num1=int(input("Enter The first number to compare: "))
num2=int(input("Enter The second number to compare: "))
checkifsame(num1,num2)