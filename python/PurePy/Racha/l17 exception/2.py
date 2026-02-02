try:
    num,num1=eval(input("Enter two numbers separated by a comma: "))
    result = num/num1
    print("Result is:",result)
except ZeroDivisionError:
    print("OOO..oop!\nDivision with zero is Error!!!")
except SyntaxError:
    print("Comma is missing. Enter numbers separeted by comma like this 1, 2")
except:
    print("Wrong Input")
else:
    print("No exeptions")
finally:
    print("This will execute no matter what")