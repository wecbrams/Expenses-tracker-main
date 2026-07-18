#create a class
class Vehicle :
    def __init__(self, max_speed, mileage):
        #blind argument
        self.max_speed = max_speed
        self.mileage = mileage
#object creation
modelX = Vehicle(240, 18)
#access the variables inside init method
print("Module max speed:", modelX.max_speed)
print("Module mileage:", modelX.mileage)

#Activity 1
#create a class
class student : 
    grade = 10
    print("Hi im a student of Grade", grade)
#create an object
ob = student()