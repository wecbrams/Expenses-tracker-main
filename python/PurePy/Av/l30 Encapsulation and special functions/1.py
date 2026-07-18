class myClass:
    #private variable
    __privatevar = 25

    #private method
    def __privmeth(self):
        print("I'm inside class myClass")
    def hello(self):
        print("Private variable value: ",myClass.__privatevar)

f= myClass()
f.hello()
f.__privmeth()