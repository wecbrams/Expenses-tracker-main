value=input("Enter a value to check: ")
reverse=value[::-1]
if(value==reverse):
    print(f"{value}, is a palindrome number")
else:
    print(f"{value}, is not a palindrome number/")