class Employees:
    def __init__(self):
        print("Employee created")
    
    def __del__(self):
        print("Destructor called")

def creOB():
    print("Making object")
    obj=Employees()
    print("Function end...")
    return obj
print("Calling the created object function")
obj=creOB()
print("Program End...")
        
