# Parent class
class Person:
    def __init__(self, fname, lname, idnumber):
        self.firstname = fname
        self.lastname = lname
        self.idnumber = idnumber

    def display(self):
        print(self.firstname, self.lastname)
        print("ID:", self.idnumber)

# Child class
class Student(Person):
    def __init__(self, fname, lname, idnumber, year):
        super().__init__(fname, lname, idnumber) #Person.__init__(self, fname, lname, idnumber)
        self.graduationyear = year

# Creating object
x = Student("Joey", "King", 20210401, 2021)

# Using parent method
x.display()

# Accessing child attribute
print("Graduation Year:", x.graduationyear)