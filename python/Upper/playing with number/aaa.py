value= input("Enter a value too check for palindrome number: ").upper()
reverse = value[::-1]
if value==reverse:
    print(f"{value} is a palindrome number")
else:
    print(f"{value} is not palindrome number")