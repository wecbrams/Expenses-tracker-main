from abc import ABC, abstractmethod
# Abstract parent class
class Polygon(ABC):

    # Abstract method
    @abstractmethod
    def area(self):
        pass

# Rectangle class
class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Triangle class
class Triangle(Polygon):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2


# Square class
class Square(Polygon):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# Creating objects
r = Rectangle(10, 5)
t = Triangle(8, 4)
s = Square(6)

# Printing areas
print("Rectangle Area:", r.area())
print("Triangle Area:", t.area())
print("Square Area:", s.area())