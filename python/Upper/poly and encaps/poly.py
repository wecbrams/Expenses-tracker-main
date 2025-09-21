class Cat:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def makesound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def makesound(self):
        print("Bark")

cat1 =Cat("Ginger", 3)
dog1 = Dog("Max", 2)

for animal in (cat1, dog1):
    animal.makesound()
    animal.info()