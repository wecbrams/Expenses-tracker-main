# create class
class Vehicle:
	# create init method
    def __init__(self, max_speed, mileage):
		# bind the arguments
        self.max_speed = max_speed
        self.mileage = mileage
# Object creation
modelX = Vehicle(240, 18)
# access the variables inside init method
print("Model Max Speed:",modelX.max_speed)
print("Model Mileage:", modelX.mileage)

# Activity 1
# create a class
class student:
	grade = 10
	print("Hi I am a student of grade", grade)
# create an object
ob = student()