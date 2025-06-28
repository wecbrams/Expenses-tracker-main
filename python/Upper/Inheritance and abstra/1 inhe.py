# Parent class
class Person(object):
    # __init__ is the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print("Name:", self.name)
        print("ID Number:", self.idnumber)
# Child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        # Calling __init__ of the parent class
        super().__init__(name, idnumber) # Person.__init__(self,name, idnumber)
        self.salary = salary
        self.post = post

# Creating an object instance of Employee
a = Employee('Penguin', 20210401, 15000, "Intern")

# Calling a function of the class Person using its instance
a.display()
