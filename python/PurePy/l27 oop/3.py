class Parrot:
    species ="bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

#instant the parrot class
blu=Parrot('Blu',10)
woo=Parrot('Woo',13)

# access the class attributes
print("Blue is ",blu.species)
print("Woo is ",woo.species)

# Access the instance attributes
print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")