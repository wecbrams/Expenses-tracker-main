# Class definition
class ExpressionSolver:
    # Constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b
  
    # Method to perform calculation
    def calculate(self):
        result = (self.a + self.b) * self.b
        return result 
    # Method to display result
    def display(self):
        print("Result of the expression (a + b) * b =", self.calculate())

# Creating object
obj = ExpressionSolver(5, 3)

# Calling method
obj.display()