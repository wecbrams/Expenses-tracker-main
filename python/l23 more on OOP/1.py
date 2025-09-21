# create class
class IOString():
 
    def __init__(self):
        self.str1 = ""
 
    def get_String(self):
        self.str1 = input("Enter String : ")
 
    def print_String(self):
        print("Result is :", self.str1.upper())

# Object creation
str1 = IOString()

# Call Method
str1.get_String()
str1.print_String()