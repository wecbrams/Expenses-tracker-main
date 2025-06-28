# Parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Child class
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

# Creating a Student object
x = Student("Joey", "King", 2021)

# Using methods and properties
x.printname()
print(x.graduationyear)
