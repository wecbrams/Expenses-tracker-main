class Employee:
    #Constructor
    def __init__(self):
        print("Employee created ")

    #Destructor
    def __del__(self):
        print("Employee Deleted ")
obj=Employee()
del obj