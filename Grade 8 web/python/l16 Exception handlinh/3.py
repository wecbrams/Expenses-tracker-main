try:
    num1,num2 =eval(input("Enter two numbers, separated by a comma: "))
    result=num1/num2
    print("Result is: ",result)
except ZeroDivisionError:
    print("Division by zero is error !!")
except SyntaxError:
    print("Comma is missing, Enter two numbers, separated by a comma:like 1,2 ")
except:
    print("Wrong Input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")
