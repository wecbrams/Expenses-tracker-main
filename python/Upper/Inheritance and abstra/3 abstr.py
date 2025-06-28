# Import necessary packages
from abc import ABC, abstractmethod

# Create a base class
class Animal(ABC):
    # Abstract method
    @abstractmethod
    def move(self):
        pass

# Subclasses
class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can walk and bark")

class Lion(Animal):
    def move(self):
        print("I can walk and roar")

# Driver code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()
