# Class creation
class myClass:
    # Private variables
    __piratevar=27

    # private method
    def __privatem(self):
        print("\n I am inside private method")
    
    # function to print value of private variable
    def h(self):
        print("Private Variable value: ", myClass.__piratevar)
f=myClass()
f.h()
f.__piratevar